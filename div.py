import unittest


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