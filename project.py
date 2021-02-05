import unittest


class Calculator():
    def add(self,a,x):
        return a+x
    def subtract(self,a,x):
        return a-x
    def multiply(self,a,x):
        return a*x
    def divide(self,a,x):
        if(x==0):
            return "you should not devide by zero"
        else:
            return a/b






class TestCalc(unittest.TestCase):
    calculator = Calculator()
    def test_addition(self):
        self.assertEqual(calculator.add(2,4),7)
        self.assertEqual(calculator.add(2,4),6)
        self.assertEqual(calculator.add(2,1),3)
        self.assertEqual(calculator.add(3,1),4)
        self.assertEqual(calculator.add(4,4),8)
    def test_devision(self):
        self.assertEqual(calculator.divide(10,2),5)
        self.assertEqual(calculator.divide(10,300),30)
        self.assertEqual(calculator.divide(2,40),20)
        self.assertEqual(calculator.divide(1000,10),100)
        thing = "you should not devide by zero"
        self.test_string_equality(calculator.divide(2,4),thing)
    def test_subtraction(self):
        self.assertEqual(calculator.subtract(2,4),-2)
        self.assertEqual(calculator.subtract(80,50),30)
        self.assertEqual(calculator.subtract(50,20),30)
        self.assertEqual(calculator.subtract(100,80),30)
        self.assertEqual(calculator.subtract(5,5),0)
    def test_multiplication(self):
        self.assertEqual(calculator.multiply(2,4),8)
        self.assertEqual(calculator.multiply(3,3),9)
        self.assertEqual(calculator.multiply(4,4),16)
        self.assertEqual(calculator.multiply(5,5),25)
        self.assertEqual(calculator.multiply(10,10),100)
        
        
        
unittest.main()
    
