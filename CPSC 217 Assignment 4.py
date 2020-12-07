#Andrew Alexandru
#Student ID: 30065419
#A program that sorts data based on different tasks


from collections import Counter
import sys
sys.argv = ["Asn4.py", "AnotherFoodWeb.txt"]

#Creates a dictonary from a txt file input
#Inputs: None
#Outputs: dictonary with lists:	{a:[1,2,3],b:[4,5,6]}
def CreateDict():
	try:
		foodweb = open(input("Enter filename: "))
	except:
		print("File(s) not found/accepted :(")
			
	foodwebbyline = foodweb.read().split("\n")
	while "" in foodwebbyline:
		foodwebbyline.remove("")
	pred = []
	prey = []
	for i in range(0,len(foodwebbyline)):
		currentline = foodwebbyline[i]
		currentline = currentline.split(",")
		pred.append(currentline[0])
		del currentline[0]
		prey.append(currentline)
	foodwebdict = dict(zip(pred,prey))

	return(foodwebdict)

#Creates 3 lists that are used in other fuctions
#Inputs: dictonary outputed by CreateDict() function
#Outputs: list of keys, values(with dups) from inputed dictonary 
#		  and a list of all elements from the inputed txt file(with dups)
def Triplelist(fooddict):
	preylist = []
	for x in fooddict:
		preylist = fooddict[x] + preylist

	predlist = []
	for x in fooddict:
		predlist.append(str(x))

	alllist = predlist + preylist
	
	return(predlist,preylist,alllist)

#Prints a dictonary with correct formating
#Inputs: dictonary outputed by CreateDict() function
#Outputs: None
def PrintDict(fooddict):
	print("Predators and Prey:")
	for i in fooddict:
		print("	", i, "eats",formatList(fooddict[i]))

#Prints a list keys from dictonary that that are not found also as values
#Inputs: dictonary outputed by CreateDict() function
#Outputs: None
def ApexPred(fooddict):
	predlist,preylist,alllist = Triplelist(fooddict)
	apexlist = []
	for i in predlist:
		if str(i) not in preylist:
			apexlist.append(i)
	print("Apex Predators:")
	print("	", formatList(apexlist))

#Prints a list of values from a dictonary that are not found also as keys
#Inputs: dictonary outputed by CreateDict() function
#Outputs: None
def Producer(fooddict):
	predlist,preylist,alllist = Triplelist(fooddict)
	producerlist = list(set(alllist) - set(predlist))
	print("Producers:")
	print("	", formatList(producerlist))

#Prints list of keys from a dictonary that have the longest list
#Inputs: dictonary outputed by CreateDict() function
#Output: None
def Flexiable(fooddict):
	record = 0
	flexlist = []
	for x in fooddict:
		if len(fooddict[x]) > record:
			record = len(fooddict[x])
			flexlist.clear()
			flexlist.append(str(x))
		elif len(fooddict[x]) == record:
			flexlist.append(str(x))
	print("Most Flexible Eaters:")
	print("	", formatList(flexlist))

#Prints list of the most common values found in a dictonary
#Inputs: dictonary outputed by CreateDict() function
#Outputs: None
def Tastiest(fooddict):
	predlist,preylist,alllist = Triplelist(fooddict)
	counterlist = Counter(preylist)
	record = 0
	tastylist = []
	for x in counterlist:
		if int(counterlist[x]) > record:
			record = int(counterlist[x])
			tastylist.clear()
			tastylist.append(str(x))
		elif int(counterlist[x]) == record:
			tastylist.append(str(x))
	print("Most Tasty Organism:")
	print("	", formatList(tastylist))

#Prints list of keys with the longest chained value relashionship
#Inputs: dictonary outputed by CreateDict() function
#Outputs: a dictonary with keys and their values: {a:1,b:2}
def Hights(fooddict):
	predlist,preylist,alllist = Triplelist(fooddict)
	producerlist = (list(set(alllist) - set(predlist)))
	for x in producerlist:
		fooddict[str(x)] = []
	predlist = predlist + producerlist
	heights = dict.fromkeys(predlist, 0)

	changed = True
	while changed == True:
		changed = False
		for i in predlist:
			for x in fooddict[i]:
				if heights[i] <= heights[x]:
					heights[i] = heights[x] + 1
					changed = True

	print("Heights:")
	for x, y in heights.items():
		print("	",x, ":", y)

	return(heights)

#Sorts and prints keys from a diconary based on what their chained values relashionship are
#Inputs: dictonary outputed by CreateDict() function and a 
#		 of chained vlaues relashionships from the Heights()
#Outputs: None
def Aplus(fooddict,heights):
	predlist,preylist,alllist = Triplelist(fooddict)
	herb = []
	omni = []
	carn = []
	for i in predlist:
		SUM = 0
		PRODUCT = 1
		for x in fooddict[i]:
			SUM = SUM + heights[x]
			PRODUCT = PRODUCT * heights[x]

		if SUM == 0 and PRODUCT == 0:
			herb.append(str(i))
		elif SUM != 0 and PRODUCT == 0:
			omni.append(str(i))
		elif SUM != 0 and PRODUCT != 0:
			carn.append(str(i))
	print("For an A+:")
	print("	Herbivores: ", formatList(herb))
	print("	Omnivores: ", formatList(omni))
	print("	Carnivores: ", formatList(carn))


def main():
	webdict = CreateDict()
	PrintDict(webdict)
	ApexPred(webdict)
	Producer(webdict)
	Flexiable(webdict)
	Tastiest(webdict)
	heights = Hights(webdict)
	Aplus(webdict,heights)

main()

input()
