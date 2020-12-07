#Andrew Alexandru
#Student number: 30065419
#A program to input and track power and location of hurricanes on a map

#Import Simple Graghics and Map.gif
from SimpleGraphics import *

img = loadImage("map.gif")

import sys
sys.stdin = open("andrew.txt")

#Drawmap

#Draw background
ximg = getWidth(img)
yimg = getHeight(img)
resize(ximg,yimg)

drawImage(img,0,0)

#Draw lines
setColor("azure3")

latmax = 95
latmin = 50
lonmax = 35
lonmin = 10
gridmulti = 5

#Latitude
latamu = (latmax - latmin) / gridmulti
latamupix = ximg / latamu

count = 0
offset = 0
while count < latamu :
	count = count + 1
	offset = offset + latamupix
	latcur = str(int(latmax - count * gridmulti)) + "W"
	line(offset,0,offset,yimg)
	text(offset + 20,10,latcur)

#Longitude
lonamu = (lonmax - lonmin) / gridmulti
lonamupix = yimg / lonamu

count = 0
offset = 0
while count < lonamu :
	count = count + 1
	offset = offset + lonamupix
	loncur = str(int(lonmax - count * gridmulti)) + "N"
	line(0,offset,ximg,offset)
	text(15,offset - 10,loncur)

#Inputing Data
	
#Starting variables
hc0 = 0
hcc0 = "Grey"
hdc0 = 5

hc1 = 74
hcc1 = "Green"
hdc1 = 7

hc2 = 96
hcc2 = "Yellow"
hdc2 = 9

hc3 = 111
hcc3 = "Orange"
hdc3 = 11

hc4 = 130
hcc4 = "Red"
hdc4 = 13

hc5 = 157
hcc5 = "Purple"
hdc5 = 15

#Other starting variables to make while loop work and the if firsttime statment to be true and the record system
hlo = 1
firsttime = 1
hc_RECORD = 0
hspd_RECORD = 0

#User Input
while hlo != 0:

	hlo = float(input("Enter Longitude: "))
	
	if hlo == 0:
		setColor("White")
	else:
		hla = float(input("Enter Latitude: ")) * (0 - 1)
		hspd = float(input("Enter Wind Speed: "))

		#Converting Lat and lon into pixel info with percentages
		hloP = (1-((hlo - lonmin) / (lonmax - lonmin))) * yimg
		hlaP = (1-((hla - latmin) / (latmax - latmin))) * ximg 

		#Picking the right color and diameter
		if hspd >= hc5:
			hcd = hdc5
			hcc = hcc5
			hc = 5
		elif hspd >= hc4:
			hcd = hdc4
			hcc = hcc4
			hc = 4
		elif hspd >= hc3:
			hcd = hdc3
			hcc = hcc3
			hc = 3
		elif hspd >= hc2:
			hcd = hdc2
			hcc = hcc2
			hc = 2
		elif hspd >= hc1:
			hcd = hdc1
			hcc = hcc1
			hc = 1
		elif hspd >= hc0:
			hcd = hdc0
			hcc = hcc0
			hc = 0

		hspdc = hcc

		#Line Color
		if firsttime == 0 and hspd_HISTORY > hspd:
			hcc = hspdc_HISTORY
		else:
			hcc = hspdc
		
		setColor(hcc)

		#Drawing Line
		if firsttime == 0:
			line(hlaP_HISTORY, hloP_HISTORY, hlaP, hloP)

		#History of point location and color, for lines
		hloP_HISTORY = hloP
		hlaP_HISTORY = hlaP
		
		hc_HISTORY = hc
		
		hspd_HISTORY = hspd
		hspdc_HISTORY = hspdc

		#Centering Dot
		hloP = hloP - (hcd / 2)
		hlaP = hlaP - (hcd / 2)

		#Drawing Point
		setColor(hspdc)
		ellipse(hlaP, hloP, hcd, hcd)

		#Deals with no history for the first dot, problem
		firsttime = 0

		#Records
		if hspd_RECORD <= hspd:
			hspd_RECORD = hspd
		
		if hc_RECORD <= hc:
			hc_RECORD = hc

	
	

#Printing Reocrds


hc_RECORD = "The max Category was: " + str(hc_RECORD)
text(ximg - 100, 25, hc_RECORD)

hspd_RECORD = "The max Wind Speed (mph) was: " + str(hspd_RECORD)
text(ximg - 130, 45, hspd_RECORD)

input()