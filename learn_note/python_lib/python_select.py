import select
for i in dir(select):
    if i.startswith("EPOLL"):
        num = getattr(select, i)
        print("%s ---> %d ----> %s" % (i, num, bin(num)[2:]))