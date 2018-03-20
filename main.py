#!/usr/bin/env python

from google.appengine.api import users
from profile import UserProfile
from nextpuzzle import nextPuzzle


from flask import Flask,redirect

app = Flask(__name__)

# TODO: handle all flask things in main?..

@app.route('/')
def home():
  profile = UserProfile.get_by_user(users.get_current_user())
  return redirect('/resources/welcome.html')



@app.route('/next')
def nextStep():
  profile = UserProfile.get_by_user(users.get_current_user())
  curr = profile.current_puzzle
  solved = profile.solved_puzzles
  if curr in solved:
    nextp = nextPuzzle(curr)
    if nextp:
      profile.current_puzzle = nextp # TODO: this is bad?
      profile.put()
      return redirect(nextp)
    else:
      # no next puzzle
      return redirect(nextp)
  else:
    # haven't solved current
    return redirect(curr)
