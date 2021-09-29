import matplotlib.pyplot as plt
import numpy as np

records = []
f = open("data\sol_data.csv")
firstline = False
for line in f:
    if (firstline == False):
        firstline = True
        continue
    records.append(line)
f.close()

planetsList = []
nonPlanetsList = []
# get planet and non-planet entities in records
for record in records:
    recordDetailList = record.split(",")
    if recordDetailList[1] == 'TRUE':
        planetsList.append(recordDetailList[0])
    if recordDetailList[1] == 'FALSE':
        nonPlanetsList.append(recordDetailList[0])
print(planetsList)
print(np.array(nonPlanetsList[0]))
categories = {'planets': planetsList, 'non-planets': nonPlanetsList}
n = len(categories)
Z = []
labels = []
totalcount = 0
# to used categories convert to array list and calculate total count
for col in categories:
    lencol = float(len(categories[col]))
    print(lencol)
    Z.append(lencol)
    # print(lencol)
    labels.append(col)
    # print(labels)
    totalcount += lencol
print(totalcount)
# print(Z)
Z = np.array(Z)
# print(Z)
# to set colors
colors = ['yellowgreen', 'gold']
explode = [0, 0.1]
#plot pie chart with labels and colors, set radius
plt.pie(Z, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, radius=0.3,
        center=(0.5, 0.5), frame=True)
plt.xticks([]), plt.yticks([])
plt.title("Displaying pie charts for planets and Non Planets", fontsize=8)
plt.show()
