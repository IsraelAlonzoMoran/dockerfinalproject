import os
import psycopg2
import postgres
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
                            #="dccompose_db", POSTGRES_USER="dccompose_user", POSTGRES_PASSWORD="postgrespass")
                            #"dbname=dccompose_db user=os.environ['PG_USER'] password=postgrespass port=5432")
                            #host='localhost',
                            #database='flask_db',
                            #user=os.environ['DB_USERNAME'],
                            #password=os.environ['DB_PASSWORD']) 
                            #port="5432",
                            host="localhost",
                            database="dccompose_db",
                            user=os.environ['PG_DATABASE'],
                            password=os.environ['PG_PASSWORD'])

                        
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


#--------------------------------------
"""
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
"""