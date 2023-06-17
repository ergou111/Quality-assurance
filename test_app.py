import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
from selenium.webdriver.chrome.service import Service

class TestApp(unittest.TestCase):
    def setUp(self):
        service = Service('C:\Program Files\Google\Chrome\Application/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('http://127.0.0.1:5000')

    def test_input_valid(self):
        
        input_box = self.driver.find_element(By.ID, 'input')
        input_box.send_keys('1,2,3,4')

        calculate_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        calculate_button.click()


        result = self.driver.find_element(By.CSS_SELECTOR, '.form-control-static').text
        self.assertEqual(result, '[24, 12, 8, 6]')

    def test_input_invalid(self):
        input_box = self.driver.find_element(By.ID, 'input')
        input_box.send_keys('a,b,c')

        calculate_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        calculate_button.click()

        error_msg = self.driver.find_element(By.CSS_SELECTOR, '.text-danger').text
        self.assertEqual(error_msg, 'Invalid input format. Please enter a comma-separated list of integers.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='UI-test-reports'))