# Task 17: Import the modules csv, tui and visual
# TODO: Your code here
import csv
import tui
import visual
from abc import ABC, abstractmethod
import json

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here
records = []


def run():
    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        menu_options = tui.menu()
        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here
        if (menu_options == 1):
            # Display the start message
            tui.started("Data loading")
            # Get file path
            filepath = tui.source_data_path()
            # Load data to records
            if (filepath != None):
                try:  # If doesn't exist
                    f = open(filepath)
                    firstline = False
                    for line in f:
                        if (firstline == False):
                            firstline = True
                            continue
                        records.append(line)
                    f.close()
                except:
                    print("The file dose not exist!")
            # Display complete message
            tui.completed("Data Loading")
        #     global records
        #     tui.started("Data loading")
        #     tui.source_data_path()
        # with open("data\sol_data.csv") as f:
        #     for line in f:
        #         print(line)
        # tui.completed("data processed")
        # with open("data\sol_data.csv") as f1:
        #     #f1.readline()
        #     records.append(f1.readline())
        #     print(records)
        #     tui.completed("Load Data")
        #     for line in f1:
        #         print(line.split(",")[14])

        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        # TODO: Your code here
        if (menu_options == 2):
            tui.started("The data processing")
            # If records is empty
            if (len(records) != 0):
                process_option = tui.process_type()
                # If the user selected the option to retrieve an entity
                if (process_option == 1):
                    tui.started('The entity retrieval process')  # start message
                    # find the entity in records
                    specifiedEntity = tui.entity_name()
                    bFindEntity = False
                    findRecord = []
                    for record in records:
                        recordDetailList = record.strip().split(",")
                        if (recordDetailList[0] == specifiedEntity):
                            bFindEntity = True
                            findRecord = recordDetailList
                            break
                    # display the record including user entity
                    if (bFindEntity == True):
                        cols = []
                        tui.list_entity(findRecord, cols)
                    else:
                        print("The entity does not exist!")
                    # Complete message
                    tui.completed("The entity retrieval process")
                # If the user selected the option to retrieve an entity's details
                if (process_option == 2):
                    tui.started('The entity details retrieval process')
                    # get entity and cols from user input
                    # specifiedEntity, cols = tui.entity_details()
                    detailEntities = tui.entity_details()
                    specifiedEntity = detailEntities[0]
                    cols = detailEntities[1]
                    # find the entity in records again
                    bFindEntity = False
                    findRecord = []
                    for record in records:
                        recordDetailList = record.split(",")
                        if (recordDetailList[0] == specifiedEntity):
                            bFindEntity = True
                            findRecord = recordDetailList
                            break
                    # display the entity details in cols
                    if (bFindEntity == True):
                        tui.list_entity(findRecord, cols)
                        # print(list(detailEntities))
                    else:
                        print("The entity does no exist!")
                    tui.completed("The entity details retrieval process")
                # If the user selected the option to categorise entities by their type
                if process_option == 3:
                    tui.started("The entity type categorisation process")
                    # get planet entities and non-planet entities in records
                    planetsList = []
                    nonPlanetsList = []
                    for record in records:
                        recordDetailList = record.split(",")
                        if recordDetailList[1] == 'TRUE':
                            planetsList.append(recordDetailList[0])
                        if recordDetailList[1] == 'FALSE':
                            nonPlanetsList.append(recordDetailList[0])
                    # create dic param category
                    category = {
                        'planets': planetsList,
                        'non-planets': nonPlanetsList
                    }
                    # display category
                    tui.list_categories(category)
                    tui.completed("The entity type categorisation process")
                # If the user selected the option to categorise entities by their gravity
                if process_option == 4:
                    tui.started('The categorisation by entity gravity process')
                    # get tupe gravity_range by user input
                    tupleGravityRange = tui.gravity_range()
                    # get lower and medium, high entities in records
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
                    # create dic param category
                    category = {
                        'lower': lowerList,
                        'medium': mediumList,
                        'high': highList
                    }
                    # display category
                    tui.list_categories(category)

                    tui.completed('The categorisation by entity gravity process')
                # If the user selected the option to generate an orbit summary
                if process_option == 5:
                    tui.started('The orbit summary process')
                    # get entities by user input
                    entityNameList = tui.orbits()
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
                    # display orbit entities
                    tui.list_categories(name_of_dict)
                    tui.completed('The orbit summary process')
                tui.completed('The data processing')
            else:
                print("Records is empty! Please load data")
        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        #
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        # TODO: Your code here
        if menu_options == 3:
            tui.started('The data visualisation')
            if (len(records) != 0):
                # select option form visualisation menu by user input
                visualisation_option = tui.visualise()
                # if the user selected the option to visualise the entity type
                if (visualisation_option == 1):
                    tui.started("The entity type visualisation process")
                    planetsList = []
                    nonPlanetsList = []
                    # get planet and non-planet entities in records
                    for record in records:
                        recordDetailList = record.split(",")
                        if recordDetailList[1] == 'TRUE':
                            planetsList.append(recordDetailList[0])
                        if recordDetailList[1] == 'FALSE':
                            nonPlanetsList.append(recordDetailList[0])
                    # print(nonPlanetsList)
                    # print(planetsList)
                    # create dic param category of planet and non-planet entities
                    category = {
                        'planets': planetsList,
                        'non-planets': nonPlanetsList
                    }
                    # display planet and non-planet entities by pie
                    visual.entities_pie(category)
                    tui.completed('The entity type visualisation process')
                    # if the user selected the option to visualise the entity gravity
                if visualisation_option == 2:
                    tui.started('The entity gravity visualisation process')
                    # get tuple gravity range by user input
                    tupleGravityRange = tui.gravity_range()
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
                    category = {
                        'lower': lowerList,
                        'medium': mediumList,
                        'high': highList
                    }
                    # display category by bar chart
                    visual.entities_bar(category)
                    tui.completed('The entity gravity visualisation process')
                # if the user selected the option to visualise the orbit summary
                if visualisation_option == 3:
                    tui.started('The entity orbit summary visualisation process')

                    # get entities by user input
                    entityNameList = tui.orbits()
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
                    visual.orbits(name_of_dict)
                    tui.completed('The entity orbit summary visualisation process')

                # if the user selected the option to animate the planet gravities
                if visualisation_option == 4:
                    tui.started('The gravity animation visualisation process')
                    # get tuple gravity range by user input
                    tupleGravityRange = tui.gravity_range()
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
                    category = {
                        'lower': lowerList,
                        'medium': mediumList,
                        'high': highList
                    }
                    # display gravity category by animation
                    visual.gravity_animation(category)

                    tui.completed('The gravity animation visualisation process')
                tui.completed('The data visualisation')
            else:
                print("Records is empty! Please load data")

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets 
        # in alphabetical order.
        # TODO: Your code here
        if menu_options == 4:
            tui.started('The save process')
            # if records is empty
            if len(records) != 0:
                # select opion from savemenu by user input
                saveMenu = tui.save()
                if (saveMenu == 1):
                    # create Abstract class
                    class AbstracterWriter(ABC):
                        def __init__(self, recordsdata):
                            self._recordsdata = recordsdata

                        @abstractmethod
                        def RecordsToJson(self):
                            pass

                    # create inheritance class
                    class ConcreteWriter(AbstracterWriter):
                        def __init__(self, recordsdata):
                            super().__init__(self)

                        # the method to write data into json file
                        def RecordsToJson(self):
                            # find planed and non-planed entities in records
                            planetsList = []
                            nonPlanetsList = []
                            for record in records:
                                recordDetailList = record.split(",")
                                if (recordDetailList[1] == 'TRUE'):
                                    planetsList.append(recordDetailList[0])
                                if (recordDetailList[1] == 'FALSE'):
                                    nonPlanetsList.append(recordDetailList[0])
                            # sort planetslist and nonplanetlist
                            planetsList.sort()
                            nonPlanetsList.sort()
                            # create sum list of sorted planetslist and nonplanetlist
                            newRecords = []
                            # find each planet entity record in records and inset it
                            for planet in planetsList:
                                for record in records:
                                    recordDetailList = record.split(",")
                                    if recordDetailList[0] == planet:
                                        newRecords.append(record)
                            # find each non-planet entity record in records and inset it
                            for nonplanet in nonPlanetsList:
                                for record in records:
                                    recordDetailList = record.split(",")
                                    if recordDetailList[0] == nonplanet:
                                        newRecords.append(record)
                            # print(newRecords)
                            # convert list to json type
                            # jsondata = json.dumps(newRecords, indent=4, skipkeys=True, sort_keys=True)
                            # print(jsondata)
                            # with open('data.json', 'w') as jsonfile:
                            #     json.dump(newRecords, jsonfile)
                            jsondata = '[\n'
                            for record in newRecords:
                                strrecord = '    ' + record
                                strrecord = strrecord[0:-2] + ',\n'
                                jsondata += strrecord
                            jsondata = jsondata[0:-3]
                            jsondata += '\n]'
                            # print(jsondata)
                            # write Json data to out.json file
                            outJSONFileName = 'out.json'
                            fd = open(outJSONFileName, 'w')
                            fd.write(jsondata)
                            fd.close()

                    writer = ConcreteWriter(records)
                    writer.RecordsToJson()
                else:
                    tui.error('Select a correct menu option.')
                tui.completed('The save process')
            else:
                print("Records is empty! Please load data")
        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        # TODO: Your code here
        if (menu_options == 5):
            break
        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        # TODO: Your code here
        # Display an error message
        if (menu_options == None):
            tui.error("Select a correct menu option.")


if __name__ == "__main__":
    run()
