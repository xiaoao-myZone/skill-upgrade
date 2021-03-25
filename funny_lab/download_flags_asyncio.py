import asyncio
import aiohttp

BASE_URL = "https://www.baid.com"
@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.git'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.requset("GET", url) # 不能用request库吗
    image = yield from resp.read()
    return image

@asyncio.coroutine
def download_one(cc):
    image = yield from getattr(cc)
    #show(cc)
    #save_flag(image, cc.lower()+'.gif')
    return cc

@asyncio.coroutine
def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do) #接受一串协程风格函数
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)