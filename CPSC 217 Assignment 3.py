#
#  Starting Code for CPSC 217 Assignment 3 (Fall 2018)
#
# Andrew Alexandru
# Student ID: 30065419

from SimpleGraphics import *
import statistics

# Part 1
#Takes no perm
#Outputs list of images and number of images said to be uploaded in the string (to avoid using global variable)
#Resizes window to 2 times the length and the same height as the original image

#Noticed a BUG!!!!!!!!!!!
#The resize fuction in simple graphics cant resize a window larger if it goes past the screen which the program is running
#Tested by hardcoding the width of the window to be 1174 (with the sc string of images) and pixels and the window
#would not reach said width, tried again with 1920 pixels in general and windows would not reach that width

def loadImages():
	images = []
	abriv = input("Enter abbreviation: ")
	ext = input("Enter Picture extension(without the dot): ")
	numimage = int(input("Enter number of images: "))
	

	if not 3 <= numimage <= 16:
		print("Can only process min of 3 and max of 16 images")
		input()
		close()
		quit()

	for imgnum in range(1,numimage + 1):
		images.append(loadImage(str(abriv) + "_" + str(imgnum) + "." + ext))

	resize(2 * getWidth(images[1]),getHeight(images[1]))

	return(images, numimage)


# Part 2:
#Takes a single image
#Outputs a single image that is 1/4 as big to be used as thumbnail
def createThumbnail(currentimage):
	w = getWidth(currentimage)
	wthumb = int(w / 4)
	h = getHeight(currentimage)
	hthumb = int(h / 4)
	imgthumb = createImage(wthumb, hthumb)
	for currentpixelx in range(0, w, 4):
		for currentpixely in range(0, h, 4):
			currentpixelrgb = getPixel(currentimage, currentpixelx, currentpixely)
			putPixel(imgthumb, int(currentpixelx / 4), int(currentpixely / 4), currentpixelrgb[0], currentpixelrgb[1], currentpixelrgb[2])

	return(imgthumb)

#Takes a string of images and number of images (to avoid global variable)
#Returns nothing but does draw the string of images uploaded as 1/4 of their size in a 4x4 grid on the left side of the window
def drawThumbnails(images,number_of_images):
	x = 0
	for currentimagenum in range(0, number_of_images):
		currentimage = createThumbnail(images[currentimagenum])
		if currentimagenum <= 3:
			y = 0
			x = currentimagenum * getWidth(currentimage)
		elif currentimagenum <=7:
			y = getHeight(currentimage)
			x = (currentimagenum * getWidth(currentimage)) - (getWidth(currentimage) * 4)
		elif currentimagenum <= 11:
			y = getHeight(currentimage) * 2
			x = (currentimagenum * getWidth(currentimage)) - (getWidth(currentimage) * 8)
		elif currentimagenum <= 15:
			y = getHeight(currentimage) * 3
			x = (currentimagenum * getWidth(currentimage)) - (getWidth(currentimage) * 12)
		drawImage(currentimage, x, y)
		update()

# Part 3:
#Takes a string of numbers
#Returns the median of that string of numbers
def median(rgbstr):
	median = statistics.median(rgbstr)
	return(median)
#Takes a string of images and number of images (to avoid global variable)
#Returns nothing but draws an image with the median pixel rgb values of inserted string of images effectivly moving out
#the tourists found in the photo
#Small note: works best with the washington monument series of images
def removeTourists(images,number_of_images):
	w = getWidth(images[1])
	h = getHeight(images[1])
	notouristimg = createImage(w, h)
	drawImage(notouristimg, w, 0)

	for currentpixelx in range(0, w):
		for currentpixely in range(0, h):
			currentpixelr = []
			currentpixelg = []
			currentpixelb = []
			for currentimagenum in range(0,number_of_images):
				currentpixelrgb = getPixel(images[currentimagenum],currentpixelx,currentpixely)
				currentpixelr.append(currentpixelrgb[0])
				currentpixelg.append(currentpixelrgb[1])
				currentpixelb.append(currentpixelrgb[2])
			currentpixelravg = median(currentpixelr)
			currentpixelgavg = median(currentpixelg)
			currentpixelbavg = median(currentpixelb)
			
			putPixel(notouristimg,currentpixelx,currentpixely,currentpixelravg,currentpixelgavg,currentpixelbavg)
		update()



# The main program loads the images, draws the thumbnails and then generates
# the tourist-free image
def main():
  images, numimage = loadImages()
  drawThumbnails(images,numimage)
  removeTourists(images,numimage)
main()
