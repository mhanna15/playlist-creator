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
        self.response.write(template.render())
        google_user = users.get_current_user()
        if google_user:
            nickname = google_user.nickname()
            email = google_user.email()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
            self.response.write(template.render({
                'greeting':greeting
            }));
        else:
            login_url= users.create_login_url('/');
            greeting = '(<a href="{}"> Welcome User!</a>)'.format(login_url)
            self.response.write(template.render({
                'greeting':greeting
            }));


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
], debug=True)
