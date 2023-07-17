import numpy as np
import pandas as pd


# coin data entry wrapper
class Coin:
    def __init__(self, image_name, dynasty, coin_type, details) -> None:
        self.__image_name = image_name
        self.__dynasty = dynasty
        self.__coin_type = coin_type
        self.__details = details

    ## Convert data into dictionary
    def dic(self) -> dict:
        return {
            "image_name": self.__image_name,
            "dynasty": self.__dynasty,
            "coin_type": self.__coin_type,
            "details": self.__details,
        }

    def __str__(self) -> str:
        return f"image_name: {self.__image_name}|dynasty: {self.__dynasty}|coin_type: {self.__coin_type}|details: {self.__details}"


# Datasets wrapper
class DataContainer:
    __npDataList = {
        "id": [],
        "image_name": [],
        "dynasty": [],
        "coin_type": [],
        "details": [],
    }
    __container = pd.DataFrame([])
    __n = 0

    ## Add data to data datafra
    def add(self, data: Coin):
        self.__npDataList["id"].append(self.__n)
        for i in self.__npDataList.keys():
            if i != "id":
                self.__npDataList[i].append(data[i])
        self.__container = pd.DataFrame(data=self.__npDataList)
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
