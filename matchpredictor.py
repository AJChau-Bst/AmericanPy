import csv 


#Lists!
Team = []
OPR = []
DPR = []

#puts stuff in lists
with open("2019.csv") as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
        DPR.append(row[2])
       
    #remove the header
    Team.remove(Team[0])             
    OPR.remove(OPR[0])
    DPR. remove(DPR[0])

c = input("blueone")
c = "frc" + c

resblueone = None
for i in range(0, len(Team)): 
    if Team[i] == c: 
        resblueone = i + 1
        break

cheeezits = input("bluetwo")
cheeezits = "frc" + cheeezits

resbluetwo = None
for i in range(0, len(Team)): 
    if Team[i] == cheeezits: 
        resbluetwo = i + 1
        break

w = input("bluethree")
w = "frc" + w 
resbluethree = None
for i in range(0, len(Team)): 
    if Team[i] == w: 
        resbluethree = i + 1
        break

pineapple = input("redone")
pineapple = "frc" + pineapple
resredone = None
for i in range(0, len(Team)): 
    if Team[i] == pineapple: 
        resredone = i + 1
        break

z = input("redtwo")
z = "frc" + z
resredtwo = None
for i in range(0, len(Team)): 
    if Team[i] == z: 
        resredtwo = i + 1
        break

q = input("redthree")
q = "frc" + q
resredthree = None
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

#DPR
DPRBlueone = (DPR[resblueone])
DPRBluetwo = (DPR[resbluetwo])
DPRBluethree = (DPR[resbluethree])
DPRRedone = (DPR[resredone])
DPRRedtwo = (DPR[resredtwo])
DPRRedthree = (DPR[resredthree])

#calculations
oprblue = float(OPRBlueone) + float(OPRBluetwo) + float(OPRBluethree)
oprred = float(OPRRedone) + float(OPRRedtwo) + float(OPRRedthree)
dprblue = float(DPRBlueone) + float(DPRBluetwo) + float(DPRBluethree)
dprred = float(DPRRedone) + float(DPRRedtwo) + float(DPRRedthree)


redscore = (oprred + dprblue)*.5
bluescore = (oprblue + dprred)*.5

if bluescore > redscore:
    difference = bluescore - redscore
    print ("blue wins, total OPR = " + str(oprblue))
    print ("total DPR = " + str(dprblue))
    print ("red loses, total OPR = " + str(oprred))
    print ("total DPR = " + str(dprred))
    print("win margin = " + str(difference))
elif redscore > bluescore:
    difference = redscore - bluescore
    print ("red wins, total OPR =" + str(oprred))
    print ("total DPR = " + str(dprred))
    print ("blue loses, total OPR = " + str(oprblue))
    print ("total DPR= " + str(dprblue))
    print("win margin = " + str(difference))

print("red score =" + str(redscore))
print("blue score =" + str(bluescore))