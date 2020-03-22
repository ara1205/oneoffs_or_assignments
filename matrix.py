#Used to test of a element is a string or number
#Inputs: An element from array
#Outputs: True or False
def NumTest(value):
	try:
		float(value)
		return(True)
	except:
		return(False)

#Used to open,read and convert an file into an array of lists (list within lists)
#Inputs: None
#Outputs: List of lists with numbers string converted to numbers
def datainput():
	datafile = open(input("Enter filename: "))
	print("Rows assumed to be seperated by newline")
	dataseperator = input("Enter what seperates data (ie: comma, space,...): ")
	dataSTRINGS = datafile.read().split("\n")
	datafile.close()
	data = []

	for row in dataSTRINGS:
		data.append(list(map(str, row.split(dataseperator))))

	for row in data:
		for element in row:
			if NumTest(row[0]) == True:
				row.append(float(row[0]))
				row.pop(0)
			else:
				row.append(row[0])
				row.pop(0)
	print(data)
	return(data)

#Used to find a specific element within an array
#Inputs: An array
#Outputs: specific element
def FindData(data):
	rownum = int(input("Enter Row Number: ")) - 1
	elementnum = int(input("Enter Element Number: ")) - 1
	
	temprow = data[rownum]
	spec = temprow[elementnum]

	print(spec)
	return(spec)

#Used to take average of a specific element throughtout all rows and skips string elements
#Input: An array
#Output: float average number
def ElementAvg(data):
	elementnum = int(input("Enter Element Number: ")) - 1
	sum_ = 0
	count = 0

	for row in data:
		if NumTest(row[elementnum]) == True:
			sum_ = sum_ + row[elementnum]
			count = count + 1
	
	avg = sum_ / count
	
	print(avg)
	return(avg)

def ElementOp(data):
	print("You will be asked the following in order,E = aX_bY, where a and b are coefficients,")
	print("X and Y are element columes, _ is your choice of opperator (+,*,^)")
	a = float(input("a = "))
	X = int(input("X = "))
	opp = input("_ = ")
	b = float(input("b = "))
	Y = int(input("Y = "))
	answer = []
	

#Used has main 'hub' and menu to lead to other functions
#Inputs: None
#Ouputs: None
def main():
	Running = True
	data = datainput()
	while Running == True:
		print("Find Data = 1\nElementAvg = 2\nElementOpp = 3\nExit = 0 or blank")
		command = int(input("Enter Command: "))
		if command == 0 or "":
			Running = False
		elif command == 1:
			FindData(data)
		elif command == 2:
			ElementAvg(data)
		elif command == 3:
			ElementOp(data)
main()