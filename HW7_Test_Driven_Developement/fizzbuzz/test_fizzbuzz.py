import unittest
import fizzbuzz

class TestFunctions(unittest.TestCase):
    def test_add(self):
        assert fizzbuzz.mult3(18) == True
        assert fizzbuzz.mult3(2) == False
        pass

    def test_mult5(self):
        assert fizzbuzz.mult5(15) == True
        assert fizzbuzz.mult5(2) == False
        pass

    def test_output(self):
        assert fizzbuzz.output(3) == "Fizz"
        assert fizzbuzz.output(4) == 4
        assert fizzbuzz.output(5) == "Buzz"
        assert fizzbuzz.output(15) == "FizzBuzz" 
        pass



if __name__ == '__main__':
    unittest.main()
