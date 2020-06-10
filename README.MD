# Jenga Payments API

This the Women In Business API for the backend README file. For a consistent workflow, kindly make sure to follow the following DEVELOPMENT guidelines:

### Dependencies
- Python - 3.6x +
- MongoDB

### Cloning
1. Clone the repository to your local machine
```sh
git clone ...
```
### Installation
1. Navigate to project directory:
```sh
$ cd jenga
```
2. Create a Virtual Env for project
```sh
$ python -m venv paymentsenv
```
3. Activate the Virtual ENV:
- ON windows:
```sh
paymentsenv\Scripts\activate.bat
```
- On Linux/Mac
```sh
source paymentsenv/bin/activate
```
4 .Install the project dependencies and devDependencies as follows:
```sh
pip install -r requirements.txt
```

#### NOTE:
If you use a different env name remember to add it to ```.gitignore``` file
Also if you use Pipenv you can ignore ```Pipfile``` and ```Pipfile.lock``` in your git branch.

#### Start DEV Environment

Within your ```virtual environment``` run: 
```sh
python manage.py runserver
```
#### Important Docs, Links and Solution

DB Modelling - http://docs.mongoengine.org/tutorial.html

# WORKING:
Kindly ensure to branch of master for your work 
``` git branch your-branch-name ```

Master Branch will be kept clean for production and you can only merge your changes via a merge request that will be peer reviewed by all project members.

``` KEEP THE MASTER CLEAN ✊🏾👨🏾‍💻```
#### CODE STYLE
- Lets have matching identation: ``` one four space tab or four spaces ```.

###### FOLLOW THE ZEN OF PYTHON:

``` sh
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

