from queue import LifoQueue
from random import shuffle
AROUND = [(0,1), (-1, 0), (0,-1), (1,0)]
shuffle(AROUND)
print(AROUND)
MAZE = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 1, 0, 0, 0, 1, 0, 1),
    (1, 0, 0, 1, 0, 0, 0, 1, 0, 1),
    (1, 0, 0, 0, 0, 1, 1, 0, 0, 1),
    (1, 0, 1, 1, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 1),
    (1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
    (1, 0, 1, 1, 1, 0, 1, 1, 0, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

class MazePoint(object):
    def __init__(self, x, y, maze, ori):
        self._x = x
        self._y = y
        self.ori = self.reverse_ori(ori)#latest point
        self.maze = maze
        self.branch=LifoQueue(4)
        self.search()
    
    def search(self):
        for index, ori in enumerate(AROUND):
            x = self._x + ori[0]
            y = self._y + ori[1]
            if not self.maze[y][x] and self.ori!=ori:
                self.branch.put_nowait(index)
    
    def reverse_ori(self, ori):
        ori = list(ori)
        for index, i in enumerate(ori):
            if i != 0:
                ori[index] = -i
        ori = tuple(ori)
        return ori

    def is_dead(self):
        return self.branch.empty()
    
    def next_point(self):
        index = self.branch.get_nowait()
        ori = AROUND[index]
        x = self._x + ori[0]
        y = self._y + ori[1]
        return MazePoint(x, y, self.maze, ori)

    def __eq__(self, other):
        if self._x==other._x and self._y==other._y:
            return True
        else:
            return False
    
    def print_point(self):
        ori = self.reverse_ori(self.ori)
        index = AROUND.index(ori)
        if index==0:
            print("up: (%d, %d)" %(self._x, self._y))
        elif index==1:
            print("right: (%d, %d)" %(self._x, self._y))
        elif index==2:
            print("down: (%d, %d)" %(self._x, self._y))
        else:
            print("left: (%d, %d)" %(self._x, self._y))


start_point = MazePoint(1, 1, MAZE, (0, 1))
end_point = MazePoint(8, 8, MAZE, (1, 0))
def search_path(start_point, end_point):
    tmp = start_point
    path = LifoQueue(81)
    while tmp!=end_point:
        path.put_nowait(tmp)
        print("in: (%d %d)" % (tmp._x, tmp._y))
        yield (1, tmp._x, tmp._y)
        if not tmp.is_dead():
            tmp = tmp.next_point()
        else:
            tmp = path.get_nowait()
            if path.empty():
                break
                #return []
            else:
                while not path.empty():
                    tmp = path.get_nowait()
                    print("out: (%d %d)" % (tmp._x, tmp._y))
                    yield (0, tmp._x, tmp._y)
                    if not tmp.is_dead():
                        break
                else:
                    break
                    #return []
    else:
        path.put_nowait(tmp)
        print("in: (%d %d)" % (tmp._x, tmp._y))
        yield (1, tmp._x, tmp._y)

    # ret = []
    # while not path.empty():
    #     ret.append(path.get_nowait())

    # ret.reverse()
    # return ret

# ret = search_path(start_point, end_point)
# for i in ret:
#     i.print_point()
if __name__ == "__main__":
    iter_obj = search_path(start_point, end_point)
    try:
        while True:
            next(iter_obj)
    except:
        pass