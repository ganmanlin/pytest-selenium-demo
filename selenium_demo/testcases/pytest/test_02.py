import pytest

class TestCase02(object):
    def test01(self):
        print('test01')

    def add(self):
        print("add")

    def test02(self):
        print('test02')

if __name__ == '__main__':
    pytest.main(['test_02.py'])