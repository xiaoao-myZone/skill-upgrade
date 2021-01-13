## debug experience
1. 忘记return
2. 注意变量名的直观与简洁
3. vscode的自动补全
4. 可变变量直接赋值地址会改变



## not often package usage
1. io
&#160;
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
&#160;
`json.dump或dumps会将int类型的key转化为str `
`yaml.dump或safe_dump可以避免这个问题,但是会残缺一个{`

2. os
&#160;
`os.path.isfile()需要输入绝对路径`
&#160;
`os.mkdir只能创建最后一级子目录，若要创建多级目录用os.makedirs`

&#160;
3. threading
> &emsp;主进程结束，子线程也结束

> &emsp;当调用函数只有一个参数时

`thread = threading.Tread(target=func, args=(a, ))`

> &emsp;使用Queue.get线程出现异常,Queue在调用get方法所加的锁会自动释放,但是threading.Lock的acquire不行

4. wrapper
> &emsp;用线程启用一个带装饰器的函数(装饰器带try except), 如果装饰器中中处理except部分没有打印错误信息,该函数中的报错不会被自动打印到终端

## import
1. 当导入一个包中的一个模块的时候，如果这个模块也导入了这个包中的另一个模块，并且导入时没有加包名，会报错
2. 当一个包中的模块想导入与这个包并列的包的时候， 它必须要是一个包，也就是需要有__init__.py
3. 包的导入比较鸡肋，比如你运行一个文件夹内的一个py文件，它只会在这个目录下一级文件中搜索你自己建立的包

## green thread
eventlet 会讲Queue改写成轻量版,没有mutex方法

## queer

1. 使用`dict_a[str(an_id)]`, an_id在什么情况下会自动由int转化为str

## something worth concentration
1. api name can't change for some rediculous reason (such as, let the mistake go)
2. even raise Exception, better to logger it before raising it
3. if a status logging file is import, it's better to save it every time changing it
4. go straight to resolve a problem and then to consider making it look more beautiful or less stupid
5. You can't code dazedly, or you will use much more time to debug

## wrapper
1. 调用装饰器没有加`@`
2. 定义装饰器没有加`return __wrapper`

