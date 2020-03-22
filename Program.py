import os
import re
import csv

directory = "C:\Gamma-20200322T070713Z-001\Gamma"

final = [["Filename","col1","col2"]]

for filename in os.listdir(directory)[1:]:

    print(filename);

    file = open(filename, 'r')

    #Scans when data starts
    filestart = 0
    currentlineindex = 1
    for line in file:
        if "~A" in line:
            filestart = currentlineindex
        currentlineindex = currentlineindex + 1

    #Opens data from start point
    file = open(filename, 'r')
    data = file.readlines()[filestart:]

    #Cleans Data
    cleandata = []
    for row in data:
        newrow = re.sub("\s\s+" , " ", row)
        newrow = newrow[1:]
        newrow = newrow.replace("\n","")
        newrow = newrow.replace(" ",",")
        cleandata.append(list(map(str, newrow.split(","))))

    #Prases data into floats
    parseddata = []
    for row in cleandata:
        temprow = []
        for element in row:
            temprow.append(float(element))
        parseddata.append(temprow)

    #Compares and avgs data
    finisheddata = [[0,0]]
    sumindex = 1
    for row in parseddata:
        if finisheddata[-1][0] != round(row[0]):
            finisheddata[-1][1] = finisheddata[-1][1] / sumindex
            sumindex = 1
            newrow = []
            newrow.append(round(row[0]))
            newrow.append(row[1])
            finisheddata.append(newrow)
        else:
            finisheddata[-1][1] = (finisheddata[-1][1] + row[1])
            sumindex = sumindex + 1
    finisheddata.pop(0)        

    #adds to finaldata
    for row in finisheddata:
        temp = []
        temp.append(filename.split("W")[0])
        temp.append(row[0])
        temp.append(row[1])
        final.append(temp)

#outputs data
dire ="C:\\Users\\Andrew\\Desktop\\Gamma-20200322T070713Z-001\Gamma\output"
with open(dire, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(final)
print("finished")
