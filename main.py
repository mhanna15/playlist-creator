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
        google_user = users.get_current_user()

        # If the user exists, then grab more info
        if google_user:
            nickname = google_user.nickname()
            email = google_user.email()
            self.response.write(template.render({
                'login': users.create_logout_url('/'),
                'nickname': nickname,
                'email': email
            }))
        else:
            self.response.write(template.render({
                'login': users.create_login_url('/')
            
            }))

class QuestionsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/questions.html')

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/questions.html', QuestionsHandler),
], debug=True)
