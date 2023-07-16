import map_data
import unittest


class TestUtility(unittest.TestCase):
    pass


if __name__ == "__main__":
    test = map_data.MapData(dirName="test/**/*")
    print(test.getMapData())

    test.renameMapData("jpg")
    print(test.getMapData())

    unittest.main()
