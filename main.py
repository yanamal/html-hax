#!/usr/bin/env python

from flask import Flask
from google.appengine.api import users

from requireauth import *

app = Flask(__name__)

@app.route('/')
@requires_auth
def home():
  return 'Hello World!'
