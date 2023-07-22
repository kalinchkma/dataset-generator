import numpy as np
import pandas as pd
from constant import baseDataObject


# coin data entry wrapper
class Coin:
    __coin = {}

    def __init__(self, coin: dict) -> None:
        for key in baseDataObject.keys():
            if key == "id":
                continue
            self.__coin[key] = coin[key]

    ## Convert data into dictionary
    def dic(self) -> dict:
        return self.__coin

    def __str__(self) -> str:
        return f"image_name: {self.__image_name}|dynasty: {self.__dynasty}|coin_type: {self.__coin_type}|details: {self.__details}|label: {self.__label}"


# Datasets wrapper
class DataContainer:
    __npDataList = {}
    __container = pd.DataFrame([])
    __n = 0

    def __init__(self, dataObject):
        self.__npDataList = dataObject

    ## Add data to data datafra
    def add(self, data: Coin):
        self.__npDataList["id"].append(self.__n)
        for i in self.__npDataList.keys():
            if i != "id":
                self.__npDataList[i].append(data[i])
        self.__n += 1
        return self

    ## Return dataframe
    def getDataFrame(self):
        return self.__container

    ## Return data as dictionary
    def getDataList(self):
        return self.__npDataList

    ## export dataframe to excel
    def exportDataFrameToExcel(self, fileName):
        self.__container.to_excel(fileName, index=False)

    ## export dataframe to csv
    def exportDataFramToCSV(self, fileName):
        self.__container.to_csv(fileName, sep=",", index=False)
