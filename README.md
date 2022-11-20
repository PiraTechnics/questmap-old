This is the Readme for QuestMap, a web application to plot your RPG notes on a map!

This project was build using venv as a virtual environment. The virtual environment has been excluded, following good practice.

.gitignore template by Stan Triepels: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

software requirements and dependencies can be found in requirements.txt

To set up this project on your own environment, do the following:

1. Clone the repository:
	git clone https://github.com/PiraTechnics/questmap.git

2. Setup and run virtual environment (venv is installed by default in ubuntu-based distros):
	python -m venv env
	source env/bin/activate

3. Install dependencies into active virtual environment:
	pip install -r requirements.txt

4. Create a .env file with a dummy secret key:
	 echo "SECRET_KEY=dummykey" > .env

5. Create the database:
	python manage.py migrate

6. Generate a unique secret key using django's shell and replace dummy key with output:
	echo "SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') > .env

7. Run the server:
	python manage.py runserver

For Admin management, you'll need to create a Superuser:
	python manage.py createsuperuser