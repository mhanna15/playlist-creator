import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch
from google.appengine.api import users
from dbload import seed_data
from models import Song, User
import logging


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
    def post(self):
        limit = self.request.get('quantity')
        genre = self.request.get('genre')
        mood = self.request.get('mood')
        # for m in mood:
        #    userMood = m
        logging.info(mood)

        template = jinja_env.get_template('templates/playlist.html')
        songs = Song.query().filter(Song.mood==mood).filter(Song.genre==genre).fetch(limit = int(limit))
        self.response.write(template.render({
            'songs': songs
        }))

class SeedHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('Data Loaded')
class StoreProfileHandler(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        moods = self.request.get('moods')
        genres = self.request.get('genres')
        # playlist_key = Playlist()
        users_key = User(username = username,
                        moods = moods,
                        genres = genres).put()
        self.response.write("{}, {}, {}".format(
            username, moods, genres))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/questions', QuestionsHandler),
    ('/playlist', PlaylistHandler),
    ('/seed', SeedHandler),
], debug=True)
