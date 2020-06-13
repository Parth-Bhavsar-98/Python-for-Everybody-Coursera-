'''

#Calling a JSON API

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#API End Points

#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
#To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

#Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

#Test Data / Sample Execution

#You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJ0V94rPl_bIcRqLdrlbjFMDk".

#$ python3 solution.py
#Enter location: South Federal University
#Retrieving http://...
#Retrieved 2505 characters
#Place id ChIJ0V94rPl_bIcRqLdrlbjFMDk
#Turn In

#Please run your program to find the place_id for this location:

#University of Amsterdam

'''

import urllib.request as ur
import urllib.parse as up
import json

#Api
serviceurl = 'http://py4e-data.dr-chuck.net/json?key=42&'

#Input data
while True:
    address_input = input('Enter location: ')
    if len(address_input)<1: break
    params={"sensor": "false", "address": address_input}
    url = serviceurl + up.urlencode(params)
    #print("Retrieving", url)
    data=ur.urlopen(url).read().decode("utf-8")
    json_obj=json.loads(data)
    place_id=json_obj["results"][0]["place_id"]
    print(place_id)
