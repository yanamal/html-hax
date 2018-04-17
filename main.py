#!/usr/bin/env python

from google.appengine.api import users
from profile import UserProfile

from flask import Flask,redirect

app = Flask(__name__)

# TODO: handle all flask things in main?..

@app.route('/')
def home():
  profile = UserProfile.get_by_user(users.get_current_user())
  return redirect(profile.current_puzzle)

#Quiz Question
def checkDocType():
    answer = request.args.get('struct')
    if answer == 'pass=banana':
        return progress('resources/doctypequiz.html')
    else:
￼       return 'Sorry, that\'s wrong! <a href="/resources/quizquestionissue.html">Try again?</a>'
￼
