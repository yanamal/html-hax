
from google.appengine.api import users
from flask import Flask,request,render_template

from profile import UserProfile

import json
import random

from nextpuzzle import nextPuzzle


app = Flask(__name__)

@app.route('/autopass/<puzzle>')
def render_autopass_puzzle(puzzle):
  # get passphrase that was submitted with this request, if any:
  submitted = request.args.get('pass')

  # get current user's passphrase:
  profile = UserProfile.get_by_user(users.get_current_user())

  # see if they submitted the correct one:
  if submitted and (submitted == profile.current_passphrase):
    # TODO: this logic doesn't belong here
    np = nextPuzzle(users.get_current_user())
    value = 'correct! '
    if np:
      value += '<a href="'+request.url_root+np+'">Next Puzzle</a>'
    else:
      value += 'All done!'
    return value

  # fallthrough logic - incorrect or no passphrase submitted:

  # TODO: add extra output on incorrect? (but then it'd be outside of the manual HTML structure)

  # generate a new passphrase:
  passphrase = 'default'
  with app.open_resource('data/passphrases.json') as f:
    passphrases = json.load(f)
    passphrase = random.choice(passphrases)

  # store it in user's profile:
  profile.current_passphrase = passphrase
  profile.put()

  return render_template('autopass/'+puzzle, passphrase=passphrase)

  #return puzzle + ' ' + passphrase
