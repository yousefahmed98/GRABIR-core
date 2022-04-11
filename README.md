# GRABIR Core - Delivery Website
* [GRABIR UI Repository](https://github.com/yousefahmed98/GRABIR-ui)
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Who we Are?](#who-we-are)

## General info
GRABIR core is the backend or behind the scene part of GRABIR website.
- This project contains normal and admin users with JWT authentication system. 
Each user has his features with profile, posts, offers, deals, notifications, ratings, payments and all CRUD operations.
Normal users can add, edit, delete posts, view others posts, make
offers, recieve notifications, rate another user, complete deals, pay money to another user with Paypal system. 
An admin panel to CRUD over the website, manage all the processes on the website, block, unblock users, promote others to be admins.

## Technologies
- PYTHON
- JWT 
- DJANGO
- RESTFUL-API (DRF) 
- DJOSER
- DJANGO-JASMINE
- POSTMAN
- POSTGRESQL

## Setup
Required to install in your system:
- Github Desktop / Git Bash

Then in yout terminal
```
$ git clone https://github.com/yousefahmed98/GRABIR-core.git
```
- Install python version ‘3.8.6’ from https://www.python.org/downloads/release/python-386/
- Create virtual environment
```
$ python -m venv venv
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install requirements packages for the project
```
$ pip install -r requirements.txt
```
- Install postgres from “https://www.postgresql.org/download/”.
- Install pgAdmin from “https://www.pgadmin.org/download/” then open it.
	##### Create new Database 
	* user: postgres
  * password: admin 
  * name: GRABIR-DB
  
- Open settings.py add this in database section
 ```
DATABASES = 
  {
  'default': {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': 'GRABIR-DB',
  'USER':'postgres',
  'PASSWORD': 'admin',
  },
}  
```
```
$ python manage.py migrate
```
```
$ python manage.py runserver
```
## Features
### What Can Normal User DO?
- Normal users can make CRUD on their profiles
- Normal users can make CRUD on their own posts
- Normal users can make CRUD on their own posts tags
- Normal users can add offers on others posts
- Normal users can add ratings on others profiles
- Normal users can pay money
- If blocked, he cannot log into the system on the login page (Your account is locked, please contact an admin)

### What Can Admin User DO?
- Admin users can make CRUD on posts
- Admin users can make CRUD on profile
- Admin users can block or unblock users
- Admin users can promote a normal user to an admin user so that he will be able to log into the admin screen
- Admin users can CRUD on offers
- Admin users can CRUD on deals
- Admin users can CRUD on notifications
- Admin users can CRUD on ratings
- Admin users can CRUD on messages from contact us
- The Admin page contains links: posts, profile, usera, offers, deals, notifications, deals, and messages
- For normal users, there should be a button that enables the admin to either lock or unlock this user from logging into the system and for the Admin users, this button is not available So, an admin cannot lock another admin

### Admin Dashboard 

![admin dashboard](https://user-images.githubusercontent.com/36454500/162816854-e492f9b3-f3e2-4363-be30-6d83bda58fa2.png)

## Who we Are?
- Intensive Code Camp (ICC) - Information Technology Institute (ITI) - The Egyptian Ministry of Communications and Information Technology (MCIT) Students & Teammates
- We are a Full Stack Web Development Graduates from ITI - Python Stack Track
- We are introducing a GRABIR website with many features using ReactJS framework as a Frontend, django framework as a Backend, and PostgreSQL as a database manager

### - Team members
| Name | Email 📧| 
| :-----: | :-: |
| Rahma Ramadan | rahmaramadan23@gmail.com |
| Yousef Ahmed | yousefa.mohamed12@gmail.com |
| Shrouk Hussien | shrouq.hussein.elsayed@gmail.com |
| Sherif Elshafaey | sherifelshaf3y@yahoo.com |
| Nehal Mohamed | nehalhdev@outlook.com |
