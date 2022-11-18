![Untitled (512 × 481px) (1200 × 500px) (4)](https://user-images.githubusercontent.com/42845567/201497019-2dd93260-117d-4237-99ab-975e3fe21d4a.png)




# Django Topic Board Scaffold - ![Deployed Example](https://baatcheet.app)
# Production Settings Includes
- AWS
- EC2 
- RDS PostgreSQL
- Load Balancer 
- Nginx 
- Gunicorn 
- Domain

## A Scafold Project Enabling CRUD functionality:

- Chat Rooms
- Login
- Sessions 
- Activity
- S3 Profile Images 
- RDS Postgres db

### Follow these steps:

#### 1. Create a project directory, cd into it

    mkdir chatroom  

    cd chatroom  

#### 2. Create and activate virtual environment 

> for macos..

    python3 -m venv venv    

    source venv/bin/activate    

#### 3. Clone the Repo

    git clone https://github.com/engagepy/django_baatcheet

#### 4. Setup a .env file 

> Directory structure for .env:

    baatcheet⮐

    .env

![Screenshot 2022-11-19 at 02 33 40](https://user-images.githubusercontent.com/42845567/202802065-2d0a0ac3-9a7c-481c-a974-5cbbe21ec39a.png)



> add following variables to .env for production: 

    AWS_KEY =      

    AWS_ACC_KEY = 

    BUCKET_NAME = 

    PASSWORD =

    SECRET_KEY =

### or

 > to run locally you only need to add SECRET_KEY to .env: 

    #AWS_KEY =      

    #AWS_ACC_KEY = 

    #BUCKET_NAME = 

    #PASSWORD =

    SECRET_KEY =

#### 5. Install 'requirements.txt'

    pip3 install -r requirements.txt

    python3 manage.py makemigrations

    python3 manage.py migrate --run-syncdb

    python3 manage.py runserver

#### 6. cd into the 'baatcheet' directory 

    cd baatcheet

#### 7. Run ```manage.py```

    python3 manage.py runserver
