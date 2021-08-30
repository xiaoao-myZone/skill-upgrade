import re


# 合格的ip
pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
print(pattern.search("127.0.0.1").group())
test_samples = [
    "0.0.0.1",
    "ll52.445.215.22",
    "0.fd.354.122"
]
for i in test_samples:
    if pattern.search(i):
        print("%s  --> right")
    else:
        print("%s  --> wrong")