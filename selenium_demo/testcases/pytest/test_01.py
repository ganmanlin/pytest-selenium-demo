import pytest


class TestLoginCase(object):
    # def __init__(self):

    def test01(self):
        print("test01")
        assert 1 == 1

    def test02(self):
        print("test02")
        assert 1 == 2

if __name__ == '__main__':
    pytest.main(['-vs', 'test_01.py'])
