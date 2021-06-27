import pytest
import allure

@pytest.fixture(scope="session")
def login():
    print("用例先登陆")

@allure.step("步骤1：点xxx")
def step_1():
    print("111")

@allure.step("步骤2：点xxx")
def step_2():
    print("222")

@allure.feature("编辑页面")
class TestEditPage():
    '''编辑页面'''
    @allure.story('这是一个xxx的用例')
    def test_1(self,login):
        '''用力描述：先登录，再去执行xxx'''
        step_1()
        step_2()
        print('test_1')

    @allure.story('这是一个yyy的用力')
    def test_2(self,login):
        '''用力描述：先登录，再去执行yyy'''
        print('test_2')

# if __name__ == '__main__':
