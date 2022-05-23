from flask import Flask, render_template
from flask import Flask, render_template, request, url_for, redirect

# ...
import redis
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Required to load the previously defined environment variables
# take environment variables from .env.
# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='postgres', port=5432,
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'],
                            dbname=os.environ['PG_DATABASE'])

    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)


# ...
# To show the total users entered in the PostgreSQL table
# @app.route('/create/', methods=('GET', 'POST'))
def counter():
    res = []

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM users;')
    userstotal = cur.fetchall()
    print("value:", userstotal)
    cur.close()
    conn.close()
    counters = userstotal
    sql = counters[0]
    res.append(sql[0])
    #here goes redis
    cache = redis.Redis(host='redis', port=6379)
    try:
        res.append(cache.get('counter').decode('utf-8'))
    except redis.exceptions.ConnectionError as exc:
        if retries == 0:
            raise exc
        retries -= 1
    return res
# ...


def postSql():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email, password)'
                'VALUES (%s, %s, %s)',
                (name, email, password))
    conn.commit()
    cur.close()
    conn.close()

def postCache():
    cache = redis.Redis(host='redis', port=6379)
    res = cache.incr("counter")
    return res

@app.route('/create/', methods=('GET', 'POST'))
def create():
    
    if request.method == 'POST':
        if request.form['action'] == 'sql':
            postSql()
        else:
            postCache()
    counters = counter()   
    return render_template('create.html', counters=counters)