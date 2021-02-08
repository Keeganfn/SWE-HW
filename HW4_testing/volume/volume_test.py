import unittest
from cube_volume import get_volume

class TestFunctions(unittest.TestCase):
    def test_add(self):
        assert get_volume("the",1, 5) == None
        assert get_volume("3","3", "3") == 27
        assert get_volume(5,5,5) == 125
        assert get_volume(-5,5,5) == None
        assert get_volume(5.5,5,5) == 137.5

        pass

if __name__ == '__main__':
    unittest.main()
