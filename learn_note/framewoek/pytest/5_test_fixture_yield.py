import pytest

@pytest.fixture(scope="module")
def open():
    print("\n打开浏览器")
    yield 1
    print("\n执行teardown !")
    print("最后关闭浏览器")


@pytest.mark.usefixtures("open")
def test_search1():
    print("\ntest_search1")
    raise NameError

def test_search2():
    print("\ntest_search2")

def test_search3():
    print("\ntest_search3")


class TestClass(object):
    def test_1(self,open):
        print("open return is %s" %str(open))
        print("\nTestClass::test_1, 测试用例")

    def test_2(self, open):
        print("open return is %s" %str(open))
        print("\nTestClass::test_2, 测试用例")
