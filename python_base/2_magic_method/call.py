class Test(object):
    def __init__(self) -> None:
        pass

    def __call__(self):
        return 3


t = Test()
print(t())
