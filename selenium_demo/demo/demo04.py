from selenium import webdriver
from time import sleep

# 11.掌握WebElement核心方法和属性的使用
# http://sahitest.com/demo
from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/linkTest.htm")

    def test_webElement_prop(self):
        e = self.driver.find_element_by_id('t1')
        e1 = WebElement;
        print(type(e))
        print(f"e.id :  {e.id}")
        print(f"e.tag_name :  {e.tag_name}")
        print(f"e.size :  {e.size}")
        print(f"e.rect :  {e.rect}")
        print(f"e.id :  {e.id}")
        print(f"e.text : {e.text}")
        self.driver.quit()

    def test_webElement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world!')
        sleep(2)

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('size'))

        e.value_of_css_property('font')
        e.value_of_css_property('color')
        sleep(2)
        e.clear()

        self.driver.quit()

    def test_webElement_method2(self):
        form_element = self.driver.find_element_by_xpath('/html/body/form[1]')
        e = form_element.find_element_by_id('t1').send_keys('selenium')

        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_webElement_prop()
    # case.test_webElement_method()
    case.test_webElement_method2()
