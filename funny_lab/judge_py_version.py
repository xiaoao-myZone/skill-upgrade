import sys
info = sys.version_info
for i in dir(info):
    if not i.startswith("__"):
        value = getattr(info, i)
        print("%s | %s | %s" % (i, value, type(value)))