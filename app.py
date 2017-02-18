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


cost =     {'ie4d':'Island Echo 4 D', 
            'ie2a':'Island Echo 2 A' }
wifi =     {'ie4d':'Connect to any network that starts with IES4',
            'ie2a':'Connect to any network that starts with IES2'}
wifipass= {'ie4d':'8779121550',           
           'ie2a':'8779121550'}
checkout= {'ie4d':'Please, Leave dirty linens in front of bathroom sink. - Load and start dishwasher. - Empty trash cans. - Store sandfree beach chairs and toys on balcony. - Close and lock balcony door. - Turn lights off. - Make sure front door is securely latched upon exit. -  Please try to leave our place TIDY.  Thank you!  And have a safe trip home! ',           
           'ie2a':'10:00 AM'}
checkoutt= {'ie4d':'Checkout time for this home is 10:00 AM',
            'ie2a':'Checkout time for this home is 10:00 AM'}
address= {'ie4d':'676 Santa Rosa Boulevard, unit 4 D.  Fort walton Beach Fl 32548',           
          'ie2a':'676 Santa Rosa Boulevard, unit 4 D.  Fort walton Beach Fl 32548'}
host= {'ie4d':'The Host for this home is Irina',           
       'ie2a':'The Host for this home is Irina'}
hostreach= {'ie4d':'You can reach your Host at 850-253-7008',           
            'ie2a':'You can reach your Host at 850-253-7008'}
homeament= {'ie4d':'Sorry, Your host has not shared that information with me yet.',
            'ie2a':'Wifi, HBO, Beach Chairs & Umbrella, and Beach Toys.'}
resortament= {'ie4d':'Beachfront Pool, Outdoor Grills, DVD Rentals, Beach Rentals, Beach Volleyball, Fitness Center, Tennis Court, Free Onsite Parking',           
             'ie2a':'Sorry, Your host has not shared that information with me yet.'}
#concierg= {'ie4d':'12345',           'ie2a':'67890'}
#services= {'ie4d':'12345',           'ie2a':'67890'}


    
def makeWebhookResult(req):
    if req.get("result").get("action") == "shipping.cost":
        return {}
    
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("unit-name")

    unit        =str(cost[zone])
    unitwifi    =str(wifi[zone])
    unitwifipass=str(wifipass[zone])
    unitcheckout=str(checkout[zone])
    unitcheckoutt=str(checkoutt[zone])
    unitaddress=str(address[zone])
    unithost=str(host[zone])
    unithostreach=str(hostreach[zone])
    unithomeament=str(homeament[zone])
    unitresortament=str(resortament[zone])
    
    speech="Welcome to "+unit+" ."+"  I am Leelu, how can I help.  For example. say - wifi, or contact host, or address, or checkout"
    
    
    print("Response:")
    print(speech)
    

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "contextOut":[{"name":"unit-detail","lifespan":5,"parameters":{"name":unit,
                                                                       "wifi":unitwifi,
                                                                       "wifipass":unitwifipass,
                                                                       "checkout":unitcheckout,
                                                                       "checkoutt":unitcheckoutt,
                                                                       "address":unitaddress,
                                                                       "host":unithost,
                                                                       "hostreach":unithostreach,
                                                                       "homeament":unithomeament,
                                                                       "resortament":unitresortament
                                                                      }}],
        "source": "lodgekit-stay"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
