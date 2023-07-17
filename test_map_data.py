import map_data
import unittest
import glob


class TestUtility(unittest.TestCase):
    def test_mapdata_initial(self):
        test = map_data.MapData()
        # test.mapImageDataFromFile(dirName="test")
        # print(test.getMapData())

        # test.renameMapData("jpg")
        # print(test.getMapData())
        test.mapDataFromJSON("./data.json")
        print(test.getMapData())


if __name__ == "__main__":
    unittest.main()
