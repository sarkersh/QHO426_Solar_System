import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
# import pandas as pd
# df = pd.read_csv('data\sol_data.csv')


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """
    # data_pie = df['isPlanet'].value_counts().rename_axis('planet').reset_index(name='planet_count')
    #
    # # Creating plot
    # fig = plt.figure(figsize=(10, 7))
    # plt.pie(data_pie.planet_count, labels=data_pie)
    #
    # # show plot
    # plt.show()

    # a = ['Planet', 'Non-Planet']
    # b = [20, 50]
    # plt.pie(b, labels=a)
    # plt.title("Displaying pie charts for planets and Non Panets", fontsize=16)
    # plt.show()

    # Tutor replit:
    # z = []
    # label = []
    #
    # for i in categories:
    #     label += [i]
    #     z += [len(categories[i])]
    #
    # plt.pie(z, labels=label)
    # plt.show()
    n = len(categories)
    Z = []
    labels = []
    totalcount = 0
    # to used categories convert to array list and calculate total count
    for col in categories:
        lencol = float(len(categories[col]))
        Z.append(lencol)
        labels.append(col)
        totalcount += lencol
    # print(lencol)
    Z = np.array(Z)
    # print(Z)
    # to set colors
    colors = ['yellowgreen', 'gold']
    explode = [0, 0.1]
    # ploting pie chart with labels and colors, set radius
    plt.pie(Z, explode = explode, labels = labels, colors = colors, autopct='%1.1f%%', shadow=True, startangle=90, radius=0.25, center=(0.5, 0.5), frame=True)
    plt.xticks([]), plt.yticks([])
    plt.title("Displaying pie charts for planets and Non Panets", fontsize=8)
    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    # length from categories
    le = len(categories)
    # inbuilt numpy function that returns an ndarray object containing evenly spaced values within a le.
    X = np.arange(le)
    Y = []
    totalcount = 0
    for col in categories:
        lencol = len(categories[col])
        # get value of every categories
        Y.append(lencol)
        totalcount += lencol
    # each coorodinate plot
    # plt.xticks([])
    # plt.yticks([])
    # whole entity value plot
    plt.bar(X, Y, facecolor='#9999ff', edgecolor='white')
    count = 0
    # used to add text inside the plot. The syntax adds text at an arbitrary location of the axes.
    for x, y, col in zip(X, Y, categories):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        plt.text(x + 0.4, 0, col, ha='center', va='top')
    # used to add tile inside plot.
    plt.title("Entities bar")
    plt.show()
    # X = list(df.iloc[:, 0])
    # Y = list(df.iloc[:, 8])
    # plt.bar(X, Y, color='g')
    # plt.title("Gravity plot")
    # plt.xlabel("Names of planets")
    # plt.ylabel("Gravity")
    #
    # # Show the plot
    # plt.show()
    # Tutor replit:
#     label = []
#     z = []
#
#     for i in categories:
#         label += [i]
#         z += [len(categories[i])]
#     plt.bar(label, z)
#     plt.show()






def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    i = 0
    # find max number of "small" and "large" orbiting entities
    maxNum = -1
    for orbitedPlanet in summary:
        smallsize = len(summary[orbitedPlanet]['small'])
        largesize = len(summary[orbitedPlanet]['large'])
        if smallsize > maxNum:
            maxNum = smallsize
        if largesize > maxNum:
            maxNum = largesize
    # create subplot
    for orbitedPlanet in summary:
        # small size planet length
        smallsize = len(summary[orbitedPlanet]['small'])
        # large size planet length
        largesize = len(summary[orbitedPlanet]['large'])
        plt.subplot(1, len(summary), i + 1)
        i += 1
        # total planet count
        plt.title(orbitedPlanet)
        X = np.arange(2)
        totalsize = smallsize + largesize
        Y = np.array([smallsize, largesize])
        plt.xticks([])
        plt.yticks([])
        plt.ylim(0, maxNum + 10)
        # to used draw picture of planet with small and large
        plt.bar(X, Y, facecolor='#9999ff', edgecolor='white')
        # to used add text for each explanation of planet count
        for x, y, col in zip(X, Y, summary[orbitedPlanet]):
            plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
            plt.text(x + 0.4, 0, col, ha='center', va='top')
    plt.show()

    # X = list(df.iloc[:, 0])
    # Y = list(df.iloc[:, 15])
    #
    # # Plot the data using bar() method
    # plt.bar(X, Y, color='g')
    # plt.title("orbit")
    # plt.xlabel("entity name")
    # plt.ylabel("sideralOrbit")
    #
    # # Show the plot
    # plt.show()
    # lst1 = summary["orbited planet"]["small"]
    # lst2 = summary["orbited planet"]["large"]
    # plt.text("small", len(lst1))
    # plt.text("large", len(lst2))
    #
    # print(summary["orbited planet"])

def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    # to used get length
    le = len(categories)
    # inbuilt numpy function that returns an ndarray object containing evenly spaced values within a le.
    X = np.arange(le)
    Y = []
    totalcount = 0
    for col in categories:
        lencol = len(categories[col])
        Y.append(lencol)
        totalcount += lencol

    lowercount = Y[0]
    mediumcount = Y[1]
    highcount = Y[2]
    # to used sorting by size
    Y.sort()
    # to get max value of Y arrange, because sort by size, end value is maximum
    maxNum = Y[2]
    # 1*3 arrange array format
    plotlays, plotcols = [3, 3, 3], ["black", "black", "red"]
    # output style format
    lineList = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                [[1, 1, 2, 2, 2, 2, 2, 2, 2, 2], [0, lowercount, lowercount, 0, 0, 0, 0, 0, 0, 0]],
                [[1, 1, 2, 2, 2, 3, 3, 3, 3, 3], [0, lowercount, lowercount, 0, mediumcount, mediumcount, 0, 0, 0, 0]],
                [[1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
                 [0, lowercount, lowercount, 0, mediumcount, mediumcount, 0, highcount, highcount, 0]]]
    # to used figure of blank plane
    fig = plt.figure()
    # to used figure of x,y coordinate
    ax = plt.axes(xlim=(0, 5), ylim=(0, maxNum + 30))
    # to used add text inside axies for format value, lower value, medium value, maximum value
    timetext0 = ax.text(0, 0, '')
    timetext1 = ax.text(1, lowercount + 3, '')
    timetext2 = ax.text(2, mediumcount + 3, '')
    timetext3 = ax.text(3, highcount + 3, '')
    lines = []
    # Matplotlib Animation With Multiple Subplots and Axes. and read all the lines
    for index, lay in enumerate(plotlays):
        lobj = ax.plot([], [], lw=3, color=plotcols[index])[0]
        lines.append(lobj)

    plt.title("Animate gravities")
    plt.xlabel("Entity name")
    plt.ylabel("Gravity")

    # all line value format
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    # animation definition function
    def animate(i):
        index = i % 4
        # to used set appriciate style of each bar
        for lnum, line in enumerate(lines):
            line.set_data(lineList[index][0], lineList[index][1])
        # to add text according style
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

    # to used add animation with 4 frames and draw interval is 3S in figure.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=4, interval=1000, blit=True)

    plt.show()
    # X = list(df.iloc[:, 0])
    # Y = list(df.iloc[:, 8])
    #
    # # Plot the data using bar() method
    # plt.plot(X, Y, color='g')
    # plt.title("gravity")
    # plt.xlabel("entity name")
    # plt.ylabel("gravity")
    #
    # # Show the plot
    # plt.show()
    # Cousin code:

    # fig, ax = plt.subplots()
    #
    # x = categories["low"]
    # line, = ax.plot("np.sin(x)low", x)
    #
    # def init():
    #     line.set_ydata([np.nan] * len(x))
    #     return line,
    #
    # def animate(i):
    #     line.set_ydata(np.sin(x + i / 100))
    #     return line,
    #
    # ani = animation.FuncAnimation(
    #     fig, animate, init_func=init, interval=2, blit=True, save_count=50)


