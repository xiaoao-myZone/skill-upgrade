"""
1. 客户端提供一个范围，与正确答案， 服务端需要去猜测这个答案

"""
import math
import random
import asyncio
import contextlib


class EOFError(Exception):
    pass


class AsyncConnectionBase:
    def __init__(self, reader, writer) -> None:
        self.reader = reader
        self.writer = writer

    async def send(self, commad):
        line = commad + '\n'
        data = line.encode()
        self.writer.write(data)
        await self.writer.drain()

    async def receive(self):
        line = await self.reader.readline()
        if not line:  # line会是什么
            raise EOFError("Connection closed")
        return line[:-1].decode()


WARMER = 'Warmer'
COLDER = 'Colder'
UNSURE = 'Unsure'
CORRECT = 'Correct'


class UnknownCommandError(Exception):
    pass


class AsyncSession(AsyncConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_value(None, None)

    def _clear_value(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []

    async def loop(self):
        while command := await self.receive():
            print(command)
            parts = command.split(' ')
            if parts[0] == 'PARAMS':
                self.set_params(parts)
            elif parts[0] == 'NUMBER':
                await self.send_number()
            elif parts[0] == 'REPORT':
                self.receive_report(parts)
            else:
                raise UnknownCommandError(command)

    def set_params(self, parts):
        assert len(parts) == 3
        lower = int(parts[1])
        upper = int(parts[2])
        self._clear_value(lower, upper)

    def next_guess(self):
        if self.secret is not None:
            return self.secret

        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess

    async def send_number(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        await self.send(format(guess))  # TODO format? 和str输出有何区别？

    def receive_report(self, parts):
        assert len(parts) == 2
        decision = parts[1]

        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last

        print(f'Server: {last} is {decision}')

    def close_session(self):
        print(dir(self.reader))
        # self.reader.close()
        self.writer.close()


class AsyncClient(AsyncConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state()

    def _clear_state(self):
        self.secret = None
        self.last_distance = None

    @contextlib.asynccontextmanager  # 有何意义？可以使用with
    async def session(self, lower, upper, secret):
        print(
            f'Guess a number between {lower} and {upper}!'
            f' Shhhhh, it\'s {secret}.')

        self.secret = secret
        await self.send(f'PARAMS {lower} {upper}')
        try:
            yield
        except Exception:
            import traceback
            traceback.print_exc()
        finally:
            self._clear_state()
            await self.send('PARAMS 0 -1')

    async def request_numbers(self, count):
        for _ in range(count):
            await self.send('NUMBER')
            data = await self.receive()
            yield int(data)
            if self.last_distance == 0:
                return

    async def report_outcome(self, number):
        new_distance = math.fabs(number - self.secret)
        decision = UNSURE

        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            pass
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER
        self.last_distance = new_distance

        await self.send(f'REPORT {decision}')
        return decision


async def handle_async_connection(reader, writer):
    session = AsyncSession(reader, writer)
    try:
        await session.loop()
    except EOFError:
        # TODO 什么时候会发生EOF异常呢？ 当客户端关闭
        print("client close")
    finally:
        session.close_session()


async def run_async_server(address):
    server = await asyncio.start_server(
        handle_async_connection, *address)
    # 也就是说asyncio.start_server会根据addr创建一个reader与writer
    # 给前面的句柄函数
    # 生成的server对象与被@contextlib.asynccontextmanager修饰过的函数一样
    async with server:
        await server.serve_forever()
    # 这样可以在服务器异常关闭后， 自动关闭socket


async def run_async_client(address):
    streams = await asyncio.open_connection(*address)
    # stream 到底是个啥, reader&writer
    client = AsyncClient(*streams)

    async with client.session(1, 5, 3):
        results = [(x, await client.report_outcome(x))
                   async for x in client.request_numbers(5)]
    async with client.session(10, 15, 12):
        async for number in client.request_numbers(5):
            outcome = await client.report_outcome(number)
            results.append((number, outcome))

    _, writer = streams
    writer.close()
    await writer.wait_closed()
    return results


async def main_async():
    address = ('127.0.0.1', 12345)
    server = run_async_server(address)
    server_task = asyncio.create_task(server)
    # 由于server不一定在client前创建， 所以需要停顿等待server的建立
    await asyncio.sleep(0.1)
    print("yes")
    results = await run_async_client(address)
    for number, outcome in results:
        print(f'Client: {number} is {outcome}')
    await server_task


asyncio.run(main_async(), debug=True)

"""
Conclusion:
1. 在存在IO阻塞的方法前， 加上async， 在方法内具体阻塞的函数前加上await
2. contextlib.contextmanager需要用到对应的asynccontextmanager
3. async修饰的函数中， 可以用yield
4. 存在async与await的函数的方法被调用时需要用到await
5. TODO 猜想： async与await相当与python在编译时中需要做一些事情， 但是具体如何做？
6. 虽然await后函数由协程调度， 把await看做一个协程正式注册， 那么await asyncio.sleep(0.1)会阻塞之后的协程注册
7. TODO asyncio.run与loop.run_until_complete的区别？
"""
