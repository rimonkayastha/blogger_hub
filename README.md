# BLOGGER'S HUB

## Website to write, post, edit and view blog posts written by you and other users.

This project is a practice project developed while learning the Django framework as part of my internship at Calcgen Solutions. While influenced from the DjangoGirls' intro to Django, this project was built from scratch to revise fundamental aspects of developing a Django web app. Currently, Blogger's hub meets the following functionalities:

* Sign up and login with a secure authentication system
* Edit account details
* Create blog posts with option to upload images
* Edit and delete blog posts
* Read and like other users' blog posts in a grid format with pagination
* Open a post to view the full content
* Search for posts using post title or author

## How to install this practice project

The easiest way to set up the project would be as follows:
* Clone this repo
* Activate the virtual environment through the myvenv directory
* Install Django 5.2.4 using pip. Follow the Django Documentation guide - [Django Installation Guide](https://www.djangoproject.com/download/)
* In the [blogger_hub_project](./blogger_hub_project/) directory, open terminal and run: `$ python manage.py runserver`

## Known Issues (Work in Progress)

This project is still ongoing. Certain tasks such as adding an admin honeypot, login page redirect when user is not authenticated, etc. are still yet to be added. Stay tuned!