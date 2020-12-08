## debug experience
1. 忘记return
2. 注意变量名的直观与简洁
3. vscode的自动补全
4. 可变变量直接赋值地址会改变



## not often package usage
1. io
`file_obj = io.ByteIO()`
`file_obj.write(data) #data is byte type`
`file_obj.seek(0)`
`data = file_obj.read()`
&#160;
`# file_obj.write()可以读入数据但是只能用getvalue()方法来取值`
`# file_obj.read()貌似只能读取初始化时候输入的byte类型数据`
`# 真相大白，file_obj.write()后指针在最后面，需要file_obj.seek(0)才能获取用read()获取所有信息`
&#160;
`with open("/home/usr/test/sample.json", "w+") as file_obj`
`# 不可以在没有文件test的情况下创建文件`
&#160;
`json.loads与load会将str转化为unicode`
`yaml.safe_load可以避免这个问题`

2. os
`# os.path.isfile()需要输入绝对路径`

&#160;
3. threading
> &emsp;主进程结束，子线程也结束

> &emsp;当调用函数只有一个参数时

`thread = threading.Tread(target=func, args=(a, ))`

## import
1. 当导入一个包中的一个模块的时候，如果这个模块也导入了这个包中的另一个模块，并且导入时没有加包名，会报错
2. 当一个包中的模块想导入与这个包并列的包的时候， 它必须要是一个包，也就是需要有__init__.py
3. 包的导入比较鸡肋，比如你运行一个文件夹内的一个py文件，它只会在这个目录下一级文件中搜索你自己建立的包