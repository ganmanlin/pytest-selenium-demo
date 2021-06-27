from selenium import webdriver
from time import sleep
import os

# 13 | 掌握checkbox和radiobutton的定位技巧
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms2.html'
        print(file_path)
        self.driver.get(file_path)

    def test_checkbox(self):
        swimming = self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element_by_name('reading')
        if not reading.is_selected():
            reading.click()

        sleep(3)
        swimming.click()
        reading.click()
        sleep(5)

        self.driver.quit()

    def test_radio(self):
        list = self.driver.find_elements_by_name('gender')
        list[0].click()
        sleep(5)

        self.driver.quit()

if __name__ == '__main__':
    testcase = TestCase()
    # testcase.test_checkbox()
    testcase.test_radio()
