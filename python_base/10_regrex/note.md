import re
re.match(pattern,string,flags=0)	#从起始位置匹配，没有返回None，flags为修饰符，存在则返回一个对形象

也可以写成
pattern = re.compile(represent)
res = pattern.match(content)

re.search(pattern,s,flags=0)			#扫描整个字段返回第一个匹配到的字段
匹配结果可用的方法：
	span()获取匹配到的结果在原字符串中的跨度（返回一个表示起始的元组）
	group()匹配形式中的每一个括号表示一个小组，如果不输入参数，返回匹配到的字段，如果输入小组编号，则返回小组字段

如果没有匹配到返回的对象使用group()后是空值

re.sub(pattern,repl,string,count=0,flags=0)	repl是替代的字符串也可以是函数，count指最大替换次数，0表示所有

def double(matched):
    value = int(matched.group('value'))#注意
    return str(value * 2)			#结尾还需要以字符串形式返回

匿名函数用法
add_bold_tag = lambda matched:'<%s><%s>%s</%s>%s%s</%s>' \
           %(self.paras_tag, self.bold, matched.group(1), self.bold, matched.group(2), matched.group(3), self.paras_tag)
s = 'A23G4HFD567'


##########注意，这个替换的目标是matched.group()
print(re.sub('(?P<value>\d+)', double, s))		#将每个匹配到的数字乘以2返回

re.subn可以统计次数

		##如果没有匹配到返回整个字段

####自引用######
(?P<name>内容)

####通过\g<name>方式引用之前匹配的内容####

re.findall(pattern,string,flags=0)		搜索所有匹配到的字串（彼此不重叠）并以列表形式返回

#######不匹配某个单词###############
target = r'<strong>(.+?)</strong><((?:(?!strong).)[^>]+?)>'#用来匹配多个strong并列，并且连续

不匹配某个单词，并且多条件并列直接连在一起写就可以了

######################

贪婪匹配：匹配到的字符最长（系统默认）
懒惰匹配：匹配到的字符最短

表现形式

贪婪型		懒惰型
  *		  *?
  +		  +?
  ?		  ??
 {n,}		 {n,}?


Re.I	忽略大小写区别
Re.M	跨行匹配
Re.S	圆点.可以匹配除换行符之外的所有字符
Re.U	匹配Unicode字符集，将影响\w,\W,\B,\b,\s,\S字符类的匹配结果
Re.X	忽略正则表达式中除了方括号和被反斜杠转义以外的所有空白字符

1 .通配符（需要转义）                                       x,y = y,x
'.'：可以代表除换行符（\n,\r）以外的任意一字符
'+'：。。。。。。。1次或者多次，等同{1,}
'*'：前面的内容匹配0次或者任意多次，等同{0,}
'?'：。。。。。。。0次或者1次，等同{0,1}

'|'表示并列，匹配A或B，一般需要用(A|B)不然出现歧义

'(...)'

		+，*，?具有对前面的字段具有粘性，也就是说，前面的字段没有括号()或[]隔开均会当作一个整体

表示除\n以外的任意字符---在+或者*后面加？表示懒惰
2 .元字符（还包括）（需要加\转义）
^  _  $  \  |  @  []  {}  ()

3 .字符集（其中任意字符都失去特殊性）：
[]匹配括号内的任意一个
[abcd] 任意一个
[a-z]任意一个小写
[0-9]任意一个数字
[A-Za-z0-9]英文数字任一
[^abc]非abc之外任一
等价
\d（数字）  \w（字母数字下划线）  \s(单个空格)  \D（非数字相当于[^\d]）  \W（非字符）  \S（非空格）

\A从字符串开始匹配
\Z从字符串结尾匹配
\b一个单词的开头或者结尾（\b匹配这样的位置：它的前一个字符和后一个字符不全是(一个是,一个不是或不存在)\w（匹配字母或数字或下划线或汉字）”）
\1必须与小括号配合使用

4 .选择与分组
'(fr|b|f|cl)og'
分组可以理解为将匹配到的一部分内容（括号内的）返回
对应可以用groups与group（组别，缺省默认为0），对应的star\end（组别）给出组别在整个所匹配字符串中的位置
groups()以元组返回matchobj匹配内容中的组，group（0）返回所有匹配内容
(?p<name>表达式)，可以以group('name')的方式获得匹配结果

5. 指定次数
｛｝
flag:标志位，是否区分大小写（re.IGNORECASE），多行匹配等

'x{5,10}'5-10次
'x{3,}'3次及以上
'x{3}'3次

6.位置锚点
 ^ 表示只从首段匹配
'^http'

 $ 表示只从尾端匹配
'rock$'


7.反向引用
&n匹配已经匹配的内容

		汉字域[\u4e00-\u9f5a]不包括中文标点

7.正则表达式中引入变量
r''+变量+''


########################################模块一章遇到的问题：
模式和查找的字符串可以为8位字符串（ASCII码）或者unicode字串吗？
[-0-9]是否为合法字符集



re.sub(pattern,repl,flags)
函数应用实例
#!/usr/bin/python3
import re
 
phone = "2004-959-559 # 这是一个电话号码"
 

#!/usr/bin/python
 
import re
 
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
注：这里处于repl位置的函数，只需要输入函数名，不用加（）
  应为参数默认为是前面的匹配对象，所以函数内的参数引用可以使用撇陪对象的内置方法

findall(pattern,str,pos_num,pos_num)可以指定起始位置

单词边界\b
str1='i love python '
str2=re.findall(r'\bon',str1)
str3=re.findall(r'on\b',str1)
print(str2)
print(str3)

