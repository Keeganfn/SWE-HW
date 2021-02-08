import unittest
from average_list import average_list

class TestFunctions(unittest.TestCase):
    def test_add(self):
        assert average_list([1,2,3,4]) == 2.5
        assert average_list(["1",2,3,4]) == 2.5
        assert average_list(["the",2,3,4]) == None
        assert average_list([1.0,2,3,4]) == 2.5
        assert average_list([]) == None
        assert average_list([0,0,0,0]) == None

        pass

if __name__ == '__main__':
    unittest.main()
