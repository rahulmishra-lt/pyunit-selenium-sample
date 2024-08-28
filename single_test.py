import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case
    def setUp(self):
        options = ChromeOptions()
        lt_options = {
            "build": 'PyunitTest sample build',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "platformName": 'Windows 10',  # Change your OS version here
            "browserName": 'chrome',  # Change your browser here
            "browserVersion": 'latest'  # Change your browser version here
        }
        options.set_capability('LT:Options', lt_options)

        self.driver = webdriver.Remote(
            command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            options=options
        )

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # You can write the test cases here
    def test_unit_user_should_able_to_add_item(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Url
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Click on check box
        check_box_one = wait.until(EC.element_to_be_clickable((By.NAME, "li1")))
        check_box_one.click()

        # Click on check box
        check_box_two = wait.until(EC.element_to_be_clickable((By.NAME, "li2")))
        check_box_two.click()

        # Enter item in textfield
        textfield = wait.until(EC.presence_of_element_located((By.ID, "sampletodotext")))
        textfield.send_keys("Yey, Let's add it to list")

        # Click on add button
        add_button = wait.until(EC.element_to_be_clickable((By.ID, "addbutton")))
        add_button.click()

        # Verified added item
        added_item = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='done-false']"))).text
        print(added_item)

if __name__ == "__main__":
    unittest.main()