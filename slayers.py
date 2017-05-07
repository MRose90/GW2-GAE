import webapp2
import jinja2
import json
import datetime
import os
import sys
from google.appengine.api import urlfetch
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

mithril_id = 19700
elder_id = 19722
venom_id = 24282
scale_id = 24288
totem_id =24299
blood_id = 24294
claw_id = 24350
bone_id = 24341
fang_id = 24356
carrion_id = 15465
cleric_id = 15466
berserker_id = 15468
rampager_id = 15469
knight_id = 15470
valkyrie_id = 15471
assassin_id = 46333

mithril_price = 0
elder_price = 0
t5_id = 0
t5_price = sys.maxsize
slayer_price = sys.maxsize
#GW2 launch date
last_update = datetime.datetime.strptime('25 Aug 2012', '%d %b %Y').replace(hour=0, minute=0)

def Update():
    if (datetime.datetime.now()-last_update).total_seconds() > 60:
        api_url = 'https://api.guildwars2.com/v2/commerce/prices?ids='
        api_url += str(mithril_id) + ',' +  str(elder_id)
        api_url += ',' + str(venom_id) + ',' + str(scale_id) + ',' + str(totem_id) + ',' + str(blood_id) + ',' + str(claw_id) + ',' + str(bone_id) + ',' + str(fang_id)
        api_url += ',' + str(carrion_id) + ',' + str(cleric_id) + ',' + str(berserker_id) + ',' + str(rampager_id) + ',' + str(knight_id) + ',' + str(valkyrie_id) + ',' + str(assassin_id)
        result = urlfetch.fetch(url = api_url)
        data = json.loads(result.content)
        t5s = [venom_id,scale_id,totem_id,blood_id,claw_id,bone_id,fang_id]
        slayers = [carrion_id,cleric_id, berserker_id,rampager_id,knight_id,valkyrie_id,assassin_id]
        global t5_price
        global t5_id
        global slayer_price
        global mithril_price
        global elder_price
        slayer_price = sys.maxsize
        t5_price = sys.maxsize
        for d in data:
            if d['id'] == mithril_id:
                mithril_price = d['buys']['unit_price']
            if d['id'] == elder_id:
                elder_price = d['buys']['unit_price']
            if d['id'] in t5s:
                val = d['buys']['unit_price']
                if val < t5_price:
                    t5_id = d['id']
                    t5_price = val
            if d['id'] in slayers:
                val = d['sells']['unit_price']
                if val < slayer_price:
                    slayer_price = val


def Profits(custom=None):
    p = []
    base = mithril_price*24+elder_price*12+t5_price*15
    profit = int(slayer_price*.85-base)
    gold = int(profit/10000)
    silver = int((profit-gold*10000)/100)
    copper = profit-gold*10000-silver*100
    if gold > 0:
        silver = str(silver).zfill(2)   
    if gold > 0 or silver > 0:
        copper = str(copper).zfill(2)
    p.append([1,gold,silver,copper])
    if custom:
        try:
            custom = int(custom)
        except:
            custom = None
    if custom and int(custom) > 1 and int(custom) < 250:
        profit = int(float(slayer_price*.85-base)*int(custom))
        gold = int(profit/10000)
        silver = int((profit-gold*10000)/100)
        copper = profit-gold*10000-silver*100
        if gold > 0:
            silver = str(silver).zfill(2)
        if gold > 0 or silver > 0:
            copper = str(copper).zfill(2)
        profit = int((slayer_price*.85-base)*250)
        p.append([int(custom),gold,silver,copper])
        gold = int(profit/10000)
        silver = int((profit-gold*10000)/100)
        copper = profit-gold*10000-silver*100
        if gold > 0:
            silver = str(silver).zfill(2)
        if gold > 0 or silver > 0:
            copper = str(copper).zfill(2)
        p.append([250,gold,silver,copper])
    else:
        profit = int((slayer_price*.85-base)*250)
        gold = int(profit/10000)
        silver = int((profit-gold*10000)/100)
        copper = profit-gold*10000-silver*100
        if gold > 0:
            silver = str(silver).zfill(2)
        if gold > 0 or silver > 0:
            copper = str(copper).zfill(2)
        p.append([250,gold,silver,copper])
        if custom and int(custom) > 250:
            try:
                profit = int((slayer_price*.85-base)*custom)
                gold = int(profit/10000)
                silver = int((profit-gold*10000)/100)
                copper = profit-gold*10000-silver*100
                if gold > 0:
                    silver = str(silver).zfill(2)
                if gold > 0 or silver > 0:
                    copper = str(copper).zfill(2)
                profit = int((slayer_price*.85-base)*250)
                p.append([int(custom),gold,silver,copper])
            except:
                pass
    return p
class MainPage(webapp2.RequestHandler):
    def get(self):
        Update()
        custom_val = self.request.get('custom')
        gold = int(slayer_price/10000)
        silver = int((slayer_price-gold*10000)/100)
        copper = slayer_price-gold*10000-silver*100
        if gold > 0:
            silver = str(silver).zfill(2)
        if gold > 0 or silver > 0:
            copper = str(copper).zfill(2)
        s_price = [gold,silver,copper]
        t5 = ''
        if t5_id == venom_id:
            t5 = 'Potent Venom Sac'
        if t5_id == scale_id:
            t5 = 'Large Scale'
        if t5_id == totem_id:
            t5 = 'Intricate Totem'
        if t5_id == blood_id:
            t5 = 'Vial of Potent Blood'
        if t5_id == claw_id:
            t5 = 'Large Claw'
        if t5_id == bone_id:
            t5 = 'Large Bone'
        if t5_id == fang_id:
            t5 = 'Large Fang'
        template_values = {
            'mithril_price': mithril_price,
            'elder_price': elder_price,
            't5_name': t5,
            't5_price': t5_price,
            'slayer_price': s_price,
            'profits': Profits(custom_val),
        }
        template = JINJA_ENVIRONMENT.get_template('slayers.html')
        self.response.write(template.render(template_values))
        
application = webapp2.WSGIApplication([
    ('/krait', MainPage),
], debug=True)

