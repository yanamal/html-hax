#!/usr/bin/env python

from flask import Flask,redirect,url_for
from google.appengine.api import users
from profile import UserProfile


app = Flask(__name__)

@app.route('/')
def home():
  profile = UserProfile.get_by_user(users.get_current_user())
  return redirect(profile.current_puzzle)
