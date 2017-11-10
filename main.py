""""""


import logging
import webapp2
import json
from os.path import join, dirname
from prediction import Prediction
from google.appengine.api import users
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logging.debug(user)
        if user:
            path = join(dirname(__file__), "homepage.html")
            self.response.out.write(template.render(path, None))
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        response = {
            "data": "Dummy data"
        }
        data = self.request.body
        logging.info("---------------------------")
        logging.info(data)
        logging.info("---------------------------")
        Prediction().get_abstract_data(json_data=data)
        self.response.headers['content-Type'] = 'application/json'
        self.response.out.write(json.dumps(response))

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
