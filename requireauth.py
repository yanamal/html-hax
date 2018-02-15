#!/usr/bin/env python

from flask import request
from functools import wraps
from google.appengine.api import users


def login(redirect='/'):
  return ('Please <a href="%s">log in</a>.' % users.create_login_url(redirect))


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    user = users.get_current_user()
    if user:
      return f(*args, **kwargs)
    else:
      return login(request.full_path)
  return decorated
