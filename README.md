This is the Readme for QuestMap, a web application to plot your RPG notes on a map!

This project was built using venv as a virtual environment. The virtual environment has been excluded, following good practice.

.gitignore template by Stan Triepels: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
mock maps and data sourced by https://freefantasymaps.org/about/

software requirements and dependencies can be found in requirements.txt

To set up this project on a Linux environment, do the following:

1. Clone the repository:
	git clone https://github.com/PiraTechnics/questmap.git

2. Setup and run virtual environment (venv is installed by default in ubuntu-based distros):
	python -m venv env
	source env/bin/activate

3. Install dependencies into active virtual environment:
	pip install -r requirements.txt

4. Create a .env file with a dummy secret key:
	 echo "SECRET_KEY=dummykey" > .env

5. Create the database. NOTE: you will have to change a line in forms.py first, then migrate, then change it back.
I have no idea why you need to do this, but it breaks otherwise:
	python manage.py migrate

6. Generate a unique secret key using django's shell and replace dummy key with output:
	echo "SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') > .env

7. For Admin management, you'll need to create a Superuser:
	python manage.py createsuperuser

For Windows Environments, the steps are similar, but requires the use of Git-Cli to run commands. Venv may also function differently (especially if you set it up using Windows Powershell). Reccomended Programs for Windows:
- VSCode: https://code.visualstudio.com/
- Git-scm: https://git-scm.com/download/win
