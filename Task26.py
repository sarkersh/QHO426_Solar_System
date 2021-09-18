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
entityNames = input('Enter entity names(e.g. Jupiter,Earth,Mars): ')
entityNameList = entityNames.split(",")
# get name of dict (small , large)
name_of_dict = {}
for entity in entityNameList:  # loop each entity
    smallList = []
    largeList = []
    for record in records:  # find the orbit entity in records and divide into small and large
        recordDetailList = record.split(",")
        if (recordDetailList[21] == entity):
            if (float(recordDetailList[10]) < 100):
                smallList.append(recordDetailList[0])
            else:
                largeList.append(recordDetailList[0])
# create orbit entities category
category = {
    "small": smallList,
    "large": largeList
}
# insert category to name_of_dict param
name_of_dict[entity] = category

# display orbit entities by subplot
i = 0
# find max number of "small" and "large" orbiting entities
maxNum = -1
for orbitedPlanet in name_of_dict:
    smallsize = len(name_of_dict[orbitedPlanet]['small'])
    largesize = len(name_of_dict[orbitedPlanet]['large'])
    if smallsize > maxNum:
        maxNum = smallsize
    if largesize > maxNum:
        maxNum = largesize
# create subplot
for orbitedPlanet in name_of_dict:
    smallsize = len(name_of_dict[orbitedPlanet]['small'])
    largesize = len(name_of_dict[orbitedPlanet]['large'])
    plt.subplot(1, len(name_of_dict), i + 1)
    i += 1
    plt.title(orbitedPlanet)
    X = np.arange(2)
    totalsize = smallsize + largesize
    Y = np.array([smallsize, largesize])
    plt.xticks([])
    plt.yticks([])
    plt.ylim(0, maxNum + 10)
    plt.bar(X, Y, facecolor='#9999ff', edgecolor='white')
    for x, y, col in zip(X, Y, name_of_dict[orbitedPlanet]):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        plt.text(x + 0.4, 0, col, ha='center', va='top')
plt.show()
