"""This tests functionality of our site!"""
from selenium import webdriver
import unittest

# Testing landing page functionality
class FunTestCase(unittest.TestCase):
    """This tests the functionalit of our landing page! wewt!"""
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()

    
    # A user visits '/' and sees two forms asking them to log in and/or register!
    def test_landing_shows_2_forms(self):
        self.browser.get('localhost:8000/')
        logform = self.browser.find_element_by_id("logform")
        regform = self.browser.find_element_by_id('regform')
        self.assertIsNotNone(logform)
        self.assertIsNotNone(regform)
    # A user fills out a a registration from correctly and is registered!
    def test_valid_registration_goes_to_dash(self):
        self.browser.get('localhost:8000/')
        self.browser.post(regURL, regData)
        
    # After succesffully registering a user is shown the dashboard
    # After a invalid registration attempt, user is redirected to landing and shown errors
if __name__ == "__main__":
    print("Let the testing begin!")
    unittest.main()