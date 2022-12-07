#!/bin/bash

# Setup Script for QuestMap forking/further development
# Intended for Uubuntu and other debian-based dev environments
# Run this in the project directory (~/questmap)
# Required packages: venv, python3, python-is-python3, python3-pip

# Updating packages for Python and Django development
sudo apt update -y && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-respository ppa:deadsnakes/ppa -y
sudo apt install python3 python-is-python3 python3-pip -y

# Setting up venv
python -m venv env
source env/bin/activate
pip install -r requirements.txt

# Setting up Django project files and dependencies
echo "SECRET_KEY=dummkey" > .env
python manage.py migrate
echo "SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') > .env
python manage.py createsuperuser

# Project should now be set up, including a uniquely-generated Secret Key,
# an instantiated Database, and an Admin Panel SuperUser. Run the Server to start:

# python manage.py runserver

# Don't forget to deactivate env when finished in relevant terminals:
# deactivate