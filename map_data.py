import glob
import os


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
