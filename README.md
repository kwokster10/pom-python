# Creating a Pomodoro Slackbot

## Setting Up File Structure
1. Touch the following files into a new directory
  - app.py
  - requirements.txt
  - runtime.txt
1. `git init` to initialize a new git repo
1. Using the directory name, create a new repo with a README.md and Python .gitignore file on [GitHub](https://github.com/)
1. Copy the SSH key from git and add the remote
  - `git remote add origin git@github.com:name_of_repo`

## Recommended: Create a VirtualEnvironment
1. If you do not have Anaconda installed
  -
1. Otherwise run `

## Install the following if you don't have it already from the command line
1. Python
  - check using `which python`
  - install using [Homebrew](http://brew.sh/) `brew install homebrew`
1. pip
  - download [get-pip.py](http://pip.readthedocs.org/en/stable/installing/)
  - run `python get-pip.py` inside the folder it was installed or specify the path
1. SlackClient: `pip install slackclient`
1. Flask: `pip install Flask`

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
