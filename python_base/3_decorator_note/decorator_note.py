def log(func):
    def _wrapper(*args, **kwargs):
        print(' '.join(map(str, args)))
        print(" ".join(["{key}: {value}".format(key=key, value=value)
              for key, value in kwargs.items()]))
        ret = func(*args, **kwargs)
        print(ret)
        return ret

    return _wrapper


def deep_log():
    def _wrapper(func):
        def __wrapper(*args, **kwargs):
            print(' '.join(map(str, args)))
            print(" ".join(["{key}: {value}".format(key=key, value=value)
                  for key, value in kwargs.items()]))
            ret = func(*args, **kwargs)
            print(ret)
            return ret

        return __wrapper
    return _wrapper


@log
def test(a, b):
    return a+b


test(1, 2)

"""
Conclusion:
    as seen in dynamically_change_attr.py,
    after compiling, the decorator has merged into the function
"""
