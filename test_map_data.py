import map_data
import unittest
import glob


class TestUtility(unittest.TestCase):
    def test_mapdata_initial(self):
        test = map_data.MapData()
        # test.mapDataFromFile(dirName="test")
        # print(test.getMapData())

        # test.renameMapData("jpg")
        # print(test.getMapData())
        test.mapDataFromJSON("./data.json")


if __name__ == "__main__":
    unittest.main()
