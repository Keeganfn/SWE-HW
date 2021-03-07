import unittest
import fizzbuzz

class TestFunctions(unittest.TestCase):
    def test_add(self):
        assert fizzbuzz.mult3(18) == True
        assert fizzbuzz.mult3(2) == False
        pass

if __name__ == '__main__':
    unittest.main()
