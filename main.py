import os
import glob
import json
from map_data import MapData
from data_model import Coin, DataContainer
from constant import baseDataObject
from rembg import removeBackground


def createDataFrame(dirName: str) -> tuple:
    # Create Data object
    data = MapData()
    dataContainer = DataContainer(dataObject=baseDataObject)

    sourceFile = glob.iglob(os.path.join(os.getcwd(), dirName, "**/*"), recursive=True)

    for file in sourceFile:
        # map data from json file
        if os.path.isfile(file):
            data.mapDataFromJSON(file)

    # map data to datacontainer
    for dataObject in data.getMapData():
        coin = Coin(dataObject)
        dataContainer.add(coin.dic())
    dataContainer.exportDataFramToCSV(fileName="data.csv")
    dataContainer.exportDataFrameToExcel(fileName="data.xlsx")
    data, label, dynasty, coin_type = dataContainer.getDataFrame()
    return (data, label, dynasty, coin_type)


def backgroundRemover(sorceFile: str):
    with open(sorceFile) as file:
        fileDict = json.load(file)
        fileDict = fileDict["image_directory"]
        for d in fileDict.keys():
            removeBackground(d, fileDict[d])
            print("des:", d, "out:", fileDict[d])


if __name__ == "__main__":
    # createDataFrame("data")
    backgroundRemover(sorceFile="config.json")
