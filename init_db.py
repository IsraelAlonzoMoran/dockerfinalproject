import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Required to load the previously defined environment variables

# Create connection to postgres
conn = psycopg2.connect(host='postgres', port=5432,
                        user=os.environ['DB_USERNAME'],
                        password=os.environ['DB_PASSWORD'],
                        dbname=os.environ['PG_DATABASE'])


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