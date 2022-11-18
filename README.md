![Untitled (512 × 481px) (1200 × 500px) (4)](https://user-images.githubusercontent.com/42845567/201497019-2dd93260-117d-4237-99ab-975e3fe21d4a.png)




# Django Topic Board Scaffold - Deployed Example @ [BaatCheet.app](https://baatcheet.app)
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

##### Directory structure for .env:

    baatcheet⮐

    .env
    
    manage.py

![Screenshot 2022-11-19 at 02 52 49](https://user-images.githubusercontent.com/42845567/202804845-53e760f8-fabe-4d88-bbcd-b9ba593e7a20.png)


##### Add following variables to .env for production: 

    AWS_KEY =      

    AWS_ACC_KEY = 

    BUCKET_NAME = 

    PASSWORD =

    SECRET_KEY =

##### Update following variables in settings.py for production:


    DATABASES = {
        'default': {
            'ENGINE': ,
            'NAME': ,
            'USER': ,
            'PASSWORD': os.environ['PASSWORD'],
            'HOST': ,
            'PORT': ,

        }
    }
##### or

##### To run the project locally only add SECRET_KEY to .env: 

    #AWS_KEY =      

    #AWS_ACC_KEY = 

    #BUCKET_NAME = 

    #PASSWORD =

    SECRET_KEY =

#### 5. Install `requirements.txt` , `makemigrations`, `migrate` -> `runserver` 

    pip3 install -r requirements.txt

    python3 manage.py makemigrations

    python3 manage.py migrate --run-syncdb

    python3 manage.py runserver

#### 6. cd into the 'baatcheet' directory 

    cd baatcheet

#### 7. Run ```manage.py```

    python3 manage.py runserver
