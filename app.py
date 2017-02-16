#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


cost =     {'ie4d':'Island Echo 4 D', 'ie2a':'Island Echo 2 A' }
wifi =     {'ie4d':'Connect to any network that starts with IES4',
            'ie2a':'Connect to any network that starts with IES2'}
wifipass= {'ie4d':'8779121550',           'ie2a':'8779121550'}
#checkout= {'ie4d':'1',           'ie2a':'67890'}
#checkoutt= {'ie4d':'Checkout time for this home is 10:00 AM',
#            'ie2a':'Checkout time for this home is 10:00 AM'}
#address= {'ie4d':'676 Santa Rosa Boulevard, unit 4 D.  Fort walton Beach Fl 32548',           
#          'ie2a':'676 Santa Rosa Boulevard, unit 4 D.  Fort walton Beach Fl 32548'}
#host= {'ie4d':'The Host for this home is Irina',           'ie2a':'You can reach your at 850-253-7008'}
#hostreach= {'ie4d':'You can reach your at 850-253-7008',           'ie2a':'67890'}
#homeament= {'ie4d':'12345',           'ie2a':'67890'}
#resortament= {'ie4d':'12345',           'ie2a':'67890'}
#concierg= {'ie4d':'12345',           'ie2a':'67890'}
#services= {'ie4d':'12345',           'ie2a':'67890'}


#custname1
#custval1
#custname2
#custval2
#custname3
#custval3

    
def makeWebhookResult(req):
    if req.get("result").get("action") != "unit.name":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("unit-name")

    unit        =str(cost[zone])
    unitwifipass=str(wifipass[zone])
    unitwifi    =str(wifi[zone])
    
    speech="Welcome to "+unit+" ."
    
    
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "contextOut":[{"name":"unit-detail","lifespan":5,"parameters":{"name":unit,
                                                                       "wifi":unitwifi,
                                                                       "wifipass":unitwifipass
                                                                      }}],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
