'''
在pytest中，也可以使用参数化测试，即没组参数都独立执行一次测试。
使用的工具就是pytest.mark.parametrize(argument,argvalues)

username, password
1. admin xxx
2. xxx 123
3. admin 123
4. xxx xxx

实例
import pytest

#列表
data = ['123','456']

@pytest.mark.parametrize('pwd',data)
def test1(pwd)
    print(pwd)

#元组
data2=[(1,2,3), #或则[1,2,3]
        (4,5,6),  #或则[4,5,6]]
@pytest.mark.parametrize('pwd',data)
def test2(pwd)
    print(pwd)
'''

import pytest

# 列表
data = ['123', '456']


@pytest.mark.parametrize('pwd', data)
def test1(pwd):
    # print('hello')
    print(pwd)


data2 = [(1, 2, 3),  # 或则[1,2,3]
         (4, 5, 6)  # 或则[4,5,6]
         ]


@pytest.mark.parametrize('a,b,c', data)
def test2(a, b, c):
    print(a, b, c)


data3 = (
    {'user': 'admin',
     'pwd': 'xxx'},
    {'user': 'xxx',
     'pwd': '123'},
    {'user': 'admin',
     'pwd': '123'},
    {'user': 'xxx',
     'pwd': 'xxx'})


@pytest.mark.parametrize('dic', data3)
def test3(dic):
    print(dic['user'])
    print(dic['pwd'])
    print(dic)


data4 = [
    pytest.param(1, 2, 3, id="(a+b):pass"),  # id的值可以自定义，只要方便理解用例是干什么的即可
    pytest.param(5, 5, 10, id="(a+b):pass")
]


def add(a, b):
    return a + b


class TestParametrize(object):
    @pytest.mark.parametrize('a,b,expect', data4)
    def test_parametrize_1(self, a, b, expect):
        assert add(a, b) == expect


if __name__ == '__main__':
    pytest.main(['-vs', 'test_05.py'])
