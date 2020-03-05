import csv 
import matplotlib.pyplot as plt
import numpy as np

#Lists!
Team = []
OPR = []

#puts stuff in lists
with open("2019.csv") as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
       
    #remove the header
    Team.remove(Team[0])             
    OPR.remove(OPR[0])


c = input("blueone")
c = "frc" + c

resblueone = 0
for i in range(0, len(Team)): 
    if Team[i] == c: 
        resblueone = i + 1
        break

cheeezits = input("bluetwo")
cheeezits = "frc" + cheeezits

resbluetwo = 0
for i in range(0, len(Team)): 
    if Team[i] == cheeezits: 
        resbluetwo = i + 1
        break

w = input("bluethree")
w = "frc" + w 
resbluethree = 0
for i in range(0, len(Team)): 
    if Team[i] == w: 
        resbluethree = i + 1
        break

pineapple = input("redone")
pineapple = "frc" + pineapple
resredone = 0
for i in range(0, len(Team)): 
    if Team[i] == pineapple: 
        resredone = i + 1
        break

z = input("redtwo")
z = "frc" + z
resredtwo = 0
for i in range(0, len(Team)): 
    if Team[i] == z: 
        resredtwo = i + 1
        break

q = input("redthree")
q = "frc" + q
resredthree = 0
for i in range(0, len(Team)): 
    if Team[i] == z: 
        resredthree = i + 1
        break

resblueone = int(resblueone)
resbluetwo = int(resbluetwo)
resbluethree = int(resbluethree)
resredone = int(resredone)
resredtwo = int(resredtwo)
resredthree = int(resredthree)

#OPR, locate in list
OPRBlueone = (OPR[resblueone])
OPRBluetwo = (OPR[resbluetwo])
OPRBluethree = (OPR[resbluethree])
OPRRedone = (OPR[resredone])
OPRRedtwo = (OPR[resredtwo])
OPRRedthree = (OPR[resredthree])


#calculations
oprblue = float(OPRBlueone) + float(OPRBluetwo) + float(OPRBluethree)
oprred = float(OPRRedone) + float(OPRRedtwo) + float(OPRRedthree)

redscore = oprred*1.4
bluescore = oprblue*1.4

if bluescore > redscore:
    difference = bluescore - redscore
    print ("blue wins, total OPR = " + str(oprblue))
    print ("red loses, total OPR = " + str(oprred))
    print("win margin = " + str(difference))
elif redscore > bluescore:
    difference = redscore - bluescore
    print ("red wins, total OPR =" + str(oprred))
    print ("blue loses, total OPR = " + str(oprblue))
    print("win margin = " + str(difference))

print("red score =" + str(redscore))
print("blue score =" + str(bluescore))
