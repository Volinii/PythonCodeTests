import time


def timer(func, *args):
    start = time.clock()  # 开始计时
    for i in range(1000):
        func(*args)
    return time.clock()-start  # 计算差值

print(timer(str.upper, 'spam'))
