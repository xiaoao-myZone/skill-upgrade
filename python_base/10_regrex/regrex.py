import re

# match
string = "22766cvb"
pattern = r'\d+'
# 只能从头开始匹配
print(f"[1]: {re.match(pattern, string).group()=}")
# 也可以写为
pattern = re.compile(pattern)
res = pattern.match(string)
print(f"[2]: {res.group()=}  {res.span()=}")

# search
pattern = re.compile(r"\D{1}")
print(f"[3]: {pattern.match(string)=}")
# 扫描整个字段返回第一个匹配到的字段, 如果没有res为None
print(f"[4]: {pattern.search(string).group()=}")

# findall
# 搜索所有匹配到的字串（彼此不重叠）并以列表形式返回
print(f"[5]: {pattern.findall(string, 0, 100)=}")

# sub
print(f"[6]: {pattern.sub('*', string, count=2)=}")

# subn
# 可以统计次数
print(f"[7]: {pattern.subn('*', string, count=2)=}")
# pattern = re.compile(r"\D{10}")
# print(f"[8]: {pattern.subn('*', string, count=2)=}")
# 没有匹配res[1]==0

# 顾名思义
pattern.finditer
pattern.fullmatch


# 高级用法
def double(matched):
    value = int(matched.group('value'))  # 注意
    return str(value * 2)  # 结尾还需要以字符串形式返回


# 将每个匹配到的数字乘以2返回, 注意，这个替换的目标是matched.group()
print(re.sub(r'(?P<value>\d+)', double, "aaa50bbb"))

# add_bold_tag = lambda matched: '<%s><%s>%s</%s>%s%s</%s>' % (
#     self.paras_tag, self.bold, matched.group(1), self.bold,
#     matched.group(2), matched.group(3), self.paras_tag)
