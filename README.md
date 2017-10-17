# Yummy Recipes

Create and manage your recipes on the fly

## Prerequisites

# INSTALLATION AND GUIDE

1. clone/download the project into the directory of your choice

- First, in the config.py file in your root directory and fill in your database configuration you can also do this using environment variable

# requirements

    You can find them in the requirements.txt file at the application root folder

-> The project has been run and tested with python version 3.6

-> Recommendend running the project in a virtual environment


2. Create a virtual environment

          $ python3 -m venv .env                   # creates a virtual environment
          $ source .env/bin/activate                # start the virtual environment

3. Install the project's requirements 

          $ pip install requirements.txt           # download and install project's dependancies

4. Initialise your database

        $ python manage.py db init && python manage.py db migrate && python manage.py db upgrade

5. Run your server

          $ chmod +x ./start.sh && ./start.sh         # starts project
          # This command starts your server on https://localhost:8000

## testing

1. Run your server

          $ chmod +x ./test.sh && ./test.sh
