from map_data import MapData
from data_model import Coin, DataContainer
from constant import baseDataObject


def createDataFrame() -> tuple:
    # Create Data object
    data = MapData()
    dataContainer = DataContainer(dataObject=baseDataObject)
    # map data from json file
    data.mapDataFromJSON("data.json")

    # map data to datacontainer
    for dataObject in data.getMapData():
        coin = Coin(dataObject)
        dataContainer.add(coin.dic())
    dataContainer.exportDataFramToCSV(fileName="data.csv")
    dataContainer.exportDataFrameToExcel(fileName="data.xlsx")
    data, label, dynasty, coin_type = dataContainer.getDataFrame()
    return (data, label, dynasty, coin_type)
