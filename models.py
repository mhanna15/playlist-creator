from google.appengine.ext import ndb

class Song(ndb.Model):
    mood = ndb.StringProperty(repeated = True)
    genre = ndb.StringProperty(required =  True)
    song = ndb.StringProperty(required =  True)
    artist = ndb.StringProperty(required =  True)
    album = ndb.StringProperty(required =  True)
    url = ndb.StringProperty(required =  True)
    mood = ndb.StringProperty(repeated = True)
    activity = ndb.StringProperty(repeated = True)

class User(ndb.Model):
    nickname = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    favorites = ndb.KeyProperty(Song, repeated = True)