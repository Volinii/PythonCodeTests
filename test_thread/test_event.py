import threading
from time import sleep
# Python的threading模块提供Event对象用于线程间通信，其内置了一个标识，初始值为False。
# 线程通过wait()方法进入等待状态，直到另一个线程调用set()方法将内置标识设置为True时，
# Event通知所有等待状态的线程恢复运行。
# 还可以通过isSet()方法查询Event对象内置标识的当前值。
# 1. 设置信号：set()
# 使用Event的set()方法可以设置Event对象内部的信号标识为True。
# 2. 查询信号： isSet()
# Event对象提供了isSet()方法来判断其内部信号标识的状态。
# 当使用Event对象的set()方法后，isSet()方法返回True。
# 3. 清除信号：clear()
# 使用Event对象的clear()方法可以清除Event对象内部的信号标识，即将其设为False，
# 当使用Event的clear方法后，isSet()方法返回False。
# 4. 等待：wait()
# Event对象的wait()方法只有在内部信号标识为True的时候才会很快的执行并完成返回。
# 当Event对象的内部信号标识为False时，则wait()方法一直等待到其为True时才返回。

k_event = threading.Event()


def test_a():
    k_event.wait()
    print(k_event.is_set())
    print('now,test_a get your information')
    print('clear_event')
    sleep(3)
    print('after 3 sec')
    print(k_event.is_set())
    k_event.set()


def test_b():
    for i in range(5):
        print(i, ' time, test_b am sleeping')
        sleep(1)
    k_event.set()
    print('test_b wait for the next')
    k_event.clear()
    k_event.wait()
    print('test_b get the information')

p1 = threading.Thread(target=test_a)
p2 = threading.Thread(target=test_b)
p1.start()
p2.start()
