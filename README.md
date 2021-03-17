# Easy Flask 🥳

An easy flask template with a sticky footer and proper typography styling. With the help of [TailWindCSS](https://tailwindcss.com) and their [typography package](https://github.com/tailwindlabs/tailwindcss-typography) via their CDN.

- [Easy Flask 🥳](#easy-flask-)
    - [Modules used in this templates](#modules-used-in-this-templates)
    - [Template structure](#template-structure)
    - [Switching between PROD and DEV](#switching-between-prod-and-dev)
    - [Config.py explained](#configpy-explained)
    - [Setting up your `.env` variables](#setting-up-your-env-variables)
- [Docker 🐳](#docker-)

### Modules used in this templates

 - [flask-wtf-forms](https://flask-wtf.readthedocs.io/en/stable/)
 - [python-dotenv](https://github.com/theskumar/python-dotenv)

### Template structure

```bash
.
├── Dockerfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── app.py
├── config.py
├── forms.py
├── requirements.txt
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       └── main.js
└── templates
    ├── about.html
    ├── errors
    │   └── 404.html
    ├── home.html
    ├── layout.html
    ├── login.html
    └── signup.html
```

### Switching between PROD and DEV

We have two configs set up in the `config.py` file. Variables are split between PROD and DEV. You can easily switch between the two environments by using either of the following:

```python
# app.py
app = Flask(__name__)

# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')
```

### Config.py explained

This is how our `config.py` file looks. We load our environment variables using [`python-dotenv`](https://pypi.org/project/python-dotenv/), you're able to use as many variables as you wish. Remeber to add all new variables to your `.env` file.

```python
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get("DEV_DATABASE_URI")
```

### Setting up your `.env` variables

First create a new `.env` file. We need to include a secret key the easiest way to set up your `SECRET_KEY` is to just paste the following into your python console.

```python
import secrets
k = secrets.token_hex(64)
print(k)
```

Then copy the output and place it within your new `.env` file.

```bash
# .env
SECRET_KEY=
PROD_DATABASE_URI=
DEV_DATABASE_URI=
```

# Docker 🐳

This template also includes a `Dockerfile` for you to use. You don't have to use this though. It also includes all the needed files to use the [Container](https://code.visualstudio.com/docs/remote/containers-tutorial) extention within VS Code.

You will more than likely want to change the tag name. You can do this within `.vscode > tasks.json` and the  change the following line:

```json
"tag": "easy_flask:latest",
```