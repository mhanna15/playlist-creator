class User(ndb.Model):
    username = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    preferences = ndb.StringProperty(required = True, repeated = True)
    genre = ndb.StringProperty(required = True, repeated = True)


class Song(ndb.Model):
    artist =  ndb.StringProperty(required = True)
    title = ndb.StringProperty(required = True)
    length = ndb.IntegerProperty(required = True)
