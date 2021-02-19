# Flask, Docker Template 🐳

A GitHub template for Flask running docker, also using TailwindCSS via CDN within `index.html`

The template is also set up to use `.env` files via `python-dotenv`.

You will need to create a `.env` of your own, incase the `.gitignore` file didnt catch it during copying of this template.

## Template structure

```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── app.py
├── docker
│   └── Dockerfile
├── requirements.txt
├── settings.py
└── templates
    └── index.html
```

## Simply Flask app

This is the starting point of the Flask app, build on it as you see fit.

```python
from flask import Flask, render_template
import settings

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


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

I have included this as a package for the template as I appericate it's ease of use. You're able to easily use this within the `settings.py` file.

```python
# settings.py

from dotenv import load_dotenv
import os

load_dotenv()

auth = {"username": os.getenv("USERNAME"), "password": os.getenv("PASSWORD")}
```

Then to use the creds you're able to import the settings module into the module which requires the credentials. Like so...

```python
# some module.py
import settings

username = settings.auth['username']
password = settings.auth['password']
```

## Using Tailwind CSS

I have added Tailwind in it's most simplist form, via the CDN. You can read about using Tailwind via it's CDN [here](username = settings.auth['username']
password = settings.auth['password'])

---

## TODO:

- [ ] Bake TailwindCSS properly into the template, to enable all features.
