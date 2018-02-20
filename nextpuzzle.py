import json
from profile import UserProfile
from flask import Flask

app = Flask(__name__)

def nextPuzzle(user):
  profile = UserProfile.get_by_user(user)
  curr = profile.current_puzzle
  profile.solved_puzzles.append(curr)
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
    profile.current_puzzle = nextp # TODO: this is bad?
    profile.put()
    return nextp
# getPuzzleURL, markComplete, getCurrentPuzzle?