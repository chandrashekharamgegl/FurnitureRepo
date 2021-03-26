# Furniture_Factory_API

## Setup



$ cd Furniture_Factory_API

$ virtualenv (env_name)

$ ./Scripts/activate


## Then install the dependencies:
$ pip install -r requirements.txt


## Once pip has finished downloading the dependencies:
(env)$ cd FurnitureFactory

## Start the development server
(env)$ python manage.py runserver


### Model requirements
All models are present in the models.py file

### APIs and URLs requirements
Urls are present in urls.py files. Routers have been used here. Once you start the development server API root URLs are visible.

Below are the requested API urls for CRUD operations:

    "table": "http://127.0.0.1:8000/table/",
    
              "http://127.0.0.1:8000/table/<id>",
              
              
    "leg": "http://127.0.0.1:8000/leg/",
    
           "http://127.0.0.1:8000/leg/<id>"
           
           
    "feet": "http://127.0.0.1:8000/feet/"
    
            "http://127.0.0.1:8000/feet/<id>"
            
            
### Admin Requirements
"admin": "http://127.0.0.1:8000/admin/"

username - admin
password - admin123


### Validation Requirements
Data follows the requested custom validations as mentions. All validation are present in serializers.py file.


### Test Cases
As you mentioned, all the test cases are written in the tests.py file.

To run the tests:

  stop the running dev server
  
  (env)$ python manage.py test
  
