import csv 
import matplotlib.pyplot as plt
import numpy as np

actualred1 = []
actualred2 = []
actualred3 = []
actualblue1 = []
actualblue2 = []
actualblue3 = []
actualredscore = []
actualbluescore = []

team = []
opr = []

with open("2019.csv") as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
       
    #remove the header
    Team.remove(Team[0])             
    OPR.remove(OPR[0])

with open("Match Data Example.csv") as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        #add colums into the lists
       
    #remove the header
    Team.remove(Team[0])             
    OPR.remove(OPR[0])

#compare the actual scores with my match predictor to a Least Squares Regression (for now)