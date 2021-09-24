import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
# print(lowerList)
# print(mediumList)
# print(highList)
# create dic param
categories = {
    'lower': lowerList,
    'medium': mediumList,
    'high': highList
}
# display gravity category by animation
le = len(categories)
print(le)
X = np.arange(le)
Y = []
totalcount = 0
for col in categories:
    lencol = len(categories[col])
    Y.append(lencol)
    totalcount += lencol
#print(lencol)

lowercount = Y[0]
mediumcount = Y[1]
highcount = Y[2]
Y.sort()
maxNum = Y[2]

plotlays, plotcols = [3, 3, 3], ["black", "red", "blue"]
lineList = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [[1, 1, 2, 2, 2, 2, 2, 2, 2, 2], [0, lowercount, lowercount, 0, 0, 0, 0, 0, 0, 0]],
            [[1, 1, 2, 2, 2, 3, 3, 3, 3, 3], [0, lowercount, lowercount, 0, mediumcount, mediumcount, 0, 0, 0, 0]],
            [[1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
             [0, lowercount, lowercount, 0, mediumcount, mediumcount, 0, highcount, highcount, 0]]]
"""main type is [0,lowercount,lowercount,0,mediumcount, mediumcount,0,highcount,highcount,0]
but data exsit only basic and lower value then remove medium and high
so make a 4 cases ~ empty data, lower data exist case ~ first case is empty data ~ second case is empty and lower value
third case is empty, lower value and medium data ~ and fourth case is all data exist"""
fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(0, maxNum + 30))
timetext0 = ax.text(0, 0, '')
timetext1 = ax.text(1, lowercount + 3, '')
timetext2 = ax.text(2, mediumcount + 3, '')
timetext3 = ax.text(3, highcount + 3, '')
lines = []
for index, lay in enumerate(plotlays):
    lobj = ax.plot([], [], lw=3, color=plotcols[index])[0]
    lines.append(lobj)
print(index, lay)
def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    index = i % 4
    for lnum, line in enumerate(lines):
        line.set_data(lineList[index][0], lineList[index][1])

    if index == 0:
        return tuple(lines) + (timetext0,)
    if index == 1:
        strlow = "LowEntities " + str(lowercount)
        timetext1.set_text(strlow)
        return tuple(lines) + (timetext1,)
    if index == 2:
        strmedium = "MediumEntities " + str(mediumcount)
        timetext2.set_text(strmedium)
        return tuple(lines) + (timetext1, timetext2,)
    if index == 3:
        strhigh = "HighEntities " + str(highcount)
        timetext3.set_text(strhigh)
        return tuple(lines) + (timetext1, timetext2, timetext3,)

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=4, interval=1000, blit=True)

plt.show()