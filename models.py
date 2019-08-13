class User(ndb.Model):
    username = ndb.StringProperty(required = True)
    moods = ndb.StringProperty(required = True, repeated = True)
    genres = ndb.StringProperty(required = True, repeated = True)
    preferredsize = ndb.IntegerProperty(required = True)
    playlist = ndb.KeyProperty(Playlist, repeated = True)


class Playlist(ndb.Model):
    songs = mdb.StringProperty(required = True, repeated = True)
