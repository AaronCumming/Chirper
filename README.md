# Chirper


## Description

This is a website that allows users to post messages and replies.


The user can login, view profile, make chirps (messages),
make replies, view other users chirps and replies, and delete their account.


## Usage

To run the program, type the following from the command line:
```
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py runserver
```

Then navigate to the following url on a web broswer:
*    http://127.0.0.1:8000



## Development Team:

Aaron:
* Implemented account sign up and creation.
* Implemented ablilty to delete account with or without deleting the account's chirps.
* Implemented ablilty to create chirps and replies.
* Implemented backend models and views.

Brennan:
* Implemented chirp liking functionality.

Kaylee:
* Made it look nice on the front-end.