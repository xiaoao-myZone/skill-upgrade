## essence of import
python程序执行时, 代码中的任何import都遵循如下优先次序:

1. 如果带from .pkg import obj, 则从包的次级目录下搜索pkg (存疑)
2. 从启动py程序的目录下搜索, 也即os.getcwd()返回的路径下搜索
3. 从sys.path的路径列表中依次搜索
4. ImportError

