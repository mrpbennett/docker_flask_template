"""
This file is mainly here for `python-dotenv` but you can also use this to store auth_creds.
And then import this module into the one where creds are required like this:

#app.py
import settings

username = settings.auth['username']
password = settings.auth['password']
"""
from dotenv import load_dotenv
import os

load_dotenv()

auth = {"username": os.getenv("USERNAME"), "password": os.getenv("PASSWORD")}

