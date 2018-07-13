# SimpleDemos.py
# A few classes to demo this project
import os
import serial
from portUtils import PortUtils;
CURRENTDIR = os.path.dirname(__file__)
BASEDIR = os.path.dirname(CURRENTDIR)

# Replaces part of a template with the data
class SimpleDisplayCore():
    def index(self):
        # Change this if using hardware serial
        port = PortUtils('/dev/ttyACM0', 9600)
        data = port.read()

        html = self.showDemoHTML(data)
        return html

    def showDemoHTML(self, data):
        # Split the data into the components we want
        split = data.split(":")
        irtemp = split[0]
        ambtemp = split[1]
        
        # Read the template file and replace some values
	    html = ''
	    with open(CURRENTDIR + '/output_template.html') as template:
		    html = template.read()
        	html = html.replace("%IRTEMP%", irtemp)
        	html = html.replace("%AMBTEMP%", ambtemp)
        return html

# Returns data in JSON format
class JSONDemoCore():
    def get(self):
        # Change this if using hardware serial
        port = PortUtils('/dev/ttyACM0', 9600)
        data = port.read()

        # Split the data and extract what I want
        # In this example
        split = data.split(":")
        irtemp = split[0]
        ambtemp = split[1]

        # Return our JSON
        # Is there a library to do this - yes
        # Is it necessary for this demo - no
        json = "{\"irtemp\":\"" + irtemp + "\",\"ambtemp\": \"" + ambtemp + "\"}"
        return json

if __name__ == "__main__":
    print "Not how this works - read the docs"
