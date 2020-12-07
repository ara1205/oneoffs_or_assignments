from datetime import datetime
from math import sin

x = datetime.now().timetuple().tm_yday

try:
    f = open("key.txt")
    key = f.readlines()
    f.close()
    key = int(key.pop(0))
except:
    key = int(input("Key File not found, enter key: "))

keyA = 0.5 * sin(key * 0.6127377825801646) + 0.5
keyR = 0.5 * sin(key * 0.5390392339608568) + 0.5
keyL = 0.5 * sin(key * 0.22282797894499617) + 0.5
keyH = 0.5 * sin(key * 0.07214116453226571) + 0.5

chA = round(10 * sin(keyA * x**5 + keyA * x**4 + keyA * x**3 + keyA * x**2 + keyA * x) + 11)
chR = round(10 * sin(keyR * x**5 + keyR * x**4 + keyR * x**3 + keyR * x**2 + keyR * x) + 11)
chL = round(10 * sin(keyL * x**5 + keyL * x**4 + keyL * x**3 + keyL * x**2 + keyL * x) + 11)
chH = round(10 * sin(keyH * x**5 + keyH * x**4 + keyH * x**3 + keyH * x**2 + keyH * x) + 11)

chlist = [chA,chR,chL,chH]

while True
    if len(chlist) != len(set(chlist)):
        dup = [x for x in chlist if chlist.count(x) >= 2]
        rest = [x for x in chlist if y != dup[0]
        dup[0] = dup[0] + 1
        
        
            

    
        

print("For day",str(x) + "th","of the year, the channels are the following:")
print("Andrew's Room: ", chA)
print("Ryan's Room: ", chR)
print("Logan's Room: ", chL)
print("House: ", chH)
