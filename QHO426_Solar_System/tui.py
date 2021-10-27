def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    x = 'Solar Record Management System'
    # print of 30 dashes before and after
    print("-" * 30, x, "-" * 30)


#welcome()


def menu():
    """
    Task 2: Display a menu of options and read the user's response.
    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'
    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.
    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.
    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # TODO: Your code here
    # ans = True
    # while ans:
    x = 'Main Menu'
    # print of length of x dashes before and after
    print("-" * len(x), x, "-" * len(x))
    print("""
    1.Load Data
    2.Process Data
    3.Visualise Data
    4.Save Data
    5.Exit
    """)
    strUserInput = input("\t\tWhat would you like to do?: ")
    # it will run as input value arrange is 1 to 5
    try:
        intUserInput = int(strUserInput)
        if (intUserInput >= 1 and intUserInput <= 5):
            return intUserInput
        else:
            return None
    except:
        return None

#menu()


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.
    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function
    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here
    # to used notification word of starting
    print(f"{operation} has started.")


# started("String parameter")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.
    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function
    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here
    # to used notification of end of project
    print(f'{operation} has completed.')


# completed("String parameter")


def error(error_msg):
    """
    Task 5: Display an error message.
    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function
    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here
    # to used notificaton of have a error
    print(f'Error! {error_msg}.')


# error("Its fatal error!")


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here
    # to used enter file name with csv extension
    filepath = input("Please enter the file path: ")
    # detection of file name have a csv extension
    if filepath.endswith("csv"):
        return filepath
    else:
        error("The file entered is not csv file!")
        return None




#source_data_path()

def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    x = "Processing Menu"
    # print of length of x dashes before and after
    print("\n\t\t", "-" * len(x), x, "-" * len(x))
    print("""
        How would you like for the file to be processed\n\t\t(Choose from below e.g.\"1\")?
        1.Retrieve entity
        2.Retrieve entity details
        3.Categorise entities by type
        4.Categorise entities by gravity
        5.Summarise entities by orbit
        """)
    # to used of enter for processed
    strUserInput = input("\t\tWhat would you like to do?: ")
    # to find method of input value arrange of 1 to 5
    try:
        intUserInput = int(strUserInput)
        if (intUserInput >= 1 and intUserInput <= 5):
            return intUserInput
        else:
            return None
    except:
        return None



#process_type()

def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # TODO: Your code here
    # to used read in the name of entity
    name = input("Please type the name of an entity: ")
    return name

#entity_name()

def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # TODO: Your code here
    # read of entity name
    entityName = input("Enter name of an entity: ")
    # read of entity column indexes
    columnIndexes = input('Enter a list of interger column indexes: ')
    # split by ","
    strcolumnlist = columnIndexes.split(",")
    columnList = []
    # detection of name and indexes of entity
    for column in strcolumnlist:
        try:
            intcol = int(column)
            columnList.append(intcol)
        except:
            continue
    return [entityName, columnList]


#print(entity_details())
# GeeksforGeeks. (2019). Python | Get a list as input from user. [online] Available at: https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/?ref=leftbar-rightbar [Accessed 4 Sep. 2021].

def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here
    # enter each entity value to each list variables
    if (len(cols) > 0):
        le = len(entity)
        list = []
        for z in cols:
            if (z >= le):
                continue
            else:
                list.append(entity[z])
        print(list)
    else:
        print(entity)
    return



# list_entity(['Earth', True, 9.8, 0, 8], [0,5])


def list_entities(entities, cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    # to detect specified column indexes and display that
    for entity in entities:
        if len(cols) > 0:
            list = [entities[z] for z in cols] # Using list comprehension
            print(list)
    else:
        print(entities)
    return


#list_entities(['Earth', True, 9.8, 0, 8], [0, 1])


def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here
    for key, value in categories.items():
        print(key, ' : ', value)
    # The param 'categories' is a dictionary type called by main.py

def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # TODO: Your code here
    ans = True
    # to used input lower limit value and upper limit value
    while(ans):
        try:
            minGravity = float(input("lower limit:- "))
            maxGravity = float(input("upper limit:- "))
            ans = False
        except:
            continue
    # to used set correct lower limit and upper limit value
    if (minGravity > maxGravity):
        a = maxGravity
        maxGravity = minGravity
        minGravity = a  # (www.youtube.com, n.d.)
    listGravityRange = [minGravity, maxGravity]
    # tuple containing the limits
    tupleGravityRange = tuple(listGravityRange)
    return tupleGravityRange

# print(gravity_range())


def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here
    # to used input entity nems like Jupiter,Earth ...etc
    entityNames = input('Enter entity names(e.g. Jupiter,Earth,Mars): ')
    # entity names convert to array list
    entityNameList = entityNames.split(",")
    return entityNameList


#print(orbits())


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    x = 'Visualise Menu'
    # print of length of x dashes before and after
    print("\t\t", "-" * len(x), x, "-" * len(x))
    # print multiline messages
    print("""
        How would you like for the data to be visualise\n\t\t(Choose from below e.g.\"1\")?
        1.Entities by type
        2.Entities by gravity
        3.Summary of orbits
        4.Animate gravities
        """)
    # to used input visulized method
    strUserInput = input("\t\tWhat would you like to do?:- ")
    # detect of visulized method arrange 1 to 4
    try:
        intUserInput = int(strUserInput)
        if (intUserInput >= 1 and intUserInput <= 4):
            return intUserInput
        else:
            return None
    except:
        return None


#visualise()


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    x = 'Saving Menu'
    # print of length of x dashes before and after
    print("\n\t\t", "-" * len(x), x, "-" * len(x))
    print("""
        How would you like for the data to be save\n\t\t(e.g.\"1\")?
        1.Export as JSON
        """)
    # to used of save data style  
    strUserInput = input("\t\tWhat would you like to do?:- ")
    # input value is 1 then retuen save data style and value is 0 then return none.
    try:
        intUserInput = int(strUserInput)
        if (intUserInput == 1):
            return intUserInput
        else:
            return None
    except:
        return None
 

#print(save())
