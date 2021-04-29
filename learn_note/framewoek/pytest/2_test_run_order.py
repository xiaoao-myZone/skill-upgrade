import pytest

def test_single_func():
    print("\ntest_single_func, 测试用例")

class TestClass(object):

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("\ntest_two, 测试用例")

    @pytest.mark.run(order=3)
    def test_one(self):
        print("\test_one, 测试用例")

    @pytest.mark.run(order=1)
    def test_three(self):
        print("\ntest_three, 测试用例")