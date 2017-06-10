import webapp2
import jinja2
import json
import os
from datetime import datetime
import pickle
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FP_Prices(ndb.Model):
    fid = ndb.IntegerProperty()
    weaponsmith = ndb.PickleProperty()
    huntsman = ndb.PickleProperty()
    artificer = ndb.PickleProperty()
    armorsmith = ndb.PickleProperty()
    leatherworker = ndb.PickleProperty()
    tailor = ndb.PickleProperty()
    natomi = ndb.PickleProperty()
    kani = ndb.PickleProperty()
    vec = ndb.PickleProperty()
    ival = ndb.PickleProperty()
    katren = ndb.PickleProperty()
    azzi = ndb.PickleProperty()
    rakatin = ndb.PickleProperty()
    polly = ndb.PickleProperty()
    huanya = ndb.PickleProperty()
    jatt = ndb.PickleProperty()
    assistant = ndb.PickleProperty()
    tinkerclaw = ndb.PickleProperty()
    cheap = ndb.PickleProperty()
    last = ndb.DateTimeProperty(auto_now=True)


class Provisioners(webapp2.RequestHandler):
    def get(self):
        fpp = None
        try:
            fpp = FP_Prices.query(FP_Prices.fid == 1).fetch()[0]
        except:
            self.response.write("Could not get prices.")
            return
        weaponsmith = pickle.loads(fpp.weaponsmith)
        huntsman = pickle.loads(fpp.huntsman)
        artificer = pickle.loads(fpp.artificer)
        armorsmith = pickle.loads(fpp.armorsmith)
        leatherworker = pickle.loads(fpp.leatherworker)
        tailor = pickle.loads(fpp.tailor)
        natomi = pickle.loads(fpp.natomi) 
        kani = pickle.loads(fpp.kani)
        vec = pickle.loads(fpp.vec)
        ival = pickle.loads(fpp.ival)
        katren = pickle.loads(fpp.katren)
        azzi = pickle.loads(fpp.azzi)
        rakatin = pickle.loads(fpp.rakatin)
        polly = pickle.loads(fpp.polly)
        huanya = pickle.loads(fpp.huanya)
        jatt = pickle.loads(fpp.jatt)
        assistant = pickle.loads(fpp.assistant)
        tinkerclaw = pickle.loads(fpp.tinkerclaw)
        cheap = pickle.loads(fpp.cheap)
        last = fpp.last.replace(microsecond=0)
        template_values = {
            'prov': [["Quartermaster Natomi [&BN4HAAA=]",natomi],["Supplymaster Kani [&BOAHAAA=]",kani],["Quartermaster Vec [&BAgIAAA=]",vec],
                     ["Quartermaster Ival [&BNUHAAA=]",ival],["Steward Katren [&BO8HAAA=]",katren],["Supplymaster Azzi [&BN0HAAA=]",azzi],
                     ["Scavenger Rakatin [&BAYIAAA=]",rakatin],["Forager Polly [&BAIIAAA=]",polly],["Supplier Huanya [&BAwIAAA=]",huanya],
                     ["Jatt [&BAMIAAA=]",jatt],["Supply Assistant [&BMwHAAA=]",assistant],["Terrill Tinkerclaw [&BAAIAAA=]",tinkerclaw]],
            'craft':[['Weaponsmith',weaponsmith],['Huntsman',huntsman],['Artificer',artificer],
                     ['Armorsmith',armorsmith],['Leatherworker',leatherworker],['Tailor',tailor]],
            'cheap': cheap,
            'last': last
        }
        template = JINJA_ENVIRONMENT.get_template('templates/prov.html')
        self.response.write(template.render(template_values))

class Redirect(webapp2.RequestHandler):
    def get(self):
        self.redirect('/faction-provisioner')

application = webapp2.WSGIApplication([
    ('/faction-provisioner/', Redirect),
    ('/faction-provisioner', Provisioners),
], debug=True)
