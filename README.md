# Flask, Docker Template 🐳

A GitHub template for Flask running docker, also using TailwindCSS via CDN within `layout.html`

The template is also set up to use `.env` files via `python-dotenv`.

You will need to create a `.env` of your own, incase the `.gitignore` file didnt catch it during copying of this template.

## Template structure

```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── app.py
├── config.py
├── docker
│   └── Dockerfile
├── requirements.txt
├── static
│   ├── css
│   │   └── main.css
│   └── js
│       └── main.js
└── templates
    ├── home.html
    └── layout.html
```

## Simply Flask app

This is the starting point of the Flask app, build on it as you see fit.

```python
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("config.DevConfig")


@app.route("/")
def function_name():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
```

### Packages included in template

- [`flask`](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [TailWindCSS via their CDN](https://tailwindcss.com)

## Using Flask

The only thing you will need to do, is before running / building your app you will need to `export FLASK_APP=app.py` in your terminal


## Using python-dotenv

I have included this as a package for the template as I appericate it's ease of use. You're able to easily use this within the `config.py` file.

```python
# settings.py
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
    # DATABASE_URI = environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    # DATABASE_URI = environ.get('DEV_DATABASE_URI')
```

Then to use the creds, outside of your `app.py` you're able to import the config module into the module which requires the credentials. Like so...

```python
# some module.py
import config

c = Config()

c.SOMEENV_VAR
```

## Using Tailwind CSS

I have added Tailwind in it's most simplist form, via the CDN. You can read about using Tailwind via it's CDN [here](https://tailwindcss.com/docs/installation#using-tailwind-via-cdn)

---

