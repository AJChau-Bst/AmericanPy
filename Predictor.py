import matplotlib.pyplot as plt
import csv

Team = []
OPR = []
DPR = []
CCWM = []

with open('2003.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        Team.append(row[0])
        OPR.append(float(row[1])
        DPR.append(float(row[2])
        CCWM.append(float(row[3])

