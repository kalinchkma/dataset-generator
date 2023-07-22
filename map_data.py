import glob
import os
import uuid
import json


class MapData:
    __data__ = []

    ## Map Data from file
    def mapImageDataFromFile(self, dirName):
        dirPath = dirName + "/**/*"
        for i in glob.iglob(dirPath, recursive=True):
            if os.path.isdir(i):
                continue
            self.__data__[i] = i

    ## Map data from json file
    def mapDataFromJSON(self, filePath):
        with open(filePath) as file:
            data = json.load(file)
            self.__data__ = self.__data__ + data
        print(self.__data__)

    ## Get MapData
    def getMapData(self):
        return self.__data__

    ## Warning: Do not run this method
    ## on main image datasets
    ## it will rename file names randomly
    def renameMapData(self, format):
        data = {}
        for i in self.__data__.keys():
            self.__data__[i] = f"{uuid.uuid4()}.{format}"

        for i in self.__data__.keys():
            path = i.split("/")
            path = "/".join(path[0 : (len(path) - 1)])
            path = os.path.join(path, self.__data__[i])
            os.rename(i, path)
            data[path] = path
        self.__data__ = data
