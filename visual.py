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
    for col in categories:
        lencol = float(len(categories[col]))
        Z.append(lencol)
        labels.append(col)
        totalcount += lencol
    Z = np.array(Z)
    print(Z)
    colors = ['yellowgreen', 'gold']
    explode = [0, 0.1]
    plt.pie(Z,
            explode = explode,
            labels = labels,
            colors = colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=90,
            radius=0.25,
            center=(0, 0),
            frame=True)
    plt.xticks([]), plt.yticks([])
    plt.title("entities_pie")
    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    le = len(categories)
    X = np.arange(le)
    Y = []
    totalcount = 0
    for col in categories:
        lencol = len(categories[col])
        Y.append(lencol)
        totalcount += lencol

    plt.xticks([])
    plt.yticks([])
    plt.bar(X, Y, facecolor='#9999ff', edgecolor='white')
    count = 0
    for x, y, col in zip(X, Y, categories):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        plt.text(x + 0.4, 0, col, ha='center', va='top')

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



# entities_bar('categories')


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

orbits('summary')
def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
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

    fig, ax = plt.subplots()

    x = categories["low"]
    line, = ax.plot("np.sin(x)low", x)

    def init():
        line.set_ydata([np.nan] * len(x))
        return line,

    def animate(i):
        line.set_ydata(np.sin(x + i / 100))
        return line,

    ani = animation.FuncAnimation(
        fig, animate, init_func=init, interval=2, blit=True, save_count=50)

gravity_animation('categories')

