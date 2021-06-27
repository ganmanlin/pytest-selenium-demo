from selenium import webdriver
from time import sleep


# 10. selenium webdriver常用的属性和方法
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        self.driver.back()
        sleep(3)
        self.driver.refresh()
        sleep(3)
        self.driver.forward()
        self.driver.close()  # 只关闭当前窗口
        self.driver.quit()  # 关闭浏览器，结束当前进程

    def test_windows(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_windows()
