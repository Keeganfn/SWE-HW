import unittest
import leap

class TestFunctions(unittest.TestCase):
    def test_div4(self):
        assert leap.div4(4) == True
        assert leap.div4(5) == False
        pass

if __name__ == '__main__':
    unittest.main()
