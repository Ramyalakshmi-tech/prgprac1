import unittest


def add(a,b):
    return a+b

class MyApp2(unittest.TestCase):

    def setUp(self):
        self.a=15
        self.b=25
        print("Setup Called")


    def tearDown(self):
        self.a=0
        self.b=0
        print("Teardown called")

    def test_case_add(self):
        #Act
        c=add(self.a,self.b)
        self.assertEqual(self.a+self.b,c)

if __name__ == "__main__":
            unittest.main();