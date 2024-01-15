import unittest
import pandas as pd
import openpyxl
import excel_read

class MyTestCase(unittest.TestCase):
    def setUp(self):
        address = {"Address 1": ["", "Unit 702"], "Address 2": ["Capitol Sq SW", "867 Peachtree St NE"], "City": ["Atlanta", "Atlanta"], "State": ["GA", "GA"], "Zip Code": ["30334", "30308"]}
        df = pd.DataFrame(address)
        df.to_excel("test1.xlsx", index=False)


    def testReadAddresses(self):
        test_file = "test1.xlsx"
        addresses = excel_read.get_addresses(test_file)
        address = addresses[0]
        self.assertEqual("", address.address1, )
        self.assertEqual("Capitol Sq SW", address.address2, )
        self.assertEqual("Atlanta", address.city)
        self.assertEqual("GA", address.state)
        self.assertEqual("30334", address.zip)

if __name__ == '__main__':
    unittest.main()
