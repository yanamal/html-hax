from google.appengine.ext import ndb

class UserProfile(ndb.Model):
  user_id = ndb.StringProperty()
  current_passphrase = ndb.StringProperty()

  @classmethod
  def get_by_user(cls, user):
    profile = cls.query().filter(cls.user_id == user.user_id()).get()
    if not profile:
      profile = UserProfile(user_id = user.user_id())
      profile.put()
    return profile
