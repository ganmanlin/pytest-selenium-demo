from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


# 14. select 下拉列表定位
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/forms3.html'
        print(file_path)
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element_by_id('province')
        select = Select(se)
        select.select_by_index(2)

        sleep(2)
        select.select_by_value('bj')
        #
        # sleep(2)
        # select.select_by_visible_text('TianJing')

        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(3)
        #
        # select.deselect_all()
        # sleep(3)

        # for option in select.options:
        #     print(option.text)

        # for option in select.all_selected_options:
        #     print(option.text)

        print(select.first_selected_option.text)

        self.driver.quit()
        #
        # sleep(2)


if __name__ == '__main__':
    testcase = TestCase()
    testcase.test_select()
