###############################################################################
# Name : getLocationonMap.py
# Date : Sept 10, 2016
# Desc : Python script used to display the location on the map
# Author : Snigdha Prakash
################################################################################

#Before starting the program, displaying the details
print('''------------------------------------------------------------------
Created by Snigdha Prakash
Hello, Welcome to the world of Python
Python environment used here is Python 3.5.2
This module helps you to visualize the places mentioned by you on the map
Please pull 'location.html' script along with this script and place it in the same folder where getLocationonMap.py is present
You are now ready to start. Just follow the intructions.
----------------------------------------------------------------------------''')

#Importing the necessary libraries
import json
import urllib.request
import codecs
import os

#Defining the variables
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

#Delete Location.js file if it already exist
try:
    os.remove('Location.js')
    print('Location.js deleted successfully')
except OSError:
    pass
	
	
#Taking input from the user
def userInput():
    location = input('Please enter the name of the place you want to locate : ').strip()
    return location

#Getting JASON data for the input location
def getLocation():
    url = serviceurl + urllib.parse.urlencode({"sensor":"false", "address": location})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    try: 
        js = json.loads(data.decode("utf-8"))
    except: 
        print('Unable to find the location : ', location)
        exit(1)

#Displaying latitude and longitude after parsing the JASON data
    if not('status' in js and js['status'] == 'OK') : 
        print('Unable to find the location : ', location)
        print('Please enter the correct location and try again')
        exit(1)
    lat = js["results"][0]["geometry"]["location"]["lat"]
    long = js["results"][0]["geometry"]["location"]["lng"]
    where = js['results'][0]['formatted_address']
    where = where.replace("'","")
    output = "["+str(lat)+","+str(long)+", '"+where+"']"
    return output    


#Writing the output into the file
fileJS = codecs.open('Location.js','w', "utf-8")
fileJS.write("Location = [\n")


#Taking multiple input from the user
response = 'Y'
while(response == 'Y' or response == 'y'):
    location = userInput()
    output = getLocation()
    fileJS.write(output + ",\n")
    response = input('Do you want to enter more locations? Press Y to continue : ')

fileJS.write("\n];\n")
fileJS.close()