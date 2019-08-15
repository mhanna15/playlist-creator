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
import random


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/home.html')
        # self.redirect("/home")
        self.response.write(template.render())

class MainHandler(webapp2.RequestHandler):
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
            'nickname': user.nickname(),
            'logout_url':users.create_logout_url('/')
        }))

class PlaylistHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("PLAYLIST HANDLER POST ...")

        # limit = 10

        limit = self.request.get('quantity')
        genre = self.request.get('genre')
        mood = self.request.get('mood')

        logging.info(mood)

        activity = self.request.get('activity')

        logging.info("ACTIVITY:")
        logging.info(activity)

        template = jinja_env.get_template('templates/playlist.html')
        songs = Song.query().filter(Song.mood==mood).filter(Song.genre==genre).filter(Song.activity==activity).fetch()
        print(len(songs), limit)
        numsongs = int(limit)
        if len(songs) > numsongs:
            songs = random.sample(songs, numsongs)
            print(['nelson'])
        self.response.write(template.render({
            'songs': songs
        }))

# class DeleteHandler(webapp2.DeleteHandler):
#     def get(self):

class SeedHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write('Data Loaded')
# class StoreProfileHandler(webapp2.RequestHandler):
#     def post(self):
#         username = self.request.get('username')
#         moods = self.request.get('moods')
#         genres = self.request.get('genres')

#         users_key = User(username = username,
#                         moods = moods,
#                         genres = genres).put()
#         self.response.write("{}, {}, {}".format(
#             username, moods, genres))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/profile.html')
        google_user = users.get_current_user()
        user = User.query().filter(User.email == google_user.email()).get()
        if not user:
            User(email=google_user.email(), nickname=google_user.nickname(), favorites=[]).put()
        self.response.write(template.render({
            'nickname': google_user.nickname(),
            'logout_url': users.create_logout_url('/'),
            'favorites': [Song.get_by_id(key.id()) for key in user.favorites]
        }))

class AddSongHandler(webapp2.RequestHandler):
    def post(self):
        url = json.loads(self.request.body)['url']
        song = Song.query().filter(Song.url == url).get()
        google_user = users.get_current_user()
        user = User.query().filter(User.email == google_user.email()).get()
        user.favorites.append(song.key)
        user.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Song Added')


app = webapp2.WSGIApplication([
    ('/', ProfileHandler),
    ('/questions', QuestionsHandler),
    ('/playlist', PlaylistHandler),
    ('/seed', SeedHandler),
    ('/addsong', AddSongHandler),
    # ('/delete', DeleteHandler),
], debug=True)
