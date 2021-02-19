"""
This file is mainly here for `python-dotenv` but you can also use this to store auth_creds
"""
from dotenv import load_dotenv
import os

load_dotenv()

auth = {"username": os.getenv("USERNAME"), "password": os.getenv("PASSWORD")}

