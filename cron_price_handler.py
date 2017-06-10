import webapp2
import json
import os
from google.appengine.api import urlfetch
import pickle
from google.appengine.ext import ndb

spool = 48

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
    


#mithril ore buy = 0, mithril ore sell = 1
#elder wood log buy = 2, sell = 3
#silk scrap buy = 4, sell = 5
#leather buy = 6, sell = 7
#large claw buy = 8, sell - 9
#assassin's krait machete buy = 10, sell = 11
#assassin's krait shooter buy = 12, sell = 13
#assassin's krait star buy = 14, sell = 15
#assassin's gladiator legplates buy = 16, sell = 17
#assassin's noble pants buy = 18, sell = 19
#assassin's masquerade leggings buy = 20, sell = 21
#large bone buy = 22, sell = 23
#carrion krait slayer buy = 24, sell = 25
#carrion krait short bow buy = 26, sell = 27
#carrion krait wand buy = 28, sell = 29
#carrion gladiator boots buy = 30, sell = 31
#carrion noble boots buy = 32, sell = 33
#carrion masquerade boots buy = 34, sell = 35
#large fang buy = 36, sell = 37
#valkyrie krait shell buy = 38, sell = 39
#valkyrie krait whelk buy =  40, sell = 41
#valkyrie krait crook buy = 42, sell = 43
#valkyrie gladiator chestplate buy = 44, sell = 45
#valkyrie noble coat buy = 46, sell = 47
#valkyrie masquerade raiments buy = 48, sell = 49
#karka shell buy = 50, sell = 51
#apothecary's krait ripper buy = 52, sell = 53
#apothecary's krait recurve bow buy = 54, sell = 55
#apothecary's krait crook buy = 56, sell = 57
#apothecary's gladiator pauldrons buy = 58, sell = 59
#apothecary's noble shoulders buy = 60, sell = 61
#apothecary's masquerade mantle buy = 62, sell = 63

#intricate totem buy = 64, sell = 65
#cleric's krait warhammer buy = 66, sell = 67
#cleric's krait handgun buy = 68, sell = 69
#cleric's krait star buy = 70, sell = 71
#cleric's gladiator gauntlets buy = 72, sell = 73
#cleric's noble gloves buy = 74, sell = 75
#cleric's masquerade gloves buy = 76, sell = 77

#pristine snowflake buy = 78, sells = 79
#giver's mithril mace buy = 80, sells = 81
#giver's krait recurve bow buy = 82, sells = 83
#giver's krait wand buy = 84, sells = 85
#giver's gladiator helm buy = 86, sells = 87
#giver's noble mask buy = 88, sells = 89
#giver's masquerade mask buy = 90, sells = 91

#intricate totem buy = 92, sell = 93
#rampager's krait battleaxe buy = 94, sell = 95
#rampager's krait shooter buy = 96, sell = 97
#rampager's krait wand buy = 98, sell = 99
#rampager's gladiator legplates buy = 100, sell = 101
#rampager's noble pants buy = 102, sell = 103
#rampager's masquerade leggings buy = 104, sell = 105

#valkyrie krait morning star buy = 106, sell = 107
#valkyrie krait brazier buy = 108, sell = 109

#large scale buy = 110, sell = 111
#knight's krait warhammer buy = 112, sell = 113
#knight's krait whelk buy = 114, sell = 115
#knight's krait crook buy = 116, sell = 117
#knight's gladiator boots buy = 118, sell = 119
#knight's noble boots buy = 120, sell = 121
#knight's masquerade boots buy = 122, sell = 123

#carrion krait battleaxe buy = 124, sell = 125
#carrion krait recurve bow buy = 126, sell = 127
#carrion krait star buy = 128, sell = 129
#carrion gladiator gauntlets buy = 130, sell = 131
#carrion noble gloves buy = 132, sell = 133
#carrion masquerade gloves buy = 134, sell = 135

#vial of potent blood buy = 136, sell = 137
#berserker's krait shell buy = 138, sell = 139
#berserker's krait brazier buy = 140, sell = 141
#berserker's krait star buy = 142, sell = 143
#berserker's gladiator pauldrons buy = 144, sell = 145
#berserker's noble shoulders buy = 146, sell = 147
#berserker's masquerade mantle buy = 148, sell = 149

#apothecary's krait shooter buy = 150, sell = 151
#apothecary's krait wand buy = 152, sell = 153
#apothecary's gladiator helm buy = 154, sell = 155
#apothecary's noble mask buy = 156 , sell = 157
#apothecary's masquerade mask  buy = 158, sell = 159

def updatePrices():
    #mithril ore = 19700, elder wood log = 19722
    #silk scrap = 19748,thick leather section = 19729
    ids = [19700,19722,19748,19729]
    #large claw = 24350, assassin's krait machete = 46281
    #assassin's krait shooter = 46186, assassin's krait star = 46040
    #assassin's gladiator legplates = 45622, assassin's noble pants = 45765
    #assassin's masquerade leggings = 45731
    ids.extend([24350,46281,46186,46040,45622,45765,45731])
    #large bone = 24341, carrion krait slayer = 15465
    #carrion krait short bow = 14469, carrion krait wand = 13924
    #carrion gladiator boots = 10702, carrion noble boots = 11876
    #carrion masquerade boots = 11121
    ids.extend([24341,15465,14469,13924,10702,11876,11121])
    #large fang = 24356, valkyrie krait shell = 15394
    #valkyrie krait whelk = 14517, valkyrie krait crook = 13895
    #valkyrie gladiator chestplate = 10722, valkyrie noble coat = 11798
    #valkyrie masquerade raiments = 11295
    ids.extend([24356,15394,14517,13895,10722,11798,11295])
    #karka shell = 37897, apothecary's krait ripper = 36779
    #apothecary's krait recurve bow = 36750, apothecary's krait crook = 36813
    #apothecary's gladiator pauldrons = 36746, apothecary's noble shoulders = 36891
    #apothecary's masquerade mantle = 36892
    ids.extend([37897,36779,36750,36813,36746,36891,36892])    
    #intricate totem = 24299,cleric's krait warhammer = 15508
    #cleric's krait handgun = 14596, cleric's krait star = 13974
    #cleric's gladiator gauntlets = 10710, cleric's noble gloves =11835
    #cleric's masquerade gloves =11248
    ids.extend([24299,15508,14596,13974,10710,11835,11248])
    #pristine snowflake = 38134, giver's mithril mace = 38336
    #giver's krait recurve bow = 38367, giver's krait wand = 38415
    #giver's gladiator helm = 38179, giver's noble mask = 38264
    #giver's masquerade mask = 38228
    ids.extend([38134,38336,38367,38415,38179,38264,38228])
    #intricate totem = 24299, rampager's krait battleaxe = 15427
    #rampager's krait shooter = 14648, rampager's krait wand = 13928
    #rampager's gladiator legplates = 10699, rampager's noble pants = 11754
    #rampager's masquerade leggings = 11167
    ids.extend([24299,15427,14648,13928,10699,11754,11167])
    #valkyrie krait morning star = 15352
    #valkyrie krait brazier = 14566
    ids.extend([15352,14566])
    #large scale = 24288, knight's krait warhammer = 15512
    #knight's krait whelk = 14516, knight's krait crook = 13894
    #knight's gladiator boots = 10707, knight's noble boots = 11881
    #knight's masquerade boots = 11126
    ids.extend([24288,15512,14516,13894,10707,11881,11126])
    #carrion krait battleaxe = 15423, carrion krait recurve bow = 14428
    #carrion krait star = 13973, carrion gladiator gauntlets = 10709
    #carrion noble gloves = 11834, carrion masquerade gloves = 11247
    ids.extend([15423,14428,13973,10709,11834,11247])
    #vial of potent blood = 24294, berserker's krait shell = 15391
    #berserker's krait brazier = 14563, berserker's krait star = 13976
    #berserker's gladiator pauldrons = 10691, berserker's noble shoulders = 11921
    #berserker's masquerade mantle = 11341
    ids.extend([24294,15391,14563,13976,10691,11921,11341])
    #apothecary's krait shooter = 36812, apothecary's krait wand = 36780
    #apothecary's gladiator helm = 36806, apothecary's noble mask = 36842
    #apothecary's masquerade mask = 36844
    ids.extend([36812,36780,36806,36842,36844])    
    api_url = 'https://api.guildwars2.com/v2/commerce/prices?ids='
    for val in ids:
        api_url += str(val)+','
    api_url = api_url[:-1]
    try:
        result = urlfetch.fetch(url = api_url)
        data = json.loads(result.content)
    except:
        return None
    prices = [0]*(160)
    for d in data:
        #mithril ore = 19700, elder wood log = 19722
        #silk scrap = 19748,thick leather section = 19729
        if d['id'] == 19700:
            prices[0] = d['buys']['unit_price']
            prices[1] = d['sells']['unit_price']
        if d['id'] == 19722:
            prices[2] = d['buys']['unit_price']
            prices[3] = d['sells']['unit_price']
        if d['id'] == 19748:
            prices[4] = d['buys']['unit_price']
            prices[5] = d['sells']['unit_price']
        if d['id'] == 19729:
            prices[6] = d['buys']['unit_price']
            prices[7] = d['sells']['unit_price']
        #large claw = 24350, assassin's krait machete = 46281
        #assassin's krait shooter = 46186, assassin's krait star = 46040
        #assassin's gladiator legplates = 45622, assassin's noble pants = 45765
        #assassin's masquerade leggings = 45731
        if d['id'] == 24350:
            prices[8] = d['buys']['unit_price']
            prices[9] = d['sells']['unit_price']
        if d['id'] == 46281:
            prices[10] = d['buys']['unit_price']
            prices[11] = d['sells']['unit_price']
        if d['id'] == 46186:
            prices[12] = d['buys']['unit_price']
            prices[13] = d['sells']['unit_price']
        if d['id'] == 46040:
            prices[14] = d['buys']['unit_price']
            prices[15] = d['sells']['unit_price']
        if d['id'] == 45622:
            prices[16] = d['buys']['unit_price']
            prices[17] = d['sells']['unit_price']
        if d['id'] == 45765:
            prices[18] = d['buys']['unit_price']
            prices[19] = d['sells']['unit_price']
        if d['id'] == 45731:
            prices[20] = d['buys']['unit_price']
            prices[21] = d['sells']['unit_price']
        #large bone = 24341, carrion krait slayer = 15465
        #carrion krait short bow = 14469, carrion krait wand = 13924
        #carrion gladiator boots = 10702, carrion noble boots = 11876
        #carrion masquerade boots = 11121
        if d['id'] == 24341:
            prices[22] = d['buys']['unit_price']
            prices[23] = d['sells']['unit_price']
        if d['id'] == 15465:
            prices[24] = d['buys']['unit_price']
            prices[25] = d['sells']['unit_price']
        if d['id'] == 14469:
            prices[26] = d['buys']['unit_price']
            prices[27] = d['sells']['unit_price']
        if d['id'] == 13924:
            prices[28] = d['buys']['unit_price']
            prices[29] = d['sells']['unit_price']
        if d['id'] == 10702:
            prices[30] = d['buys']['unit_price']
            prices[31] = d['sells']['unit_price']
        if d['id'] == 11876:
            prices[32] = d['buys']['unit_price']
            prices[33] = d['sells']['unit_price']
        if d['id'] == 11121:
            prices[34] = d['buys']['unit_price']
            prices[35] = d['sells']['unit_price']
        #large fang = 24356, valkyrie krait shell = 15394
        #valkyrie krait whelk = 14517, valkyrie krait crook = 13895
        #valkyrie gladiator chestplate = 10722, valkyrie noble coat = 11798
        #valkyrie masquerade raiments = 11295
        if d['id'] == 24356:
            prices[36] = d['buys']['unit_price']
            prices[37] = d['sells']['unit_price']
        if d['id'] == 15394:
            prices[38] = d['buys']['unit_price']
            prices[39] = d['sells']['unit_price']
        if d['id'] == 14517:
            prices[40] = d['buys']['unit_price']
            prices[41] = d['sells']['unit_price']
        if d['id'] == 13895:
            prices[42] = d['buys']['unit_price']
            prices[43] = d['sells']['unit_price']
        if d['id'] == 10722:
            prices[44] = d['buys']['unit_price']
            prices[45] = d['sells']['unit_price']
        if d['id'] == 11798:
            prices[46] = d['buys']['unit_price']
            prices[47] = d['sells']['unit_price']
        if d['id'] == 11295:
            prices[48] = d['buys']['unit_price']
            prices[49] = d['sells']['unit_price']
        #karka shell = 37897, apothecary's krait ripper = 36779
        #apothecary's krait recurve bow = 36750, apothecary's krait crook = 36813
        #apothecary's gladiator pauldrons = 36746, apothecary's noble shoulders = 36891
        #apothecary's masquerade mantle = 36892
        if d['id'] == 37897:
            prices[50] = d['buys']['unit_price']
            prices[51] = d['sells']['unit_price']
        if d['id'] == 36779:
            prices[52] = d['buys']['unit_price']
            prices[53] = d['sells']['unit_price']
        if d['id'] == 36750:
            prices[54] = d['buys']['unit_price']
            prices[55] = d['sells']['unit_price']
        if d['id'] == 36813:
            prices[56] = d['buys']['unit_price']
            prices[57] = d['sells']['unit_price']
        if d['id'] == 36746:
            prices[58] = d['buys']['unit_price']
            prices[59] = d['sells']['unit_price']
        if d['id'] == 36891:
            prices[60] = d['buys']['unit_price']
            prices[61] = d['sells']['unit_price']
        if d['id'] == 36892:
            prices[62] = d['buys']['unit_price']
            prices[63] = d['sells']['unit_price']      
        #intricate totem = 24299,cleric's krait warhammer = 15508
        #cleric's krait handgun = 14596, cleric's krait star = 13974
        #cleric's gladiator gauntlets = 10710, cleric's noble gloves =11835
        #cleric's masquerade gloves =11248
        if d['id'] == 24299:
            prices[64] = d['buys']['unit_price']
            prices[65] = d['sells']['unit_price']
        if d['id'] == 15508:
            prices[66] = d['buys']['unit_price']
            prices[67] = d['sells']['unit_price']
        if d['id'] == 14596:
            prices[68] = d['buys']['unit_price']
            prices[69] = d['sells']['unit_price']
        if d['id'] == 13974:
            prices[70] = d['buys']['unit_price']
            prices[71] = d['sells']['unit_price']
        if d['id'] == 10710:
            prices[72] = d['buys']['unit_price']
            prices[73] = d['sells']['unit_price']
        if d['id'] == 11835:
            prices[74] = d['buys']['unit_price']
            prices[75] = d['sells']['unit_price']
        if d['id'] == 11248:
            prices[76] = d['buys']['unit_price']
            prices[77] = d['sells']['unit_price']
        #pristine snowflake = 38134, giver's mithril mace = 38336
        #giver's krait recurve bow = 38367, giver's krait wand = 38415
        #giver's gladiator helm = 38179, giver's noble mask = 38264
        #giver's masquerade mask = 38228
        if d['id'] == 38134:
            prices[78] = d['buys']['unit_price']
            prices[79] = d['sells']['unit_price']
        if d['id'] == 38336:
            prices[80] = d['buys']['unit_price']
            prices[81] = d['sells']['unit_price']
        if d['id'] == 38367:
            prices[82] = d['buys']['unit_price']
            prices[83] = d['sells']['unit_price']
        if d['id'] == 38415:
            prices[84] = d['buys']['unit_price']
            prices[85] = d['sells']['unit_price']
        if d['id'] == 38179:
            prices[86] = d['buys']['unit_price']
            prices[87] = d['sells']['unit_price']
        if d['id'] == 38264:
            prices[88] = d['buys']['unit_price']
            prices[89] = d['sells']['unit_price']
        if d['id'] == 38228:
            prices[90] = d['buys']['unit_price']
            prices[91] = d['sells']['unit_price']
        #intricate totem = 24299, rampager's krait battleaxe = 15427
        #rampager's krait shooter = 14648, rampager's krait wand = 13928
        #rampager's gladiator legplates = 10699, rampager's noble pants = 11754
        #rampager's masquerade leggings = 11167
        if d['id'] == 24299:
            prices[92] = d['buys']['unit_price']
            prices[93] = d['sells']['unit_price']
        if d['id'] == 15427:
            prices[94] = d['buys']['unit_price']
            prices[95] = d['sells']['unit_price']
        if d['id'] == 14648:
            prices[96] = d['buys']['unit_price']
            prices[97] = d['sells']['unit_price']
        if d['id'] == 13928:
            prices[98] = d['buys']['unit_price']
            prices[99] = d['sells']['unit_price']
        if d['id'] == 10699:
            prices[100] = d['buys']['unit_price']
            prices[101] = d['sells']['unit_price']
        if d['id'] == 11754:
            prices[102] = d['buys']['unit_price']
            prices[103] = d['sells']['unit_price']
        if d['id'] == 11167:
            prices[104] = d['buys']['unit_price']
            prices[105] = d['sells']['unit_price']
        #valkyrie krait morning star = 15352
        #valkyrie krait brazier = 14566
        if d['id'] == 15352:
            prices[106] = d['buys']['unit_price']
            prices[107] = d['sells']['unit_price']
        if d['id'] == 14566:
            prices[108] = d['buys']['unit_price']
            prices[109] = d['sells']['unit_price']
        #large scale = 24288, knight's krait warhammer = 15512
        #knight's krait whelk = 14516, knight's krait crook = 13894
        #knight's gladiator boots = 10707, knight's noble boots = 11881
        #knight's masquerade boots = 11126
        if d['id'] == 24288:
            prices[110] = d['buys']['unit_price']
            prices[111] = d['sells']['unit_price']
        if d['id'] == 15512:
            prices[112] = d['buys']['unit_price']
            prices[113] = d['sells']['unit_price']
        if d['id'] == 14516:
            prices[114] = d['buys']['unit_price']
            prices[115] = d['sells']['unit_price']
        if d['id'] == 13894:
            prices[116] = d['buys']['unit_price']
            prices[117] = d['sells']['unit_price']
        if d['id'] == 10707:
            prices[118] = d['buys']['unit_price']
            prices[119] = d['sells']['unit_price']
        if d['id'] == 11881:
            prices[120] = d['buys']['unit_price']
            prices[121] = d['sells']['unit_price']
        if d['id'] == 11126:
            prices[122] = d['buys']['unit_price']
            prices[123] = d['sells']['unit_price']
        #carrion krait battleaxe = 15423, carrion krait recurve bow = 14428
        #carrion krait star = 13973, carrion gladiator gauntlets = 10709
        #carrion noble gloves = 11834, carrion masquerade gloves = 11247
        if d['id'] == 15423:
            prices[124] = d['buys']['unit_price']
            prices[125] = d['sells']['unit_price']
        if d['id'] == 14428:
            prices[126] = d['buys']['unit_price']
            prices[127] = d['sells']['unit_price']
        if d['id'] == 13973:
            prices[128] = d['buys']['unit_price']
            prices[129] = d['sells']['unit_price']
        if d['id'] == 10709:
            prices[130] = d['buys']['unit_price']
            prices[131] = d['sells']['unit_price']
        if d['id'] == 11834:
            prices[132] = d['buys']['unit_price']
            prices[133] = d['sells']['unit_price']
        if d['id'] == 11247:
            prices[134] = d['buys']['unit_price']
            prices[135] = d['sells']['unit_price']
        #vial of potent blood = 24294, berserker's krait shell = 15391
        #berserker's krait brazier = 14563, berserker's krait star = 13976
        #berserker's gladiator pauldrons = 10691, berserker's noble shoulders = 11921
        #berserker's masquerade mantle = 11341
        if d['id'] == 24294:
            prices[136] = d['buys']['unit_price']
            prices[137] = d['sells']['unit_price']
        if d['id'] == 15391:
            prices[138] = d['buys']['unit_price']
            prices[139] = d['sells']['unit_price']
        if d['id'] == 14563:
            prices[140] = d['buys']['unit_price']
            prices[141] = d['sells']['unit_price']
        if d['id'] == 13976:
            prices[142] = d['buys']['unit_price']
            prices[143] = d['sells']['unit_price']
        if d['id'] == 10691:
            prices[144] = d['buys']['unit_price']
            prices[145] = d['sells']['unit_price']
        if d['id'] == 11921:
            prices[146] = d['buys']['unit_price']
            prices[147] = d['sells']['unit_price']
        if d['id'] == 11341:
            prices[148] = d['buys']['unit_price']
            prices[149] = d['sells']['unit_price']
        #apothecary's krait shooter = 36812, apothecary's krait wand = 36780
        #apothecary's gladiator helm = 36806, apothecary's noble mask = 36842
        #apothecary's masquerade mask = 36844
        if d['id'] == 36812:
            prices[150] = d['buys']['unit_price']
            prices[151] = d['sells']['unit_price']
        if d['id'] == 36780:
            prices[152] = d['buys']['unit_price']
            prices[153] = d['sells']['unit_price']
        if d['id'] == 36806:
            prices[154] = d['buys']['unit_price']
            prices[155] = d['sells']['unit_price']
        if d['id'] == 36842:
            prices[156] = d['buys']['unit_price']
            prices[157] = d['sells']['unit_price']
        if d['id'] == 36844:
            prices[158] = d['buys']['unit_price']
            prices[159] = d['sells']['unit_price']
            return prices
        
def Total(array):
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for row in array:
        total1 += row[1]
        total2 += row[2]
        total3 += row[3]
        total4 += row[4]
    return total1,total2,total3,total4

def cheapest(array):
    c_buy = None
    c_sell = None
    buy = None
    sell = None    
    c_buy_r = None
    c_sell_r = None
    buy_r = None
    sell_r = None
    counter = 0
    for row in array:
        if c_buy == None:
            c_buy = row
            c_buy_r = counter
        elif c_buy[1] > row[1]:
            c_buy = row
            c_buy_r = counter
        if c_sell == None:
            c_sell = row
            c_sell_r = counter
        elif c_sell[2] > row[2]:
            c_sell = row
            c_sell_r = counter
        if buy == None:
            buy = row
            buy_r = counter
        elif buy[3] > row[3]:
            buy = row
            buy_r = counter
        if sell == None:
            sell = row
            sell_r = counter
        elif sell[4] > row[4]:
            sell = row
            sell_r = counter
    return c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r

def gsc(price):
    gold = int(price/10000)
    silver = int((price-gold*10000)/100)
    copper = price-gold*10000-silver*100
    if gold > 0:
        silver = str(silver).zfill(2)   
    if gold > 0 or silver > 0:
        copper = str(copper).zfill(2)
    return [gold,silver,copper]
 
def gscArr(arr):
    newArr = []
    for row in arr:
        newArr.append([row[0],gsc(row[1]),gsc(row[2]),gsc(row[3]),gsc(row[4])])
    return newArr

class Provisioners(webapp2.RequestHandler):
    def get(self):
        prices = updatePrices()
        if prices is None:
            return
        cheap = []
        weaponsmith = []
        huntsman = []
        artificer = []
        armorsmith = []
        leatherworker = []
        tailor = []
        natomi = []
        kani =[]
        vec = []
        ival = []
        katren = []
        azzi = []
        rakatin = []
        polly = []
        huanya = []
        jatt = []
        assistant = []
        tinkerclaw = []
        row = ["Assassin's Krait Machete",
               24*prices[0]+12*prices[2]+15*prices[8],
               24*prices[1]+12*prices[3]+15*prices[9],
               prices[10],
               prices[11]]
        natomi.append(row)
        weaponsmith.append(row)
        row = ["Assassin's Krait Shooter",
               18*prices[0]+21*prices[2]+15*prices[8],
               18*prices[1]+21*prices[3]+15*prices[9],
               prices[12],
               prices[13]]
        natomi.append(row)
        huntsman.append(row)
        row = ["Assassin's Krait Star",
               12*prices[0]+27*prices[2]+15*prices[8],
               12*prices[1]+27*prices[3]+15*prices[9],
               prices[14],
               prices[15]]
        natomi.append(row)
        artificer.append(row)
        row = ["Assassin's Gladiator Legplates",
               15*prices[4]+40*prices[6]+8*prices[0]+15*prices[8]+28*spool,
               15*prices[5]+40*prices[7]+8*prices[1]+15*prices[9]+28*spool,
               prices[16],
               prices[17]]
        natomi.append(row)
        armorsmith.append(row)
        row = ["Assassin's Noble Pants",
               15*prices[4]+56*prices[6]+15*prices[8]+28*spool,
               15*prices[5]+56*prices[7]+15*prices[9]+28*spool,
               prices[18],
               prices[19]]
        natomi.append(row)
        leatherworker.append(row)
        row = ["Assassin's Masquerade Leggings",
               27*prices[4]+40*prices[6]+15*prices[8]+28*spool,
               27*prices[5]+40*prices[7]+15*prices[9]+28*spool,
               prices[20],
               prices[21]]
        natomi.append(row)
        tailor.append(row)
        
        row = ["Carrion Krait Slayer",
                            24*prices[0]+12*prices[2]+15*prices[22],
                            24*prices[1]+12*prices[3]+15*prices[23],
                            prices[24],
                            prices[25]]
        kani.append(row)
        weaponsmith.append(row)
        row = ["Carrion Krait Short Bow",
                            12*prices[0]+24*prices[2]+12*prices[6]+15*prices[22],
                            12*prices[1]+24*prices[3]+12*prices[7]+15*prices[23],
                            prices[26],
                            prices[27]]
        kani.append(row)
        huntsman.append(row)
        row = ["Carrion Krait Wand",
                            12*prices[0]+27*prices[2]+15*prices[22],
                            12*prices[1]+27*prices[3]+15*prices[23],
                            prices[28],
                            prices[29]]
        kani.append(row)
        artificer.append(row)
        row = ["Carrion Gladiator Boots",
                            4*prices[0]+40*prices[6]+15*prices[4]+26*spool+15*prices[22],
                            4*prices[1]+40*prices[7]+15*prices[5]+26*spool+15*prices[23],
                            prices[30],
                            prices[31]]
        kani.append(row)
        armorsmith.append(row)
        row = ["Carrion Noble Boots",
                            56*prices[6]+12*prices[4]+26*spool+15*prices[22],
                            56*prices[7]+12*prices[5]+26*spool+15*prices[23],
                            prices[32],
                            prices[33]]
        kani.append(row)
        leatherworker.append(row)
        row = ["Carrion Masquarade Boots",
                            48*prices[6]+18*prices[4]+26*spool+15*prices[22],
                            48*prices[7]+18*prices[5]+26*spool+15*prices[23],
                            prices[34],
                            prices[35]]
        kani.append(row)
        tailor.append(row)
        
        row = ["Valkyrie Krait Shell",
                            20*prices[0]+12*prices[2]+15*prices[36],
                            20*prices[1]+12*prices[3]+15*prices[37],
                            prices[38],
                            prices[39]]
        vec.append(row)
        weaponsmith.append(row)
        row = ["Valkyrie Krait Whelk",
                            16*prices[0]+18*prices[2]+15*prices[36],
                            16*prices[1]+18*prices[3]+15*prices[37],
                            prices[40],
                            prices[41]]
        vec.append(row)
        huntsman.append(row)
        row = ["Valkyrie Krait Crook",
                            12*prices[0]+30*prices[2]+15*prices[36],
                            12*prices[1]+30*prices[3]+15*prices[37],
                            prices[42],
                            prices[43]]
        vec.append(row)
        artificer.append(row)
        row = ["Valkyrie Gladiator Chestplate",
                            10*prices[0]+40*prices[6]+15*prices[4]+28*spool+15*prices[36],
                            10*prices[1]+40*prices[7]+15*prices[5]+28*spool+15*prices[37],
                            prices[44],
                            prices[45]]
        vec.append(row)
        armorsmith.append(row)
        row = ["Valkyrie Noble Coat",
                            60*prices[6]+15*prices[4]+28*spool+15*prices[36],
                            60*prices[7]+15*prices[5]+28*spool+15*prices[37],
                            prices[46],
                            prices[47]]
        vec.append(row)
        leatherworker.append(row)
        row = ["Valkyrie Masquerade Raiments",
                            44*prices[6]+27*prices[4]+28*spool+15*prices[36],
                            44*prices[7]+27*prices[5]+28*spool+15*prices[37],
                            prices[48],
                            prices[49]]
        vec.append(row)
        tailor.append(row)  
        
        row = ["Apothecary's Krait Ripper",
                            22*prices[0]+12*prices[2]+20*prices[50],
                            22*prices[1]+12*prices[3]+20*prices[51],
                            prices[52],
                            prices[53]]
        ival.append(row)
        weaponsmith.append(row)
        row = ["Apothecary's Krait Recurve Bow",
                            12*prices[0]+24*prices[2]+12*prices[6]+20*prices[50],
                            12*prices[1]+24*prices[3]+12*prices[7]+20*prices[51],
                            prices[54],
                            prices[55]]
        ival.append(row)
        huntsman.append(row)
        row = ["Apothecary's Krait Crook",
                            12*prices[0]+30*prices[2]+20*prices[50],
                            12*prices[1]+30*prices[3]+20*prices[51],
                            prices[56],
                            prices[57]]
        ival.append(row)
        artificer.append(row)
        row = ["Apothecary's Gladiator Pauldrons",
                            4*prices[0]+40*prices[6]+15*prices[4]+26*spool+20*prices[50],
                            4*prices[1]+40*prices[7]+15*prices[5]+26*spool+20*prices[51],
                            prices[58],
                            prices[59]]
        ival.append(row)
        armorsmith.append(row)
        row = ["Apothecary's Noble Shoulders",
                            48*prices[6]+15*prices[4]+26*spool+20*prices[50],
                            48*prices[7]+15*prices[5]+26*spool+20*prices[51],
                            prices[60],
                            prices[61]]
        ival.append(row)
        leatherworker.append(row)
        row = ["Apothecary's Masquerade Mantle",
                            44*prices[6]+18*prices[4]+26*spool+20*prices[50],
                            44*prices[7]+18*prices[5]+26*spool+20*prices[51],
                            prices[62],
                            prices[63]]
        ival.append(row)
        tailor.append(row)
        
        row = ["Cleric's Krait Warhammer",
                            18*prices[0]+18*prices[2]+15*prices[64],
                            18*prices[1]+18*prices[3]+15*prices[65],
                            prices[66],
                            prices[67]]
        katren.append(row)
        weaponsmith.append(row)
        row = ["Cleric's Krait Handgun",
                            18*prices[0]+18*prices[2]+15*prices[64],
                            18*prices[1]+18*prices[3]+15*prices[65],
                            prices[68],
                            prices[69]]
        katren.append(row)
        huntsman.append(row)
        row = ["Cleric's Krait Star",
                            12*prices[0]+27*prices[2]+15*prices[64],
                            12*prices[1]+27*prices[3]+15*prices[65],
                            prices[70],
                            prices[71]]
        katren.append(row)
        artificer.append(row)
        row = ["Cleric's Gladiator Gauntlets",
                            4*prices[0]+40*prices[6]+15*prices[4]+26*spool+15*prices[64],
                            4*prices[1]+40*prices[7]+15*prices[5]+26*spool+15*prices[65],
                            prices[72],
                            prices[73]]
        katren.append(row)
        armorsmith.append(row)
        row = ["Cleric's Noble Gloves",
                            48*prices[6]+15*prices[4]+26*spool+15*prices[64],
                            48*prices[7]+15*prices[5]+26*spool+15*prices[65],
                            prices[74],
                            prices[75]]
        katren.append(row)
        leatherworker.append(row)
        row = ["Cleric's Masquerade Gloves",
                            44*prices[6]+18*prices[4]+26*spool+15*prices[64],
                            44*prices[7]+18*prices[5]+26*spool+15*prices[65],
                            prices[76],
                            prices[77]]
        katren.append(row)
        tailor.append(row)
        
        row = ["Giver's Mithril Mace",
                            18*prices[0]+18*prices[2]+15*prices[78],
                            18*prices[1]+18*prices[3]+15*prices[79],
                            prices[80],
                            prices[81]]
        azzi.append(row)
        weaponsmith.append(row)
        row = ["Giver's Krait Recurve Bow",
                            12*prices[0]+24*prices[2]+12*prices[6]+15*prices[78],
                            12*prices[1]+24*prices[3]+12*prices[7]+15*prices[79],
                            prices[82],
                            prices[83]]
        azzi.append(row)
        huntsman.append(row)
        row = ["Giver's Krait Wand",
                            12*prices[0]+27*prices[2]+15*prices[78],
                            12*prices[1]+27*prices[3]+15*prices[79],
                            prices[84],
                            prices[85]]
        azzi.append(row)
        artificer.append(row)
        row = ["Giver's Gladiator Helm",
                            4*prices[0]+40*prices[6]+18*prices[4]+26*spool+8*prices[78],
                            4*prices[1]+40*prices[7]+18*prices[5]+26*spool+8*prices[79],
                            prices[86],
                            prices[87]]
        azzi.append(row)
        armorsmith.append(row)
        row = ["Giver's Noble Mask",
                            44*prices[6]+18*prices[4]+26*spool+8*prices[78],
                            44*prices[7]+18*prices[5]+26*spool+8*prices[79],
                            prices[88],
                            prices[89]]
        azzi.append(row)
        leatherworker.append(row)
        row = ["Giver's Masquerade Mask",
                            44*prices[6]+18*prices[4]+26*spool+8*prices[78],
                            44*prices[7]+18*prices[5]+26*spool+8*prices[79],
                            prices[90],
                            prices[91]]
        azzi.append(row)
        tailor.append(row)

        row = ["Rampager's Krait Battleaxe",
                            18*prices[0]+18*prices[2]+15*prices[92],
                            18*prices[1]+18*prices[3]+15*prices[93],
                            prices[94],
                            prices[95]]
        rakatin.append(row)
        weaponsmith.append(row)
        row = ["Rampager's Krait Shooter",
                            18*prices[0]+21*prices[2]+15*prices[92],
                            18*prices[1]+21*prices[3]+15*prices[93],
                            prices[96],
                            prices[97]]
        rakatin.append(row)
        huntsman.append(row)
        row = ["Rampager's Krait Wand",
                            12*prices[0]+27*prices[2]+15*prices[92],
                            12*prices[1]+27*prices[3]+15*prices[93],
                            prices[98],
                            prices[99]]
        rakatin.append(row)
        artificer.append(row)
        row = ["Rampager's Gladiator Legplates",
                            8*prices[0]+40*prices[6]+15*prices[4]+28*spool+15*prices[92],
                            8*prices[1]+40*prices[7]+15*prices[5]+28*spool+15*prices[93],
                            prices[100],
                            prices[101]]
        rakatin.append(row)
        armorsmith.append(row)
        row = ["Rampager's Noble Pants",
                            56*prices[6]+15*prices[4]+28*spool+15*prices[92],
                            56*prices[7]+15*prices[5]+28*spool+15*prices[93],
                            prices[102],
                            prices[103]]
        rakatin.append(row)
        leatherworker.append(row)
        row = ["Rampager's Masquerade Leggings",
                            40*prices[6]+27*prices[4]+28*spool+15*prices[92],
                            40*prices[7]+27*prices[5]+28*spool+15*prices[93],
                            prices[104],
                            prices[105]]
        rakatin.append(row)
        tailor.append(row)    

        row = ["Valkyrie Krait Morning Star",
                            18*prices[0]+18*prices[2]+15*prices[36],
                            18*prices[1]+18*prices[3]+15*prices[37],
                            prices[106],
                            prices[107]]
        polly.append(row)
        weaponsmith.append(row)
        row = ["Valkyrie Krait Brazier",
                            16*prices[0]+18*prices[2]+15*prices[36],
                            16*prices[1]+18*prices[3]+15*prices[37],
                            prices[108],
                            prices[109]]
        polly.append(row)
        huntsman.append(row)
        row = ["Valkyrie Krait Crook",
                            12*prices[0]+30*prices[2]+15*prices[36],
                            12*prices[1]+30*prices[3]+15*prices[37],
                            prices[42],
                            prices[43]]
        polly.append(row)
        artificer.append(row)
        row = ["Valkyrie Gladiator Chestplate",
                            4*prices[0]+40*prices[6]+12*prices[4]+25*spool+15*prices[36],
                            4*prices[1]+40*prices[7]+12*prices[5]+25*spool+15*prices[37],
                            prices[44],
                            prices[45]]
        polly.append(row)
        armorsmith.append(row)
        row = ["Valkyrie Noble Coat",
                            40*prices[6]+12*prices[4]+25*spool+15*prices[36],
                            40*prices[7]+12*prices[5]+25*spool+15*prices[37],
                            prices[46],
                            prices[47]]
        polly.append(row)
        leatherworker.append(row)
        row = ["Valkyrie Masquerade Raiments",
                            40*prices[6]+12*prices[4]+25*spool+15*prices[36],
                            40*prices[7]+12*prices[5]+25*spool+15*prices[37],
                            prices[48],
                            prices[49]]
        polly.append(row)
        tailor.append(row)

        row = ["Knight's Krait Warhammer",
                            18*prices[0]+18*prices[2]+15*prices[110],
                            18*prices[1]+18*prices[3]+15*prices[111],
                            prices[112],
                            prices[113]]
        huanya.append(row)
        weaponsmith.append(row)
        row = ["Knight's Krait Whelk",
                            16*prices[0]+18*prices[2]+15*prices[110],
                            16*prices[1]+18*prices[3]+15*prices[111],
                            prices[114],
                            prices[115]]
        huanya.append(row)
        huntsman.append(row)
        row = ["Knight's Krait Crook",
                            12*prices[0]+30*prices[2]+15*prices[110],
                            12*prices[1]+30*prices[3]+15*prices[111],
                            prices[116],
                            prices[117]]
        huanya.append(row)
        artificer.append(row)
        row = ["Knight's Gladiator Boots",
                            4*prices[0]+40*prices[6]+15*prices[4]+26*spool+15*prices[110],
                            4*prices[1]+40*prices[7]+15*prices[5]+26*spool+15*prices[111],
                            prices[118],
                            prices[119]]
        huanya.append(row)
        armorsmith.append(row)
        row = ["Knight's Noble Boots",
                            56*prices[6]+12*prices[4]+26*spool+15*prices[110],
                            56*prices[7]+12*prices[5]+26*spool+15*prices[111],
                            prices[120],
                            prices[121]]
        huanya.append(row)
        leatherworker.append(row)
        row = ["Knight's Masquerade Boots",
                            48*prices[6]+18*prices[4]+26*spool+15*prices[110],
                            48*prices[7]+18*prices[5]+26*spool+15*prices[111],
                            prices[122],
                            prices[123]]
        huanya.append(row)
        tailor.append(row)    

        row = ["Carrion Krait Battleaxe",
                            18*prices[0]+18*prices[2]+15*prices[22],
                            18*prices[1]+18*prices[3]+15*prices[23],
                            prices[124],
                            prices[125]]
        jatt.append(row)
        weaponsmith.append(row)
        row = ["Carrion Krait Recurve Bow",
                            12*prices[0]+24*prices[2]+12*prices[6]+15*prices[22],
                            12*prices[1]+24*prices[3]+12*prices[7]+15*prices[23],
                            prices[126],
                            prices[127]]
        jatt.append(row)
        huntsman.append(row)
        row = ["Carrion Krait Star",
                            12*prices[0]+27*prices[2]+15*prices[22],
                            12*prices[1]+27*prices[3]+15*prices[23],
                            prices[128],
                            prices[129]]
        jatt.append(row)
        artificer.append(row)
        row = ["Carrion Gladiator Gauntlets",
                            4*prices[0]+40*prices[6]+15*prices[4]+26*spool+15*prices[22],
                            4*prices[1]+40*prices[7]+15*prices[5]+26*spool+15*prices[23],
                            prices[130],
                            prices[131]]
        jatt.append(row)
        armorsmith.append(row)
        row = ["Carrion Noble Gloves",
                            48*prices[6]+15*prices[4]+26*spool+15*prices[22],
                            48*prices[7]+15*prices[5]+26*spool+15*prices[23],
                            prices[132],
                            prices[133]]
        jatt.append(row)
        leatherworker.append(row)
        row = ["Carrion Masquerade Gloves",
                            44*prices[6]+18*prices[4]+26*spool+15*prices[22],
                            44*prices[7]+18*prices[5]+26*spool+15*prices[23],
                            prices[134],
                            prices[135]]
        jatt.append(row)
        tailor.append(row)

        row = ["Berserker's Krait Shell",
                            20*prices[0]+12*prices[2]+15*prices[136],
                            20*prices[1]+12*prices[3]+15*prices[137],
                            prices[138],
                            prices[139]]
        assistant.append(row)
        weaponsmith.append(row)
        row = ["Berserker's Krait Brazier",
                            16*prices[0]+18*prices[2]+15*prices[136],
                            16*prices[1]+18*prices[3]+15*prices[137],
                            prices[140],
                            prices[141]]
        assistant.append(row)
        huntsman.append(row)
        row = ["Berserker's Krait Star",
                            12*prices[0]+27*prices[2]+15*prices[136],
                            12*prices[1]+27*prices[3]+15*prices[137],
                            prices[142],
                            prices[143]]
        assistant.append(row)
        artificer.append(row)
        row = ["Berserker's Gladiator Pauldrons",
                            4*prices[0]+40*prices[6]+15*prices[4]+26*spool+15*prices[136],
                            4*prices[1]+40*prices[7]+15*prices[5]+26*spool+15*prices[137],
                            prices[144],
                            prices[145]]
        assistant.append(row)
        armorsmith.append(row)
        row = ["Berserker's Noble Shoulders",
                            48*prices[6]+15*prices[4]+26*spool+15*prices[136],
                            48*prices[7]+15*prices[5]+26*spool+15*prices[137],
                            prices[146],
                            prices[147]]
        assistant.append(row)
        leatherworker.append(row)
        row = ["Berserker's Masquerade Mantle",
                            44*prices[6]+18*prices[4]+26*spool+15*prices[136],
                            44*prices[7]+18*prices[5]+26*spool+15*prices[137],
                            prices[148],
                            prices[149]]
        assistant.append(row)
        tailor.append(row)    

        row = ["Apothecary's Krait Ripper",
                            22*prices[0]+12*prices[2]+20*prices[50],
                            22*prices[1]+12*prices[3]+20*prices[51],
                            prices[52],
                            prices[53]]
        tinkerclaw.append(row)
        weaponsmith.append(row)
        row = ["Apothecary's Krait Shooter",
                            18*prices[0]+21*prices[2]+20*prices[50],
                            18*prices[1]+21*prices[3]+20*prices[51],
                            prices[150],
                            prices[151]]
        tinkerclaw.append(row)
        huntsman.append(row)
        row = ["Apothecary's Krait Wand",
                            12*prices[0]+27*prices[2]+20*prices[50],
                            12*prices[1]+27*prices[3]+20*prices[51],
                            prices[152],
                            prices[153]]
        tinkerclaw.append(row)
        artificer.append(row)
        row = ["Apothecary's Gladiator Helm",
                            2*prices[0]+40*prices[6]+18*prices[4]+26*spool+20*prices[50],
                            2*prices[1]+40*prices[7]+18*prices[5]+26*spool+20*prices[51],
                            prices[154],
                            prices[155]]
        tinkerclaw.append(row)
        armorsmith.append(row)
        row = ["Apothecary's Noble Mask",
                            44*prices[6]+18*prices[4]+26*spool+20*prices[50],
                            44*prices[7]+18*prices[5]+26*spool+20*prices[51],
                            prices[156],
                            prices[157]]
        tinkerclaw.append(row)
        leatherworker.append(row)
        row = ["Apothecary's Masquerade Mask",
                            44*prices[6]+18*prices[4]+26*spool+20*prices[50],
                            44*prices[7]+18*prices[5]+26*spool+20*prices[51],
                            prices[158],
                            prices[159]]
        tinkerclaw.append(row)
        tailor.append(row)
        total_c_buy = 0
        total_c_sell = 0
        total_buy = 0
        total_sell = 0
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(natomi)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Quartermaster Natomi [&BN4HAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(kani)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Supplymaster Kani [&BOAHAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(vec)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Quartermaster Vec [&BAgIAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(ival)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Quartermaster Ival [&BNUHAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(katren)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Steward Katren [&BO8HAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_rl = cheapest(azzi)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Supplymaster Azzi [&BN0HAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(rakatin)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Scavenger Rakatin [&BAYIAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(polly)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Forager Polly [&BAIIAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(huanya)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Supplier Huanya [&BAwIAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(jatt)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Jatt [&BAMIAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(assistant)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Supply Assistant [&BMwHAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        c_buy,c_sell,buy,sell,c_buy_r,c_sell_r,buy_r,sell_r = cheapest(tinkerclaw)
        total_c_buy += c_buy[1]
        total_c_sell += c_sell[2]
        total_buy += buy[3]
        total_sell += sell[4]
        cheap.append(["Terrill Tinkerclaw [&BAAIAAA=]",[c_buy[0],gsc(c_buy[1]),c_buy_r],[c_sell[0],gsc(c_sell[2]),c_sell_r],[buy[0],gsc(buy[3]),buy_r],[sell[0],gsc(sell[4]),sell_r]])
        cheap.append(['Total',['',gsc(total_c_buy)],['',gsc(total_c_sell)],['',gsc(total_buy)],['',gsc(total_sell)]])
        t1,t2,t3,t4 = Total(weaponsmith)
        weaponsmith.append(["Total",t1,t2,t3,t4])
        t1,t2,t3,t4 = Total(huntsman)
        huntsman.append(["Total",t1,t2,t3,t4])
        t1,t2,t3,t4 = Total(artificer)
        artificer.append(["Total",t1,t2,t3,t4])
        t1,t2,t3,t4 = Total(armorsmith)
        armorsmith.append(["Total",t1,t2,t3,t4])
        t1,t2,t3,t4 = Total(leatherworker)
        leatherworker.append(["Total",t1,t2,t3,t4])
        t1,t2,t3,t4 = Total(tailor)
        tailor.append(["Total",t1,t2,t3,t4])

        weaponsmith = gscArr(weaponsmith)
        huntsman = gscArr(huntsman)
        artificer = gscArr(artificer)
        armorsmith = gscArr(armorsmith)
        leatherworker = gscArr(leatherworker)
        tailor = gscArr(tailor)
        natomi = gscArr(natomi)  
        kani = gscArr(kani)
        vec = gscArr(vec)
        ival = gscArr(ival)
        katren = gscArr(katren)
        azzi = gscArr(azzi)
        rakatin = gscArr(rakatin)
        polly = gscArr(polly)
        huanya = gscArr(huanya)
        jatt = gscArr(jatt)
        assistant = gscArr(assistant)
        tinkerclaw = gscArr(tinkerclaw)
        fpp = None
        try:
            fpp = FP_Prices.query(FP_Prices.fid == 1).fetch()[0]
        except:
            fpp = FP_Prices()
        fpp.fid = 1
        fpp.weaponsmith = pickle.dumps(weaponsmith)
        fpp.huntsman = pickle.dumps(huntsman)
        fpp.artificer = pickle.dumps(artificer)
        fpp.armorsmith = pickle.dumps(armorsmith)
        fpp.leatherworker = pickle.dumps(leatherworker)
        fpp.tailor = pickle.dumps(tailor)
        fpp.natomi = pickle.dumps(natomi)
        fpp.kani = pickle.dumps(kani)
        fpp.vec = pickle.dumps(vec)
        fpp.ival = pickle.dumps(ival)
        fpp.katren = pickle.dumps(katren)
        fpp.azzi = pickle.dumps(azzi)
        fpp.rakatin = pickle.dumps(rakatin)
        fpp.polly = pickle.dumps(polly)
        fpp.huanya = pickle.dumps(huanya)
        fpp.jatt = pickle.dumps(jatt)
        fpp.assistant = pickle.dumps(assistant)
        fpp.tinkerclaw = pickle.dumps(tinkerclaw)
        fpp.cheap = pickle.dumps(cheap)
        fpp.put()
        
application = webapp2.WSGIApplication([
    ('/cph', Provisioners),
], debug=True)

