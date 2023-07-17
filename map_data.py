import glob
import os
import uuid


class MapData:
    __data__ = {}

    def __init__(self, dirName):
        self.dirName = dirName
        self.__mapData__()

    def __mapData__(self):
        for i in glob.iglob(self.dirName, recursive=True):
            if os.path.isdir(i):
                continue
            self.__data__[i] = i

    def getMapData(self):
        return self.__data__

    ## Warning: Do not run this method
    ## on main image datasets
    ## it would rename randomly add files
    def renameMapData(self, format):
        for i in self.__data__.keys():
            self.__data__[i] = f"{uuid.uuid4()}.{format}"

        for i in self.__data__.keys():
            path = i.split("/")
            path = "/".join(path[0 : (len(path) - 1)])
            path = os.path.join(path, self.__data__[i])
            os.rename(i, path)
