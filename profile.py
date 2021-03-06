from google.appengine.ext import ndb
import json

from flask import Flask

app = Flask(__name__)

class UserProfile(ndb.Model):
  user_id = ndb.StringProperty()
  current_passphrase = ndb.StringProperty()
  current_puzzle = ndb.StringProperty()
  user_email = ndb.StringProperty()
  solved_puzzles = ndb.StringProperty(repeated=True)

  @classmethod
  def get_by_user(cls, user):
    profile = cls.query().filter(cls.user_id == user).get()
    # automatically create blank profile if user doesn't already exist
    # TODO: sometimes duplicates are created?..
    if not profile:
      with app.open_resource('data/puzzleSequence.json') as f:
        puzzles = json.load(f)
        profile = UserProfile(user_id = user, user_email = '',
                              solved_puzzles=[], current_puzzle = puzzles[0])
        profile.put()
    return profile
