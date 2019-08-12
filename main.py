import webapp2
import jinja2
import os
import json
from urllib import urlencode
from google.appengine.api import urlfetch

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class SignUpHandler(webapp2.RequestHandler):
    




app = webapp2.WSGIApplication([

], debug=True)