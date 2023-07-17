from map_data import MapData
from data_model import Coin, DataContainer

baseDataObject = {
    "id": [],
    "image_name": [],
    "dynasty": [],
    "coin_type": [],
    "details": [],
}


def createDataFrame():
    # Create Data object
    data = MapData()
    dataContainer = DataContainer(dataObject=baseDataObject)
    # map data from json file
    data.mapDataFromJSON("data.json")

    # map data to datacontainer
    for dataObject in data.getMapData():
        coin = Coin(
            image_name=dataObject["image_name"],
            dynasty=dataObject["dynasty"],
            coin_type=dataObject["coin_type"],
            details=dataObject["details"],
        )
        dataContainer.add(coin.dic())
    dataContainer.exportDataFramToCSV(fileName="data.csv")
    dataContainer.exportDataFrameToExcel(fileName="data.xlsx")
    print(dataContainer.getDataFrame())


if __name__ == "__main__":
    createDataFrame()
