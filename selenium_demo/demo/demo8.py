from selenium import webdriver
from time import sleep
import os

#15. 弹框处理：掌握alert、confirm、prompt三种弹框的用法
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/test_alert.html'
        print(file_path)
        self.driver.get(file_path)
        # self.driver.get("http://sahitest.com/demo/alertTest.htm")

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        # 切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()
        self.driver.quit()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        # 切换到alert
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        # confirm.accept()
        confirm.dismiss()
        self.driver.quit()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        # 切换到alert
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.send_keys("小花")
        prompt.accept()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
