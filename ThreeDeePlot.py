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

with open('2003.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        Team.append(int(row[0]))
        OPR.append(int(row[1]))
        DPR.append(int(row[2]))
        CCWM.append(int(row[2]))


#x = [int(i) for i in OPR]
#y = [int(i) for i in DPR]
#z = [int(i) for i in CCWM]

ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()


#Need to turn list into integers/float to be able to plot them. The first possible issue could be the commas and ' ' marks, which we can remove. Otherwise, storing in a list may
#(cont) not be the best idea. 