Description
- The application is designed to allow the user to leave comments. 
- All comments and information about users are stored in the database. 
- The user can edit and delete their own comments

Technologies  
Beck:
- Djando
- WebSockets (Django Channels)
- Docker
- DRF
- Redis (how broker or NOSQL)

Launch

clone this repo   
setup your POSTGRESQL database  
set environment variables: 
for mac export nameenv=value

- DB_HOST
- POSTGRES_DB 
- POSTGRES_PASSWORD;
- POSTGRES_USER 
- SECRET_KEY

run pip install -r requirements.txt   
run python manage.py makemigrations   
run python manage.py migrate    
run python manage.py runserver 127.0.0.1:8080
