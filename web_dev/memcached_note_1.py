#-*- coding: utf-8 -*-
import memcache, random, time, timeit

def compute_square(mc, n):
    value = mc.get('sq:%d' %n)
    if value is None:
        time.sleep(0.001)
        value = n * n
        mc.set('sq:%d' % n, value, time=30) #使用pickle转化python对象
    return value

def main():
    mc = memcache.Client(['127.0.0.1:11211'])

    def make_request():
        compute_square(mc, random.randint(0, 5000))
    
    print("Ten successive runs: ")
    for i in range(1, 11):
        print('%.2f' % timeit.timeit(make_request, number=2000), end=' ', flush=True)
    print("")

    #2.86 2.89 2.92 2.92 2.90 2.89 2.91 2.89 2.92 2.93
    #结果并没有出现明显优化的迹象
    #神坑, 没有配置memcahce
    # 让我想到fluent python里面的一个装饰器

if __name__ == '__main__':
    main()

"""
GE3DCNRWGYYTANZXFR4GSYLPMFXS2SCQFR4GSYLPMFXSYMJTHEXDEMRXF.YZDKLRRGM4SYL3IN5WWKL3YNFQW6YLPF4XGY33DMFWC63DJMIXXA6LUNB.XW4MZOGUXXG2LUMUWXAYLDNNQWOZLTF5WWK3LDMFRWQZLEF5PV62LONF2.F6XZOOB4Q0000.d372fc0.testpcurl.com
Traceback (most recent call last):
  File "/home/xiaoao/xiaoao/skill-upgrade/web_dev/memcached_note_1.py", line 23, in <module>
    main()
  File "/home/xiaoao/xiaoao/skill-upgrade/web_dev/memcached_note_1.py", line 13, in main
    mc = memcached.Client(['127.0.0.1:11211'])
AttributeError: module 'memcached' has no attribute 'Client'

将pip install python3-memcached 错写成 pip install memcached
将import memcahe 错写成 import memcached

sudo apt-get install memcached
sudo memcached -d -m 128 -p 11211 -u root -c 1024 -l 127.0.0.1 -P /tmp/memcache.pid -s /tmp/memcached.sock
ps -ef | grep memcache
"""