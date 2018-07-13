# Main application for python web server
# Has two demo features for showing data formats for data collected from
# arduino
#
# Project details at
# prototypingcorner.io/projects/arduino-and-pi-in-harmony
#
# MIT License
# Copyright (c) 2018 Prototyping Corner

from flask import Flask, request, make_response
application = Flask(__name__)

import traceback
import os
import sys
CURRENTDIR = os.path.dirname(os.path.abspath(__file__))
if CURRENTDIR not in sys.path:
    sys.path.insert(0, CURRENTDIR)

# Our demo classes in simpleDemos.py
from simpleDemos import SimpleDisplayCore, JSONDemoCore

def displayErrorHTML(error):
    # Formats an error in HTML for debugging on web page
    # DONT USE ON PRODUCTION SYSTEM - unless you have no regard for security
    err = "<p>PYTHON ERROR</p>"
    err += "<pre>" + error + "</pre>"
    return err

@application.errorhandler(500)
def internalServerError(error):
    err = "<p>ERROR! 500</p>"
    err += "<pre>"+ str(error) + "</pre>"
    err += "<pre>"+ str(traceback.format_exc()) + "</pre>"
    return err

# Renders a simple html page with the data
@application.route('/demo', methods=['GET'])
def simpleDemo():
    try:
        # The simple display core
        core = SimpleDisplayCore()
        htmlOut = core.index()

        # Output the HTML
        response = make_response(htmlOut)
        response.headers['Content-Type'] = 'text/html'
        return response
    except:
        # Woops something went wrong
        response = make_response(displayErrorHTML(traceback.format_exc()))
        response.headers['Content-Type'] = 'text/html'
        return response

# Provides the data in JSON format to do some better things with
@application.route('/api/data', methods=['GET'])
def jsonDemo():
    json = JSONDemoCore().get()
    response = make_response(json)
    response.headers['Content-Type'] = 'application/json'
    return response

# Run the app
if __name__ == "__main__":
    application.debug = True
    application.run()
