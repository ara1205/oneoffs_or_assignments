#Andrew Alexandru
#Student Number: 30065419
#Program will draw a happy face centered around the inputed coordinates

from SimpleGraphics import *

#Inputs
x = float(input("X Coordinate: "))
y = float(input("Y Coordinate: "))

#Outside window error
if (x>950 or x<-150) or (y>750 or y<-150):
	print("You will not be able to see face, try picking more centered values")

#Head
setFill("yellow")
ellipse(x-150,y-150,300,300)

#Square Eye
setFill("purple4")
rect(x-75,y-50,35,35)

#Triangle Eye
setFill("firebrick1")
polygon(x+60,y-50,x+95,y-50,x+78,y-15)

#Mouth
setFill("hot pink")
blob(x,y+50,x+25,y+57,x+5,y+70,x-10,y+65,x-25,y+60,x-5,y+55)