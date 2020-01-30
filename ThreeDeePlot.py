import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

listTeam = []
listOPR = []
listDPR = []
listCCWM = []
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

path = "C:\Users\A\Documents\GitHub\AmericanPy\2003.csv"
with open(path) as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        listTeam.append(row[0])
        listOPR.append(row[1])
        listDPR.append(row[2])
        listCCWM.append(row[2])


#x = firstColumn
#y =[5,6,2,3,13,4,1,2,4,8]
#z =[2,3,3,3,5,7,9,11,9,10]



#ax.scatter(x, y, z, c='r', marker='o')

#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')

#plt.show()

print(listTeam)
