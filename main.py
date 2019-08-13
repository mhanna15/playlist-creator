import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch
from google.appengine.api import users


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.redirect("/questions")
    
    # def post(self):
    #     genre = self.request.get(genre)
    #     currentUser = users.get_current_user()
    #     email = currentUser.email()
    #     dbUser = User.query().filter(User.email == email).get()
    #     dbUser.genre = genre
    #     dbUser.put()

    # def post(self):
    #     mood = self.request.get(mood)
    #     currentUser = users.get_current_user()
    #     email = currentUser.email()
    #     dbUser = User.query().filter(User.email == email).get()
    #     dbUser.genre = mood
    #     dbUser.put()

class QuestionsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_env.get_template('templates/questions.html')
        self.response.write(template.render({
            'nickname': user.nickname()

        }))

class PlaylistHandler(webapp2.RequestHandler):
    def get(self):     
        template = jinja_env.get_template('templates/playlist.html')
        self.response.write(template.render())

class StoreProfileHandler(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        moods = self.request.get('moods')
        genres = self.request.get('genres')
        preferredsize = int(self.request.get('preferredsize'))
        # playlist_key = Playlist()
        users_key = Users(username = username,
                        moods = moods,
                        genres = genres,
                        preferredsize = preferredsize).put()
        self.response.write("{}, {}, {}, {}".format(
            username, moods, genres, preferredsize))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/questions', QuestionsHandler),
    ('/playlist', PlaylistHandler)
], debug=True)
