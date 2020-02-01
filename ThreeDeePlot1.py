import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

Team = []
OPR = []
DPR = []
CCWM = []

request = input("team number")
request = "frc" + request

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')


with open('2003.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
        DPR.append(row[2])
        CCWM.append(row[3])
    Team.remove(Team[0])
    OPR.remove(OPR[0])
    DPR.remove(DPR[0])
    CCWM.remove(CCWM[0])

    OPR = [ float(x) for x in OPR ]
    DPR = [ float(x) for x in DPR ]
    CCWM = [ float(x) for x in CCWM ]


x = OPR
y = DPR
z = CCWM

ax.scatter(x, y, z, s=3, c='r', marker='*')

exprime = Team.index(request)

#identify the OPR DPR and CCWM position

a = OPR[exprime]
b = DPR[exprime]
c = DPR[exprime]

ax.scatter(a, b, c, s=3, c='b', marker='s')


ax.set_xlabel('OPR')
ax.set_ylabel('DPR')
ax.set_zlabel('CCWM')
plt.show()