import unittest

class ExampleTest(unittest.TestCase):
    # TestCase class runs this before each test
    def setUp(self):
        pass
    
    # TestCase class runs this after each test
    def tearDown(self):
        pass
    

    # anything that starts with test_ will be treated as such
    def test_something(self):
        self.assertEqual(2+2, 4)
        self.assertNotEqual(3+5, 5)
        # there are many more assert methods available
    
    def test_other_thing(self):
        pass
    

if __name__ == "__main__":
    unittest.main()