import csv
from abc import ABC, abstractmethod
import json

records = []

class AbstracterWriter(ABC):
    def __init__(self, recordsdata):
        self._recordsdata = recordsdata

    @abstractmethod
    def RecordsToJson(self):
        pass


# create inheritance class
class ConcreteWriter(AbstracterWriter):
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
        # convert list to json type
        jsondata = json.dumps(newRecords, indent=4, skipkeys=True, sort_keys=True)
        with open('data.json', 'w') as jsonfile:
            json.dump(newRecords, jsonfile)


writer = ConcreteWriter(records)
writer.RecordsToJson()