class Tasks(object):
    def __init__(self) -> None:
        self.tasks = [1, 2, 3, 4]

    def __iter__(self):
        for i in self.tasks:
            yield i


t = Tasks()
for i in t:
    print(i)
