def entities_pie(categories):
    import matplotlib.pyplot as p
    import csv
    import numpy as np
    with open("data\sol_data.csv", "r") as f:
        lines = csv.reader(f)
        header_row = next(lines)
        # print(header_row)
        Planets = []
        Non_Planets = []
        # entitity = [Planets, Non_Planets]
        # data_pie = ['Planets', 'Non_Planets']

        for row in lines:
            Planets.append(len(row[21]))
            #print(Planets)
            Non_Planets.append(len(row[0]))
            #print(Non_Planets)
    fig = p.figure(figsize = (10, 7))
    p.pie(Non_Planets, labels = Planets)
    #p.pie(entitity, labels = data_pie)
    p.show()

#entities_pie('data_pie')
"""
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """




def entities_bar(categories):

    import matplotlib.pyplot as plt
    import pandas as pd
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    a_dictionary = {"low":1,
                    "medium":2,
                     "high":3
    }
    keys = a_dictionary.keys()
    values = a_dictionary.values()

    plt.bar(keys, values)
    # df = pd.read_csv('data\sol_data.csv')
    # X = list(df.iloc[:, 0])
    # #print(X)
    # Y = list(df.iloc[:, 8])
    # #print(Y)
    # plt.bar(X, Y, color='g')
    # plt.title("Gravity plot")
    # plt.xlabel("Names of planets")
    # plt.ylabel("Gravity")
    plt.show()


#entities_bar('bar')


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
#     import matplotlib.pyplot as plt
#     summary = {
#         "orbited planet": {
#             "small": ['1 Ceres', '136199 Eris', 'Uranus'],
#             "large": ['Jupyter', 'Saturn']
#         }
#     }
#
#     plt.plot(summary, kind="bar", stacked=True)
#     plt.show()
#
# orbits('summary')


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    import random
    import csv
    from itertools import count
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    plt.style.use("fivethirtyeight")

    low = []
    medium = []
    high = []

    fieldnames = ["gravity"]
    with open ("data\sol_data.csv", 'r') as f:
        reader = csv.DictReader(f, fieldnames = 'gravity')
        header_row = next(reader)
        info = {
            'low' : 0.00081,
            'medium' : 6.321575,
            'high' : 274
        }
    plt.plot(low, medium, high)
    ani = FuncAnimation(plt.gcf(), gravity_animation, interval=1000)


    # index = count()

    # def animate(i):
    #     x_vals.append(next(index))
    #     y_vals.append(random.randint(0, 5))

    #plt.tight_layout()
    plt.show()












gravity_animation('categories')
