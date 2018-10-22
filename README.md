# [Nyumba-Kumi-App](https://nyumbakumiapp.herokuapp.com/)
#### Web application that helps users to know what is happening in their neighbourhood. 
#### October 22th, 2018
#### By **[Evoh Mike](https://github.com/Evohmike/Nyumba-Kumi-App)**

## Description
This is a simple web application that allows users to know more about their neighbourhood.User can join their neighbourhood and also able to create if it doesclone of the awward website. A user can create neigbourhood , create business and post and comment in the neighbourhood they are in.

## Specifications
Find the specs [here]()

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Evohmike/Nyumba-Kumi-App.git && cd Nyumba-Kumi-App

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
python3.6 -m virtualenv env && source env/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE hood;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'hood'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations app
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
No seriuos bugs but if you come across any you can contact me through my email address below.

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on evohmike@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Evoh Mike**