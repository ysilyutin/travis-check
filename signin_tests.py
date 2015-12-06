import unittest
from selenium import webdriver
from pyvirtualdisplay import Display
from random import choice
from string import ascii_letters, digits

class SignInTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.display = Display(visible=0, size=(1024, 768))
        cls.display.start()
        # Create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://testmunk.com/login")

    def test_signin_with_valid_credentials(self):
        # Get the email and password textboxes
        email_field = self.driver.find_element_by_name("email")
        email_field.clear()

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()

        sign_in_button = self.driver.find_element_by_id("log-in")

        # Enter valid email\password and click Sign In button
        email_field.send_keys("*****@testmunk.com")
        password_field.send_keys("****")
        sign_in_button.click()

        title = self.driver.title
        self.assertEqual(title, "Dashboard | Testmunk")

    def test_signin_with_invalid_credentials(self):
        # Get the email and password textboxes
        email_field = self.driver.find_element_by_name("email")
        email_field.clear()

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()

        sign_in_button = self.driver.find_element_by_id("log-in")

        # Create a random password string contains letter and digits
        random_password = ''.join([choice(ascii_letters + digits) for i in range(32)])

        # Enter valid email\password and click Sign In button
        email_field.send_keys("*****@testmunk.com")
        password_field.send_keys(random_password)

        sign_in_button.click()

        alert = self.driver.find_element_by_class_name('alert-danger')
        self.assertEqual(alert.text, 'Error:\nInvalid email or password')

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()
        cls.display.stop()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
