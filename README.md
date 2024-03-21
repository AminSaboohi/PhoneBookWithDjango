# Django Phonebook Project
## Overview
This project is a web-based phonebook application developed using the Django framework. It enables users to register and log in to manage a personal phonebook where they can add, view, modify, or delete contact information. The application also supports adding new cities and provinces, allowing for a comprehensive and detailed contact management system. 
## Features
- User registration and authentication.
- Ability to add, view, modify, and delete contact information.
- Direct access to contact details by clicking on the contact's ID.
- Functionalities to add new cities and provinces to the database.
- Clean and intuitive user interface for managing contacts.
## Requirements
All the necessary libraries and dependencies required to run this project are listed in the requirements.txt file. Install them using the following command: 
```
pip install -r requirements.txt
```

## Configuration
Before running the application, you need to configure your local settings. Please copy sample_setting.py to local_setting.py and follow the instructions provided within to set up your database connection and other necessary settings. 
## Setting Up the Database
To prepare your database for the application, run the following Django commands: 

```
python manage.py makemigrations
 ```
```
python manage.py migrate
```

## Running the Application
To start the Django development server, execute: 
```
python manage.py runserver
```
Then, navigate to http://127.0.0.1:8000/ in your web browser to access the application. From there, you can register as a new user or log in if you already have an account. 
## Contributing
Contributions to this project are welcome. If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request. 
