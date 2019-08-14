from google.appengine.ext import ndb

class Song(ndb.Model):
    genre = ndb.StringProperty(required =  True)
    song = ndb.StringProperty(required =  True)
    artist = ndb.StringProperty(required =  True)
    album = ndb.StringProperty(required =  True)
    url = ndb.StringProperty(required =  True)
    mood = ndb.StringProperty(repeated = True)

class User(ndb.Model):
    username = ndb.StringProperty(required = True)
    mood = ndb.StringProperty(repeated = True)
    genres = ndb.StringProperty(repeated = True)
    preferredsize = ndb.IntegerProperty(required = True)
    playlist = ndb.KeyProperty(Song, repeated = True)