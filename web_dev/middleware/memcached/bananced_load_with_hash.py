# -*- coding: utf-8 -*-
import hashlib
import random
import os

main_dir = os.path.dirname(os.path.abspath(__file__))
word_path = os.path.join(main_dir, "../../my_heap/words")

def alpha_shard(word):
    """Using poor job of assigning data to servers by using first letters."""
    if word[0] < 'g':       # abcdef
        return 'server0'
    if word[1] < 'n':       # ghijklm
        return 'server1'
    if word[2] < 't':       # nopqrs
        return 'server2'
    else:                   # tuvwxyz
        return 'server3'


def hash_shard(word):
    """Using python built-in hash() function """
    return "server%d" % (hash(word) % 4) # TODO why % 4

def md5_shard(word):
    data = word.encode("utf-8")
    return "server%d" % (hashlib.md5(data).digest()[-1] % 4) # TODO why % 4

def get_words(num=20000, path=word_path):
    with open(path, "w") as f_obj:
        while num:
            array = []
            for i in range(8):
                array.append(chr(random.randint(ord('a'), ord('z'))))
            array.append("\n")
            f_obj.write("".join(array))
            num-=1
    

    

if __name__ == "__main__":
    if not os.path.exists(word_path):
        get_words()
    words = open(word_path).read().split()
    for function in alpha_shard, hash_shard, md5_shard:
        d = {"server0": 0, "server1": 0, "server2": 0, "server3": 0}
        for word in words:
            d[function(word.lower())] += 1
        print(function.__name__[:-6])
        for key, value in sorted(d.items()):
            print(" {} {} {:.4}".format(key, value, value / len(words)))

"""
TODO hashlib和hash对竟然能将这些值散列的如此均匀,很好奇如何做到的
"""
"""
所以, 当想存一个字段的时候, 需要用一种均匀的算法根据字段名帮它分配一个server
然后,将这个值存入, 假设是memcahed
当想要再拿出来时, 就用相同的算法找到对应的server,然后过去值
"""