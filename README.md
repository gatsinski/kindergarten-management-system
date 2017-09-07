# kindergarten-management-system
A project designed to help managing one or multiple kindergartens with a single and unified system.


## Creating virtual environment (optional)
Creating a virtual environment is optional but yet highly recommeded.

### Linux/Mac users

* Make sure you have **Python 3** and **pip** installed on your system.
* Open your teminal
* Type `pip install virtualenvwrapper`
* Once the installation is complete enter `mkvirtualenv environment_name -p path_to_python -a path_to_project`. If python 3 is your default Python version you can ommit the *-p path_to_pyhon* and if you don't want the virtual environment to change your active directory every time you enter it you can also ommit the *-a path_to_project* part.
* Enter the following code into your **.bash.rc** / **.bash_profile** and then source it.

    `export WORKON_HOME=$HOME/.virtualenvs`

    `source /usr/local/bin/virtualenvwrapper.sh`
* After the installation your newly created virtual environment will automatically be activated. Next time you want to work on this project just type `workon environment_name`.

### Windows users

* Make sure you have **Python 3** and **pip** installed on your system.
* Open your command prompt
* Type `pip install virtualenvwrapper-win`
* Once the installation is complete enter `mk virtualenv environment_name`
* After the installation your newly created virtual environment will automatically be activated. Next time you want to work on this project just type `workon environment_name`.

## Installation

You will need *Python 3* and *pip* to run this project.

* Enter `kms` inside project's main directory.
* Type `pip install -r requirements.txt` in you terminal/command prompt.
* Type `python manage.py migrate` to apply all database migrations. Currently the default database is SQLite. Edit the settings.py file if you want to use MySQL/MariaDB or PostgreSQL.
* Type `python manage.py createsuperuser` if you need admin rights.
* Type `python manage.py runserver` to start the local server. The default port is 8000, but you can specify different one right after the `runserver` command.


