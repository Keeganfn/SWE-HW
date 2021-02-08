import unittest
from combine_name import combine

class TestFunctions(unittest.TestCase):
    def test_add(self):
        assert combine("John", "Smith") == "John Smith"
        assert combine("1", "+2") == None
        assert combine("John!", "Smith!") == None

        pass

if __name__ == '__main__':
    unittest.main()
