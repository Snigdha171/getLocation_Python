# getLocation_Python
This repository contains all the files needed to run a python script and get the places marked on google map

Description -  The program takes input from the user and displays the marked location on Google map in the front end. This is an interactive program and the user can enter as many locations as he/she likes and view them on the map along with a tabular data sheet displaying the latitude and longitude of the places.

There are 2 scripts required to run this module :

1. getLocationonMap.py - Invoke this script in the command prompt and follow the instruction. This is based on python 3.5.2 version. It creates an intermediate file named - Location.js in the same folder where this python script is run. This file will then be used by lcation.html to give the desired result.

2. location.html - Place this file in the same folder where getLocationonMap.py is present and open it with google chrome. You can see a table with the names of the place that were given as input and their latitude and longitude. Along with this, you will also see the places marked on Google Map on the same page.

Please note, Location.js is a sample file that is created on running getLocationonMap.py and sampleOutput.jpg shows the sample data which appears on the screen after running location.html

