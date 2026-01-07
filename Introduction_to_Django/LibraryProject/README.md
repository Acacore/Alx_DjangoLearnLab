# Alx_DjangoLearnLab
Alx Project week9 | Django

LibraryProject
Project Overview

LibraryProject is a Django-based project created to introduce the fundamentals of Django development. The project focuses on setting up a Django environment, understanding the default project structure, and building a simple Django app with a Book model. It also demonstrates basic database operations using Django’s Object-Relational Mapper (ORM).

Objectives

Set up a Django development environment

Create and run a Django project

Understand Django’s default project structure

Create a Django app and define a model

Perform basic CRUD operations using Django ORM

Technologies Used

Python 3

Django

SQLite (default Django database)

Project Setup
1. Install Python

Ensure Python is installed on your system:

python --version

2. Install Django

Install Django using pip:

pip install django

3. Create the Django Project

Create the project named LibraryProject:

django-admin startproject LibraryProject


Navigate into the project directory:

cd LibraryProject

4. Run the Development Server

Start the Django development server:

python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/


You should see the default Django welcome page.

Project Structure
LibraryProject/
├── LibraryProject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── README.md

Key Files Explained

settings.py – Contains configuration settings for the Django project

urls.py – Defines URL routes for the project

manage.py – Command-line utility for interacting with the Django project

Bookshelf App
App Creation

Create a Django app named bookshelf:

python manage.py startapp bookshelf


Add the app to INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    ...
    'bookshelf',
]

Book Model

The Book model represents books stored in the system.

Model Definition
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title

Database Migration

Create and apply migrations:

python manage.py makemigrations
python manage.py migrate

Django ORM Operations (CRUD)

Use the Django shell to perform database operations:

python manage.py shell

Create
from bookshelf.models import Book
Book.objects.create(title="Django Basics", author="John Doe", published_year=2024)

Read
Book.objects.all()

Update
book = Book.objects.get(id=1)
book.title = "Advanced Django"
book.save()

Delete
book.delete()

Conclusion

This project demonstrates the foundational concepts of Django, including project setup, app creation, model definition, and database interactions using Django ORM. It serves as a solid starting point for building more complex Django applications.