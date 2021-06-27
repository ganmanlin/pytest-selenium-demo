import pytest


class Test04(object):
    @pytest.mark.do
    def test1(self):
        print('test1')

    @pytest.mark.undo
    def test2(self):
        print('test2')

if __name__ == '__main__':
    pytest.main('-m do',['test_04.py'])
