import pytest


class Test06(object):
    @pytest.fixture()
    def init(self):
        print('init...')
        return 1

    def test1(self, init):
        print('test1')

    def test2(self, init):
        print('test2')


if __name__ == '__main__':
    pytest.main(['-sv', 'test_06.py'])
