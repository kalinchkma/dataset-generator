import map_data
import unittest


class TestUtility(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()

    test = map_data.MapData(dirName="Gupta/**/*")
    print(len(test.getMapData()))
