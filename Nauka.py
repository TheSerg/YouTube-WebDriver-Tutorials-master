from mock.mock import self
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearch(unittest.TestCase):


    def SerUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')


    def test_01(self):
        driver = self.driver
        driver.get('https://www.google.com')
        input_filed = driver.find_element_by_id('lst-ib')
        input_filed.send_keys('python')
        input_filed.send_keys(Keys.ENTER)
        time.sleep(2)

        titles = driver.find_element_by_class_name('r')
        for title in titles:
            assert 'python' in title.text.lower()


    def test_02(self):
        driver = self.driver
        self.driver.find_element_by_id('lst-ib')
        self.driver.send_keys('java')
        self.driver.refresh()
        self.driver.send_keys(Keys.ENTER)
        time.sleep(2)

        titles = self.driver.find_element_by_class_name('r')
        for title in titles:
            assert 'java' in title.text.lower()

    def TearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()

