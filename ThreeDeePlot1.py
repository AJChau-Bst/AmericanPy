import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

Team = []
OPR = []
DPR = []
CCWM = []

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

Team = Team[1:]
OPR= OPR[1:]
DPR = DPR[1:]
CCWM = CCWM[1:]

with open('2003.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
        DPR.append(row[2])
        CCWM.append(row[3])


    x = OPR
    y = DPR
    z = CCWM

    ax.scatter(x, y, z, s=3, c='r', marker='*')

    ax.set_xlabel('OPR')
    ax.set_ylabel('DPR')
    ax.set_zlabel('CCWM')
    plt.show()

#print(OPR)
    #Need to turn list into integers/float to be able to plot them. The first possible issue could be the commas and ' ' marks, which we can remove. Otherwise, storing in a list may
    #(cont) not be the best idea. 