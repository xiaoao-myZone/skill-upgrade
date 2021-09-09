import sys
# from io import TextIOWrapper


print(sys.stdout)
print(sys.stdin)
txt = sys.stdin.readline()
print("receive: %s" % txt)  # as same as input
