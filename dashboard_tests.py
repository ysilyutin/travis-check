import unittest
from pyvirtualdisplay import Display
from selenium import webdriver
import selenium.webdriver.support.ui as ui


class DashboardTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.display = Display(visible=0, size=(1024, 768))
        cls.display.start()
        # Create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://testmunk.com/login")

    def test_verify_amount_of_testruns(self):
        last_testrun = self.driver.find_element_by_class_name("run-name-input").get_attribute("title")
        last_testrun_number = int(last_testrun.split()[1])

        # Find amount of testruns on the page
        testruns = self.driver.find_elements_by_class_name("run-name-input")
        self.assertEqual(len(testruns), last_testrun_number)

    def test_new_testrun_button_opens_popup_window(self):
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

        # New Testrun button should open the new popup window
        new_testrun_button = self.driver.find_element_by_id("new-testrun-widget")
        testrun_popup_window = self.driver.find_element_by_id("testrun-application")

        wait = ui.WebDriverWait(self, 10)
        new_testrun_button.click()
        wait.until(lambda driver: testrun_popup_window.is_displayed())

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()
        cls.display.stop()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
