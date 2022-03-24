import unittest

def check_even_or_odd(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

class MyEvenorOddApp(unittest.TestCase):

    def test_case_even_or_odd1(self):
        result=check_even_or_odd(2)
        self.assertEqual("even",result)

    def test_case_even_or_odd2(self):
        result=check_even_or_odd(5)
        self.assertLogs("odd",result)



def check_divisibleby7(x):
    if x%7 ==0:
        return True
    else:
        return False

class CheckDivisble(unittest.TestCase):

    def test_case_check_divisible_1(self):
        result=check_divisibleby7(4)
        self.assertFalse(result)

    def test_case_check_divisible_2(self):
        result=check_divisibleby7(14)
        self.assertTrue(result)

    def Prime_or_not(x):
        flag=False

        if x>1:
            for i in range(2,x):
                if(x%i)==0:
                    flag=True
                    break
        if flag:
            return True
        else:
            return False

if __name__=="__main__":
    unittest.main();