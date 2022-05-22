# NCLOUDS | Docker + Docker Compose

## Database

### Configuration


```sql
CREATE DATABASE nclouds_db;
CREATE USER nclouds_user WITH PASSWORD 'nclouds_password';
GRANT ALL PRIVILEGES ON DATABASE nclouds_db to nclouds_user;

```
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


