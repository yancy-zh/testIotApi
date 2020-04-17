import unittest
class TestBase(unittest.TestCase):
    listOfFurniture = {"sofa": "made of leather",
                   "docking closet": "the wooden closet under the TV set",
                   "tea table": "the table in front of the sofa"}

    listOfAppliances = {
                   "tv set": "tv for the living room"
                    }

    priceList = {"sofa": 2000,
                 "docking closet": 1000,
                 "tv set": 10000,
                 "tea table": 1000,
                }

    def assertResponseOK(self):
        pass