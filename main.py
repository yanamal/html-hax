#!/usr/bin/env python

# Import python libraries:
import logging, os
import json
import random

# Import third-party libraries:
from google.appengine.api import users
from flask import Flask,redirect,request,render_template

# Import our own files:
from profile import UserProfile
from nextpuzzle import progress

# make the flask app:
app = Flask(__name__)

# Set up debug messages, when not in "real world" production mode
production_environment = os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')
if not production_environment:
    app.debug = True
    logging.info('debugging!')

# When user goes to home page, redirect to static welcome page
@app.route('/')
def home():
  return redirect('/resources/welcome.html')

# when user goes to /next,
# figure out the next logical step for this user and redirect there.
@app.route('/next')
def nextStep():
  profile = UserProfile.get_by_user(users.get_current_user())
  return redirect(profile.current_puzzle)

@app.route('/dummyprofile')
def renderDummyProfile():
  username = 'Fake User'
  current_puzzle = 'fake/url.html'
  total_puzzles = 8
  completed_puzzles = ['autopass/hello-world.html','resources/doctypequiz.html']
  num_completed = 2
  return render_template('profile.html',
                          user=username,
                          curr=current_puzzle,
                          total=total_puzzles,
                          completed_count=num_completed,
                          completed_urls=completed_puzzles)

@app.route('/dummyheadertest')
def renderDummyPuzzle():
  puzzlename = 'Fake Puzzle'
  total_puzzles = 8
  num_completed = 2
  prev_puzzle = 'fake/url.html'
  return render_template('autopass/hello-world-inherit.html',
                          puzzle_name=puzzlename,
                          completed_count=num_completed,
                          total=total_puzzles) 

# check the doc type quiz question
@app.route('/doctypeanswer')
def checkDocType():
  answer = request.args.get('struct') # get what was submitted in the struct field
  if answer == 'opt2': # compare to correct answer
    # if correct, then use the progress() function to progress from this puzzle
    return progress('resources/doctypequiz.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
    # progress() also marks the current puzzle as solved for this user.
  else:
    # wrong answer - return a short snippet of HTML to send them back to the same quiz.
    return 'Sorry, that\'s wrong! <a href="/resources/doctypequiz.html">Try again?</a>'

# check the doc type quiz question
@app.route('/viccorrect')
def checkVicCorrect():
  answer = request.args.get('choice') # get what was submitted in the struct field
  if answer == 'Dogs': # compare to correct answer
    # if correct, then use the progress() function to progress from this puzzle
    return progress('resources/VicsQuiz.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
    # progress() also marks the current puzzle as solved for this user.
  else:
    # wrong answer - return a short snippet of HTML to send them back to the same quiz.
    return 'Sorry, that\'s wrong! <a href="/resources/VicsQuiz.html">Try again?</a>'

@app.route('/kennedyanswer')
def checkForm():
  answer = request.args.get('form') # get what was submitted in the struct field
  if answer == '<form>': # compare to correct answer
    # if correct, then use the progress() function to progress from this puzzle
    return progress('resources/selecttheform.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
    # progress() also marks the current puzzle as solved for this user.
  else:
    # wrong answer - return a short snippet of HTML to send them back to the same quiz.
    return 'Sorry, that\'s wrong! <a href="/resources/selecttheform.html">Try again?</a>'

@app.route('/youranswer')
def headertype():
  answer = request.args.get('heading') # get what was submitted in the struct field
  if answer == 'opt1': # compare to correct answer
    # if correct, then use the progress() function to progress from this puzzle
    return progress('resources/daizhaquiz.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
    # progress() also marks the current puzzle as solved for this user.
  else:
    # wrong answer - return a short snippet of HTML to send them back to the same quiz.
    return 'Sorry, that\'s wrong! <a href="/resources/daizhaquiz.html">Try again?</a>'

@app.route('/daletypeanswer')
def daleDocType():
  answer = request.args.get('struct') # get what was submitted in the struct field
  if answer == 'opt1': # compare to correct answer
    # if correct, then use the progress() function to progress from this puzzle
    return progress('resources/dalequiz.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
    # progress() also marks the current puzzle as solved for this user.
  else:
    # wrong answer - return a short snippet of HTML to send them back to the same quiz.
    return 'Sorry, that\'s wrong! <a href="/resources/dalequiz.html">Try again?</a>'


# check the doc type quiz question
@app.route('/quizanswer')
def quiz():
  answer = request.args.get('question') # get what was submitted in the struct field
  if answer == '1': # compare to correct answer
    # if correct, then use the progress() function to progress from this puzzle
    return progress('resources/newquiz.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
    # progress() also marks the current puzzle as solved for this user.
  else:
    # wrong answer - return a short snippet of HTML to send them back to the same quiz.
    return 'Sorry, that\'s wrong! <a href="/resources/newquiz.html">Try again?</a>'


# when user navigates to an autopass puzzle, either display the puzzle,
# or (if this is a correct solution) move on to the next puzzle
@app.route('/autopass/<puzzle>')
def render_autopass_puzzle(puzzle):
  # get passphrase that was submitted with this request, if any:
  submitted = request.args.get('pass')
  # get current user's passphrase:
  profile = UserProfile.get_by_user(users.get_current_user())
  # see if they submitted the correct one:
  if submitted and (submitted == profile.current_passphrase):
    profile.solved_puzzles.append('autopass/'+puzzle)
    profile.put()
    value = 'correct! '
    value += progress('autopass/'+puzzle)
    return value

  # fallthrough logic - incorrect or no passphrase submitted:

  # TODO: add extra output on pass submitted, but incorrect?
  # (but then it'd be outside of the manual HTML structure)

  # generate a new passphrase:
  passphrase = 'default'
  with app.open_resource('data/passphrases.json') as f:
    passphrases = json.load(f)
    passphrase = random.choice(passphrases)

  # store it in user's profile:
  profile.current_passphrase = passphrase
  profile.put()

  return render_template('autopass/'+puzzle, passphrase=passphrase)

@app.route('/answer')
def CheckForm():
    answer = request.args.get('pass') # get what was submitted in the struct field
    if answer == 'pass=banana': # compare to correct answer
      # if correct, then use the progress() function to progress from this puzzle
      return progress('resources/quizquestionissue.html') # progress() takes in the name of the current puzzle, and returns a link to the next one
      # progress() also marks the current puzzle as solved for this user.
    else:
      # wrong answer - return a short snippet of HTML to send them back to the same quiz.
      return 'Sorry, that\'s wrong! <a href="/resources/quizquestionissue.html">Try again?</a>'
