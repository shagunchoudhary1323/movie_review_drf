# Movie Review API

This is a movie review and recommendation API project built using Django and Django REST framework. This project includes APIs for managing reviews, movies data, searching and filtering the movies and reviews. Users are allowed to perform CRUD operations i.e. users can create, read, update and delete reviews.
Based on the user reviews and movie ratings, some movies will be recommended. User login and sign up apis are built with JWT Authentication.

### Prerequisites
- Python
- Django
- Django Rest Framework

## Software Required

- Python (version - 3.10.7 or above)
- VS Code

## Installation Steps

- Create the virtualenv first, it is a good practice.
 
- Install required software inside virtual environment of project.

- Open this folder in any code editor (for example: VS Code).

- Now open the terminal in the editor.

- To install all of Python's required packages and libraries, we must execute:

```cmd
    pip install -r requirements.txt   
```

- Now to create tables in database, run the following command on terminal:
```cmd
    python manage.py makemigrations
    python manage.py migrate
```

- Now run the server:
```cmd
    python manage.py runserver
```

- On postman , we can test our GET and POST api's for meals as well as orders schema.
  
#### Here is the Postman collection link:

https://shagunpr7-postman-team.postman.co/workspace/shagunpr7-postman-team-Workspac~398eb2c5-d7d0-453b-8622-455180616853/collection/26163677-52a0ec3a-913e-4739-9f85-b43903ba1e9b?action=share&creator=26163677

This Postman collection includes testing api endpoints.






