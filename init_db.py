import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
conn = psycopg2.connect(
        #POSTGRES_DB="dccompose_db", POSTGRES_USER="dccompose_user", POSTGRES_PASSWORD="postgrespass"

                          host="localhost",
                            database="dccompose_db",
                            user=os.environ['PG_DATABASE'],
                            password=os.environ['PG_PASSWORD'])

#"dbname=dccompose_db user=os.environ['PG_USER'] password=postgrespass port=5432")
        #host="localhost",
        #database="flask_db",
        #user=os.environ['DB_USERNAME'],
        #password=os.environ['DB_PASSWORD']

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'name varchar (100) NOT NULL,'
                                 'email varchar (50) NOT NULL,'
                                 'password varchar (50) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            ('Israel Alonzo',
             'israelalonzo@gmail.com',
             'docker12345')
            )


cur.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            ('Logan Diaz',
             'logandiaz@gmail.com',
             'compose12345')
            )

conn.commit()

cur.close()
conn.close()