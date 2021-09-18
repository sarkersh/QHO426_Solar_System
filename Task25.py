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
minGravity = float(input("lower limit:- "))
maxGravity = float(input("upper limit:- "))
listGravityRange = [minGravity, maxGravity]
tupleGravityRange = tuple(listGravityRange)
# get lower, medium and high entities in records
lowerList = []
mediumList = []
highList = []
for record in records:
    recordDetailList = record.split(",")
    if float(recordDetailList[8]) < tupleGravityRange[0]:
        lowerList.append(recordDetailList[0])
    if float(recordDetailList[8]) >= tupleGravityRange[0] and float(recordDetailList[8]) <= \
            tupleGravityRange[1]:
        mediumList.append(recordDetailList[0])
    if float(recordDetailList[8]) > tupleGravityRange[1]:
        highList.append(recordDetailList[0])
# create dic param
categories = {
    'lower': lowerList,
    'medium': mediumList,
    'high': highList
}
# display category by bar chart
le = len(categories)
X = np.arange(le)
Y = []
totalcount = 0
for col in categories:
    lencol = len(categories[col])
    Y.append(lencol)
    totalcount += lencol

# plt.xticks([])
# plt.yticks([])
plt.bar(X, Y, facecolor='#9999ff', edgecolor='r')
count = 0
for x, y, col in zip(X, Y, categories):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    plt.text(x + 0.4, 0, col, ha='center', va='top')

plt.title("Entities bar")
plt.show()