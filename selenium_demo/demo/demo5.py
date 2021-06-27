from selenium import webdriver
from time import sleep
import os

#form表单：熟练掌握form表单操作步骤
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms.html'
        print(file_path)
        self.driver.get(file_path)

    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('admin')
        password = self.driver.find_element_by_id('pwd')
        password.send_keys('123')

        print(username.get_attribute('value'))
        print(password.get_attribute('value'))

        sleep(2)
        self.driver.find_element_by_id('submit').click()

        username.clear()
        password.clear()

        self.driver.quit()

    # def


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
