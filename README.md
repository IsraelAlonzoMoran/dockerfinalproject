# NCLOUDS | Docker + Docker Compose

## Database

### Configuration


```sql
CREATE DATABASE nclouds_db;
CREATE USER nclouds_user WITH PASSWORD 'nclouds_password';
GRANT ALL PRIVILEGES ON DATABASE nclouds_db to nclouds_user;

```

Run the following command `sudo apt upate`

```bash


```
[This link:](https://ddd.com)

# Install pip 
sudo apt install python3-pip
# Install Flask Flask psycopg2-binary with the below command //make sure to be with the termimal inside your project directory
# this why this dependencies are installed inside your project folder
pip install Flask psycopg2-binary

# Install python-dotenv to allow using the variables that are inside .env 
pip install python-dotenv
#
pip freeze > requirements.txt

# Export 
export FLASK_ENV=app
export FLASK_ENV=development
# then build the docker-compose infrastructure
docker-compose build
# then start the services with docker-compose up
docker-compose up

docker images
docker ps
#docker-postgres(is the container name)
docker exec -it compose_postgres psql -U compose_user compose_db
compose_db=# \du        
CREATE USER frontenduser WITH PASSWORD 'frontendpass';
GRANT ALL PRIVILEGES ON DATABASE compose_db TO frontenduser;

ebian% docker exec -it compose_postgres psql -U compose_user compose_db 
psql (14.2 (Debian 14.2-1.pgdg110+1))
Type "help" for help.

compose_db=# \du
                                     List of roles
  Role name   |                         Attributes                         | Member of 
--------------+------------------------------------------------------------+-----------
 compose_user | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

compose_db=# \list
                                       List of databases
    Name    |    Owner     | Encoding |  Collate   |   Ctype    |       Access privileges       
------------+--------------+----------+------------+------------+-------------------------------
 compose_db | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres   | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0  | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | =c/compose_user              +
            |              |          |            |            | compose_user=CTc/compose_user
 template1  | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | =c/compose_user              +
            |              |          |            |            | compose_user=CTc/compose_user
(4 rows)

compose_db=# \dt
Did not find any relations.
compose_db=# CREATE USER frontenduser WITH PASSWORD 'frontendpass';
CREATE ROLE
compose_db=# GRANT ALL PRIVILEGES ON DATABASE compose_db TO frontenduser;
GRANT
compose_db=# \l
                                       List of databases
    Name    |    Owner     | Encoding |  Collate   |   Ctype    |       Access privileges       
------------+--------------+----------+------------+------------+-------------------------------
 compose_db | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/compose_user             +
            |              |          |            |            | compose_user=CTc/compose_user+
            |              |          |            |            | frontenduser=CTc/compose_user
 postgres   | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0  | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | =c/compose_user              +
            |              |          |            |            | compose_user=CTc/compose_user
 template1  | compose_user | UTF8     | en_US.utf8 | en_US.utf8 | =c/compose_user              +
            |              |          |            |            | compose_user=CTc/compose_user
(4 rows)

compose_db=# \q



# Export Flask app and development(make sure you are with the terminal inside your project directory)
export FLASK_APP=app
export FLASK_ENV=development
# Export the username and and password as well
export DB_USERNAME="your user name"
export DB_PASSWORD="your password"

# With the development server running, visit the following URL using your browser:
http://127.0.0.1:5000/

# Adding New Users