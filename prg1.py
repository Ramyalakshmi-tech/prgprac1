import unittest

def add(x,y):
    return x+y
class MyApps(unittest.TestCase):
    def test_case_add(self):
        a=12
        b=22
        c=add(a,b)
        self.assertEqual(a + b, c)
    def test_case_add1(self):
        a=12.34
        b=34.4
        c=add(a,b)
        self.assertEqual(c,a+b)

def adds(x,y,z):
    return x+y+z
class MyAppss(unittest.TestCase):
    def test_case_adde(self):
        a=12
        b=22
        c=78
        d=adds(a,b,c)
        self.assertEqual(a+ b + c, d)
    def test_case_addg(self):
        a=12.34
        b=34.4
        c=89.6
        d=adds(a,b,c)
        self.assertEqual(d,a+b+c)

def sub(x,y):
    return x-y
class MyAppssub(unittest.TestCase):
    def test_case_sub(self):
        a=12
        b=22
        c=sub(a,b)
        self.assertEqual(a - b, c)
    def test_case_sub1(self):
        a=12.34
        b=34.4
        c=sub(a,b)
        self.assertEqual(c,a-b)

def mul(x,y):
    return x*y
class MyAppsmul(unittest.TestCase):
    def test_case_mul(self):
        a=12
        b=22
        c=mul(a,b)
        self.assertEqual(a * b, c)
    def test_case_mul1(self):
        a=12.34
        b=34.4
        c=mul(a,b)
        self.assertEqual(c,a*b)

def div(x, y):
            return x / y

class MyAppsdiv(unittest.TestCase):
            def test_case_div(self):
                a = 12
                b = 22
                c = div(a, b)
                self.assertEqual(a / b, c)

            def test_case_div1(self):
                a = 12.34
                b = 34.4
                c = div(a, b)
                self.assertEqual(c, a / b)



if __name__=="__main__":
    unittest.main();