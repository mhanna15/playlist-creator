class User(ndb.Model):
    username = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = False)

class Song(ndb.Model):
    artist =  ndb.StringProperty(required = True)
    title = ndb.StringProperty(required = True)
    length = ndb.IntegerProperty(required = True)



