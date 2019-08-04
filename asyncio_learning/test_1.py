import time
import asyncio
# 同步代码


def hello():
    time.sleep(1)
    print('hello world', time.time())


def run():
    for i in range(3):
        hello()
        print('hi')


async def hello_():
    asyncio.sleep(1)
    time.sleep(1)
    print('hello word', time.time())


def run_():
    print(time.time())
    for i in range(3):
        loop.run_until_complete(hello_())  # 阻塞执行

loop = asyncio.get_event_loop()

if __name__ == '__main__':
    run()
    print('*'*30)
    run_()
