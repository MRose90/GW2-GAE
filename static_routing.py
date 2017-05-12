import webapp2
import jinja2
import os
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class Legal(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/legal.html')
        self.response.write(template.render())

class Legal2(webapp2.RequestHandler):
    def get(self):
        self.redirect('/legal')
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/legal/', Legal2),
    ('/legal', Legal),
], debug=True)

