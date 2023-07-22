from map_data import MapData
from data_model import Coin, DataContainer
from constant import baseDataObject


def createDataFrame():
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
    print(dataContainer.getDataFrame())


if __name__ == "__main__":
    createDataFrame()
