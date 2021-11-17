class A(object):
    def __init__(self) -> None:
        super().__init__()

    def __new__(cls):
        return super().__new__(cls)


a = A()
