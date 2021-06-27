from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium')
sleep(1)
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

def test():
    # import subprocess
    # p = subprocess.Popen("chromedriver")
    # p.communicate()
    case = TestCase()
    case.test()

if __name__ == '__main__':
    test()