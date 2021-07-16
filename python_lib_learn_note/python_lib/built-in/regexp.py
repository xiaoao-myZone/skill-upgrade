import re


# 合格的ip
pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
print(pattern.search("127.0.0.1").group())
