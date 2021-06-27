'''
模块级（setup_module/teardown_module）开始于模块始末，全局的
函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
类级（setup_class/teardown_clas）只在类前后运行一次（在类中）
方法级（setup_method/teardown_method）开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
'''

import pytest

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')

def test1():
    print('test1')

def test2():
    print('test2')

if __name__ == '__main__':
    pytest.main(['test_08_setup_module.py','-sv'])