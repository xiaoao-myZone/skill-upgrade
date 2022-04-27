# -*- coding: utf-8 -*-
import pytest


def setup_module():
    print("\nsetup_module, 只执行一次，但有多个测试类的时候使用")


def teardown_module():
    print("\nteardown_module, 只执行一次，当有多个测试类的时候使用")


class TestPytest1(object):

    @classmethod
    def setup_class(cls):
        print("\n**steup_class1, 只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\n**teardown_class1, 只执行一次")

    def setup_method(self):
        print("\nsetup_method1,每个测试方法都执行一次")

    def teardown_method(self):
        print("\nteardown_method1,每个测试方法都执行一次")

    @pytest.mark.run(order=2)
    def test_three(self):
        print("\ntest_three, 测试用例")

    @pytest.mark.run(order=1)
    def test_four(self):
        print("\ntest_four, 测试用例")


class TestPytest2(object):

    @classmethod
    def setup_class(cls):
        print("\n**steup_class2, 只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\n**teardown_class2, 只执行一次")

    def setup(self):  # def setup_method(self):
        print("\nsetup_method2,每个测试方法都执行一次")

    def teardown(self):  # def teardown_method(self):
        print("\nteardown_method2,每个测试方法都执行一次")

    def test_two(self):
        print("\ntest_two, 测试用例")

    def test_one(self):
        print("\ntest_one, 测试用例")
