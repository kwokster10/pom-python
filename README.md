# Creating a Pomodoro Slackbot

## Install the following if you don't have it already from the command line
1. Python
  - check using `which python`
  - install using [Homebrew](http://brew.sh/) `brew install homebrew`
1. pip
  - download [get-pip.py](http://pip.readthedocs.org/en/stable/installing/)
  - run `python get-pip.py` inside the folder it was installed or specify the path

## Recommended: Create a VirtualEnvironment
1. If you do not have Anaconda installed, use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/#introduction)
  - `pip install virtualenv`
  - `pip install virtualenvwrapper`
  - `find / -name virtualenvwrapper.sh`. Use this in `path_from_find` in source below. It should look something like `/usr/local/bin/virtualenvwrapper.sh`
  - Add `export WORKON_HOME=$HOME/.virtualenvs` and `source path_from_find_name` to shell startup file, such as your .bash_profile.
  - Reload your profile e.g. `source `~/.bash_profile`
  - Find your python path using `which python`. Use this below to create your virtual environment
  - `mkvirtualenv --python=path_from_which_python name_for_virtualenv`
1. Otherwise `conda create -n name_for_virtualenv python=x.x`
  - `name_for_virtualenv` is the name you would like to call your virtual environment, e.g. pom_slackbot
  - `x.x` denotes the version of Python to use, e.g. 3.4.3 
  - if you have any troubles, check out this [eResearch cookbook](http://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
- Good resource that describes the difference and incompatibilities on [astropy:docs](http://docs.astropy.org/en/stable/development/workflow/virtual_pythons.html)

## Setting Up File Structure
1. Touch the following files into a new directory
  - app.py
  - requirements.txt
  - runtime.txt
1. `git init` to initialize a new git repo
1. Using the directory name, create a new repo with a README.md and Python .gitignore file on [GitHub](https://github.com/)
1. Copy the SSH key from git and add the remote
  - `git remote add origin git@github.com:name_of_repo`

## Packages For This Project
1. SlackClient: `pip install slackclient`
1. Flask: `pip install Flask`
1. Add dependencies to requirements.txt
  - `pip freeze > requirements.txt`

## If Deploying To Heroku
1. Gunicorn: `pip install gunicorn`
1. `touch Procfile`
  - add `web: gunicorn app:app` and save
1. Add dependency to requirements.txt
  - `pip freeze > requirements.txt`

## Special Thanks
1. [Real Python Blog on Setting Up Flask Project](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)

## Documentation
1. Slackclient
  - [GitHub](https://github.com/slackhq/python-slackclient)
  - [PyPI](https://pypi.python.org/pypi/slackclient)
