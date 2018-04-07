#!/usr/bin/env python

import logging, os

from google.appengine.api import users
from profile import UserProfile
from nextpuzzle import nextPuzzle

from flask import Flask,redirect

app = Flask(__name__)

production_environment = os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')
if not production_environment:
    app.debug = True
    logging.info('debugging!')

# TODO: handle all flask things in main?..

@app.route('/')
def home():
  profile = UserProfile.get_by_user(users.get_current_user())
  return redirect('/resources/welcome.html')

# automatically go to the next logical step for this user.
@app.route('/next')
def nextStep():
  profile = UserProfile.get_by_user(users.get_current_user())
  curr = profile.current_puzzle
  return redirect(curr)
