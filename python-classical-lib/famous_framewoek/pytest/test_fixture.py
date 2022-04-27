# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def login():
    print("\n执行登录")
    return ('tom', '123')


@pytest.fixture()
def operate():
    print("\n登陆后的操作")


@pytest.fixture(scope="session")  # session > module > class > function
def boring_func():
    print("\nThis is boring func")


def test_case1(login, operate):
    print(login)
    print("\ntest_case1，需要登陆")


def test_case2(boring_func):
    print("\ntest_case2, 不需要登陆")


def test_case3(login):
    print('\n'+str(login))
    print("\ntest_case3, 需要登陆")


# TODO 对于希望全局使用的函数，可以放在conftest.py里
"""
注意事项：
    1. conftest.py具有唯一性
    2. 在根目录下或是某一个package下面运行，作用范围也因此不同
        
"""
