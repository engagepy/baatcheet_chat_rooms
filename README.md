[https://www.canva.com/design/DAFHXCwBsC0/LH7v9hEnP7VsGIk67SZUkA/view?utm_content=DAFHXCwBsC0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton]

# Django Scaffold - AWS > EC2 > RDS PostgreSQL > Load Balancer > Nginx > Gunicorn > Domain

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

    git clone https://github.com/zora89/django_baatcheet.git

#### 4. Setup a .env file 

> Directory structure for .env:

    baatcheet⮐

    .env


> add following variables to .env: 

    AWS_KEY =      

    AWS_ACC_KEY = 

    BUCKET_NAME = 

    PASSWORD =

    SECRET_KEY =

#### 5. Install 'requirements.txt'

    pip3 install -r requirements.txt    

#### 6. cd into the 'baatcheet' directory 

    cd baatcheet    

#### 7. Run ```manage.py```

    python3 manage.py runserver 
