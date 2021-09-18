
    整个文档是一个文档节点
    每个 HTML 元素是元素节点
    HTML 元素内的文本是文本节点
    每个 HTML 属性是属性节点
    注释是注释节点


import bs4
#建立bs对象
bs = bs4.beautifulsoup(res)   #bs对象可以直接按标准格式输出整个html文档

bs.title表示输出第一个title标签
	进一步可以知道该标签的一些信息，比如：·父节点 bs.title.parent,
					      ·节点标签的名字(最外层) bs.title.name
					      ·文本内容(末端节点才有)  bs.title.string
					      ·查询其中的属性 bs.p['class']

获得所有某一类标签：              bs.find_all('a')   ·ps:如果有同类标签嵌套，会重复嵌进去的节点
获得所有某一类属性：              bs.find(id='zxc')  ·find_all 与 find 的区别？
获得某一节点的属性(不包括子节点): element.get('href')

获取所有文档节点
bs.get_text()


·bs的css选择器
bs.select(selector)
selector:
	·"title"		查找html文件里的标签，返回所有以title为标签的节点组成的列表
	·"html head title"     查找在html->head里的所有以title为标签的节点
	·"head > title"	注意有空格，查找head子节点（一级子标签？还是所有？答:一级，并且第一个tag必须是，且后面的不能中断）
	·"#link"		查找有id='link'的最内层节点
	·".sister"		查找class='sister'
	·"a[href]"		查找含有href属性的a标签

	·"#link + .sister"	查找所有紧接着id为link1元素之后的class为sister的元素的节点
	·"p + ul"		查找在标签p后面的ul标签
	·"#link1,#link2"	并列查询用，隔开
	

	·"a[href='http……']"  绝对匹配，等号前加^表示从前匹配，加$表示从后，加*表示从整体中匹配
#################
	·也可以用"[name='wd']" 其中wd前后的引号可要可不要
	·标签与属性的联用"span.bg"

#总的来说，空格表示子父结构，进一步查找####### ","表示并列查找 ###### '+'表示(同级?)先后
#多个属性  a[#cc][.fes]

结果分析：如果返回结果有多个，是按从前到后的查找顺序，按找到的时间先后顺序排列的

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .
tag可以理解为一种标签夹着的文本，它们有.name与attrs属性，同时相当于一个字典，存折的事属性key:value






	