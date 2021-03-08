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

    def test_div400(self):
        assert leap.div400(400) == True
        assert leap.div400(5) == False
        pass

    def test_leap_check(self):
        assert leap.leap_check(400) == True
        assert leap.leap_check(2024) == True
        assert leap.leap_check(3) == False
        assert leap.leap_check(300) == False
        pass




if __name__ == '__main__':
    unittest.main()
