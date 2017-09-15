import unittest
from wall import app

class WallTester(unittest.TestCase):

    def setUp(self):
        app.testing=True
        self.app = app.test_client()
    
    def tearDown(self):
        pass
    
    def test_havelandingpage(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()