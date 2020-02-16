import csv 
import matplotlib.pyplot as plt
import numpy as np
import tbapy

#Lists!
Team = []
OPR = []


#i love my little bean 

#basic plot stuff
fig = plt.figure()

#puts stuff in lists
with open("2019.csv") as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])

       
    #remove the header
    Team.remove(Team[0])
    OPR.remove(OPR[0])


x = Team 
y = OPR

plt.scatter(x, y,)

print(Team)

plt.show()