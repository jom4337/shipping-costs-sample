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


#------------Home DETAIL----------------------#
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
address= {'ie4d':'676 Santa Rosa Boulevard, unit 4 D.  Fort Walton Beach Fl 32548. Guests can receive packages only. Please go to front desk to retrieve.',           
          'ie2a':'676 Santa Rosa Boulevard, unit 4 D.  Fort Walton Beach Fl 32548. Guests can receive packages only. Please go to front desk to retrieve.'}
host= {'ie4d':'The Host for this home is Irina',           
       'ie2a':'The Host for this home is Irina'}
hostreach= {'ie4d':'You can reach your Host at 850-253-7008',           
            'ie2a':'You can reach your Host at 850-253-7008'}
#------------Home DETAIL----------------------#
#------------Home Ameneties Detail----------------------#
homeament1 =     {'ie4d':'Wifi', 
                      'ie2a':'' }
homeament2 =     {'ie4d':'HBO', 
                      'ie2a':'' }
homeament3 =     {'ie4d':'Beach Chairs', 
                      'ie2a':'' }
homeament4 =     {'ie4d':'Beach Toys', 
                      'ie2a':'Island Echo 2 A' }
homeament5 =     {'ie4d':'', 
                      'ie2a':'Island Echo 2 A' }
#------------Home Ameneties Detail----------------------#
#------------Home Ameneties more Detail----------------------#
morehomeament =     {'ie4d-wifi':'Availble in the unit and throughout the building', 
                     'ie4d-hbo':'Avaialble in both the licing room and the bedroom', 
                     'ie4d-chairs':'Beach Chairs & Umbrella are stored on the balcony  They are there for all Guests to use', 
                     'ie4d-toys':'Stored on the balcony in a plastic bin  They are there for all Guests to use',
                     'ie2a-toys':'Stored on the balcony '
                     }
#------------Home Ameneties more Detail----------------------#    

def makeWebhookResult(req):
    
    
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
#------------------action-------------------------------#
    if req.get("result").get("action") == "unit-name":
        speech="Welcome" 
        
#----------------acion unit.name------------------------#              
    if req.get("result").get("action") == "unit.name":
        
        result = req.get("result")
        parameters = result.get("parameters")
        zone = parameters.get("unit-name")
        
        
        speech="Welcome to "+unit+" ."+"  I am Leelu, how can I help.  For example. say - wifi, or contact host, or address, or checkout"
        
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
    
    #speech="Welcome to "+unit+" ."+"  I am Leelu, how can I help.  For example. say - wifi, or contact host, or address, or checkout"

        
    print("Response:")
    print(speech)
    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
