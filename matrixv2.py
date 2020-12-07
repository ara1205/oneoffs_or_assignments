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

def main():
    data = datainput()
    print(data)

main()
