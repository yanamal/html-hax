import json
from google.appengine.api import users
from profile import UserProfile
from flask import Flask

app = Flask(__name__)

# helper function: given the name of the current puzzle,
# decide what the next puzzle should be.
# TODO: getNextPuzzle
def nextPuzzle(curr):
  with app.open_resource('data/puzzleSequence.json') as f:
    puzzles = json.load(f)
    nextp = puzzles[0]
    if curr and (curr in puzzles):
      # TODO: something more efficient and less error-prone.
      i = puzzles.index(curr)
      # if this was the last one, you're done!
      if (i+1) >= len(puzzles):
        return None
      nextp = puzzles[i+1]
    return nextp

# progress user state to the next puzzle (assume current one has just been solved);
# return link to next puzzle, if any.
def progress(curr):
  profile = UserProfile.get_by_user(users.get_current_user())
  nextp = nextPuzzle(curr)
  if nextp:
    profile.current_puzzle = nextp # this is probably fine.
    profile.put()
    return '<a href="/'+nextp+'">Next puzzle!</a>'
  else:
    # no next puzzle
    return 'All done!'
