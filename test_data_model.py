from data_model import Coin, DataContainer
import unittest


class TestDataPackage(unittest.TestCase):
    def test_coin(self):
        result = "image_name: skanda|dynasty: gupta/skanda|coin_type: archer type|details: test"
        coin = Coin(
            image_name="skanda",
            dynasty="gupta/skanda",
            coin_type="archer type",
            details="test",
        )
        self.assertEqual(str(coin), result)

    def test_coin_dic(self):
        result = {
            "image_name": "skanda",
            "dynasty": "gupta/skanda",
            "coin_type": "archer type",
            "details": "test",
        }
        self.assertEqual(
            Coin(
                image_name="skanda",
                dynasty="gupta/skanda",
                coin_type="archer type",
                details="test",
            ).dic(),
            result,
        )

    def test_dataContainer(self):
        dataObject = {
            "id": [],
            "image_name": [],
            "dynasty": [],
            "coin_type": [],
            "details": [],
        }

        test = DataContainer(dataObject=dataObject)

        data = Coin(
            image_name="132", coin_type="123", dynasty="123", details="isadksahd"
        )
        data2 = Coin("132", "123", "123", "isadksahd")
        data3 = Coin("jhagsdg", "asdjh", "123", "isadksahd")
        data4 = Coin("uiy6euwd", "123", "123", "isadksahd")

        test.add(data.dic())
        test.add(data2.dic())
        test.add(data3.dic())
        test.add(data4.dic())

        print(test.getDataFrame())
        # print(str(data))
        test.exportDataFrameToExcel("data.xlsx")
        test.exportDataFramToCSV("data.csv")


if __name__ == "__main__":
    unittest.main()
