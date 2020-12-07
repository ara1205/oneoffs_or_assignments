def datainput():
    datafile = open(input("Enter filename: "))
    print("Rows assumed to be seperated by newline and values by comma")
    dataRows = datafile.read().split("\n")
    datafile.close()
    data = []

    for row in dataRows:
        data.append(row.split(","))

    for row in data:
        for element in row[:]:
            if element == "":
                row.remove(element)
                

    return(data)

def sumRow(teamIndex, dataset):

    summedrow = []
    
    for row in dataset:
            if row[teamIndex] == 1:
                index = 0
                for element in row:
                    summedrow[index] = summedrow[index] + element

    return(summedrow)
                
            

def main():
    data = datainput()
    summed = sumRow(0,data)
    print(summed)

main()
