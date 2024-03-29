## debug experience
1. 忘记return
2. 注意变量名的直观与简洁
3. vscode的自动补全
4. 可变变量直接赋值地址会改变
5. list_obj.sort()返回None



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

> &emsp;当调用函数只有一个参数时,原因是当()不加","时,python编译器会认为这是一个优先运算标志,而不是一个元组

`thread = threading.Tread(target=func, args=(a, ))`

> &emsp;使用Queue.get线程出现异常,Queue在调用get方法所加的锁会自动释放,但是threading.Lock的acquire不行

> &emsp;使用带lock的装饰器后，不能实现递归

4. wrapper
> &emsp;用线程启用一个带装饰器的函数(装饰器带try except), 如果装饰器中中处理except部分没有打印错误信息,该函数中的报错不会被自动打印到终端

> &emsp;装饰器莫忘记返回wrapper

> &emsp;不能用ipdb.set_trace

## import
1. 当导入一个包中的一个模块的时候，如果这个模块也导入了这个包中的另一个模块，并且导入时没有加包名，会报错
2. 当一个包中的模块想导入与这个包并列的包的时候， 它必须要是一个包，也就是需要有__init__.py(这不是本质)
3. 包的导入比较鸡肋，比如你运行一个文件夹内的一个py文件，它只会在这个目录下一级文件中搜索你自己建立的包
4. 包中的模块导入只能是当前模块目录(from .test import Test)或者运行目录(python test.py所在的目录)或者系统目录
5. `from decorator import decorator`， 极有可能是os.get_cwd()目录下存在一个decorator.py文件

6. import的搜索顺序: 1. 所运行的py文件所在的目录 2. 环境变量中的目录

## thread
1. eventlet 会讲Queue改写成轻量版,没有mutex方法
2. 线程中的打印信息一般都会出现在终端,有些没有报错的情况下莫名其妙消失,可能是用try-except捕捉了

## queer

1. 使用`dict_a[str(an_id)]`, an_id在什么情况下会自动由int转化为str, 使用json.dump(s)的时候，json不接受int作为map的键

## something worth concentration
1. api name can't change for some ridiculous reason (such as, let the mistake go)
2. even raise Exception, better to logger it before raising it
3. if a status logging file is import, it's better to save it every time changing it
4. go straight to resolve a problem and then to consider making it look more beautiful or less stupid
5. You can't code dazedly, or you will use much more time to debug

## wrapper
1. 调用装饰器没有加`@`
2. 定义装饰器没有加`return __wrapper`

## annotation
1. On Python ≥ 3.6, :class:`WebSocketCommonProtocol` instances support


## str
1. `{:.4f}.format(1.2)`可以限定输出的小数位数
2. 当一个可序列化对象中存在两种编码方式， 使用json.dumps时会报错, 比如`{"a": u"fddd", "b": "ttt"}` (存疑)


## list
1. `a = [1,2,3,4,5]; a[::2] = [8,8,8]`a的结果为`[8,2,8,4,8]`
2. `a[100:]`即便a的长度小于100, 超范围分片并不会报错, 只会尽力返回所输入的分片中存在的部分
3. `a = [1,2,0]; a[-1] += a.pop() + 100` a为`[1, 100]` 而不是 `[1, 102]`, 实际做出的运算是`a[-2] = a[-1]*2 + 100; del a[-1]`
4. 以上可以改为 `a[-1] = a.pop() + 100 + a[-1]`, 这说明python是从左往右运算的, 但应该与解释器有关, 存在从右往左的运算的解释器吗
5. 对python3， 可以使用 `m, *n = 1,2,3,4,5`或者`m, *n = (1,2,3,4,5)`或者`m, *n = [1,2,3,4,5]`， 但是python2不行

## tuple

1. `a = (1, [1,2]); a[1].append(1)`没有问题, 但是`a[1] += [1]`会报错， 但其实是修改成功了

### class
1. 类中的一级缩进的内容会在编译的时候执行, 并可以通过self调用
```
class Test:
    name = 'Lucus'
    def self_intro(self):
        print("My name is %d" % self.name)
```
2. TODO
### function

函数中需要输入一系列可迭代参数时，前面加*，比如(*'MJPG')，相当于输入('M','J','P','G')

### GIL
[python中的GIL详解](https://www.cnblogs.com/SuKiWX/p/8804974.html)
问题1: 既然线程之间的切换是根据每个线程运行的微指令， 那么在众多线程在进行IO等待时， 直觉上没有微指令执行， 
    那岂不是获取GIL的线程在IO等待没有结束前是不可能让渡GIL, 但是现实情况不是这样， 要么IO等待存在微指令， 
    要么这个帖子中的描述不准确 TODO


### metaclass

## pip
1. 获取配置
`pip config list`
2. 获取某一个配置
`pip config get global.index-url`
3. 修改某个配置
`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
4. 取消某个配置(回复默认设置)
`pip config unset global.index-url`
5. 其他pip config 操作 debug, edit, get, list, set, unset
6. ultimate set
`vim ~/.pip/pip.conf`
7. install
`pip install -r requirements.txt`
8. resintall
`pip install --force--reinstall pkg`
9. temperary add time out
`pip install pkg --timeout 60`