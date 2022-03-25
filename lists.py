import unittest

def myList():
    list=[67,56,89,679]
    return list



class MyListChecker(unittest.TestCase):
    def test_list(self):
        element=678
        self.assertNotIn(element,myList())

class MyListInChecker(unittest.TestCase):
    def test_list1(self):
        element=679
        self.assertIn(element,myList())

if __name__=="__main__":
    unittest.main();