import unittest
import leap

class TestFunctions(unittest.TestCase):
    def test_div4(self):
        assert leap.div4(4) == True
        assert leap.div4(5) == False
        pass

    def test_div100(self):
        assert leap.div100(100) == True
        assert leap.div100(5) == False
        pass


if __name__ == '__main__':
    unittest.main()
