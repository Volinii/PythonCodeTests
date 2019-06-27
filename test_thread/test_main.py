import threading
from time import sleep

# 第一种线程调用方法
# 创建一个Thread实例，把函数（target）及其参数（args）都传递进去。
# 当线程开始执行时，这个函数也会开始执行。


def test(a):
    sleep(1)
    print('test', a)
p1 = threading.Thread(target=test, args=('haha',))
p2 = threading.Thread(target=test, args=('2222',))
p1.start()
p2.start()
#  p1.join()  # 阻塞，p1进程完成后继续执行主线程
print('main')

# 第二种线程调用方法
# 创建一个Thread实例，传递给它一个可调用的类实例，这是多线程编程的一个更为面向对象的方法。


class TestClass:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

p3 = threading.Thread(target=TestClass(test, 'hello class'))
p3.start()


# 第三种线程调用方法
# 派生Thread类的子类，重写它的run方法，把线程执行的代码放到这个新的子类里，然后创建这个子类的实例。


class SubTest(threading.Thread):
    def __init__(self, num):
        self.num = num
        threading.Thread.__init__(self)  # 调用父类的初始化方法

    def run(self):  # 重写run方法
        print('test 3rd thread', self.num)

p4 = SubTest(5)
p5 = SubTest(7)
p4.start()
p5.start()

# start()：启动线程
# run()：定义线程功能的方法（一般会被子类重写） 
# join(timeout=None)：设置后主线程在终止前一直挂起（被阻塞），直到子线程结束。如果给了timeout参数，则最多阻塞timeout秒
# isAlive()：返回线程是否在运行
# getName(name)： 返回线程名
#  setName(name)：设置线程名
# isDaemon(bool)：返回是否是守护线程
# setDaemon(bool)：设置是否是守护线程，必须在start()方法调用之前设置.守护线程:表示这个线程不重要,不管是否完成，一并和主线程退出


def wait_5_s(content):
    sleep(10)
    print('wait', content)

p6 = threading.Thread(target=wait_5_s, args=('hahaha',), name='Janmeey')
p6.start()
print(p6.getName())
print('isAlive: ', p6.isAlive())


# 对于多线程来说，最大的特点就是线程之间可以共享数据，
# 共享数据会出现多线程同时更改一个变量，使用同样的资源，而出现死锁、数据错乱等情况。
# 例如有两个全局资源，a和b，有两个线程thread1和thread2。thread1占用a，想访问b，
# 但此时thread2占用b，想访问a，两个线程都不释放此时拥有的资源，那么就会造成死锁。
# 针对该问题，Python的threading模块提供了Lock对象（锁），
# 锁是最简单最低级的同步机制，保证了每次只有一个线程对全局变量进行写入操作。
# 首先通过threading.Lock()创建一个锁，
# 当访问某个资源之前，用acquire()获取锁，
# 待资源访问完之后，用release()释放锁。锁定方法acquire()可以有一个超时时间的可选参数timeout，
# 如果设定了timeout，则在超时后通过返回值可以判断是否得到了锁。
lock = threading.Lock()
common = 'common'


def read_common():
    print('run read_common')
    lock.acquire()
    global common
    print(common)
    sleep(3)
    print(3)
    lock.release()

p1 = threading.Thread(target=read_common)
p2 = threading.Thread(target=read_common)
p1.start()
p2.start()


# 可以使用with关键字代替手动调用acquire()和release()
a = 3


def target():
    print('the curent threading %s is running' % threading.current_thread().name)
    sleep(4)
    global a
    with lock:  # 可以使用with关键字代替手动调用acquire()和release()
        print('%s is changing the value of a' % threading.current_thread().name)
        a += 3
        print(a)
        print('the curent threading %s is ended' % threading.current_thread().name)

t1 = threading.Thread(target=target)
t2 = threading.Thread(target=target)

t1.start()
t2.start()

# RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。
# RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。
# 拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。
# 当所有RLock被release()后，其他线程才能获取资源。
# RLock包含一个锁定池和一个初始值为0的计数器，
# 计数器记录了acquire()和release()的次数，
# 每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。


# Python提供的Condition对象提供了对复杂线程同步问题的支持，除了Lock带有的锁定池外，还包含一个等待池。
# Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。
# 线程首先acquire一个条件变量，然后判断一些条件。
# 如果条件不满足则wait，
# 如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，
# 其他处于wait状态的线程接到通知后会重新判断条件。
# 不断重复这一过程从而解决复杂的同步问题。

product = None
con = threading.Condition()


def produce():
    global product
    if con.acquire():
        c = 0
        while True:
            if product is None:
                print('produce...')
                product = 'anything'
                con.notify()  # 通知消费者，商品已经生产
            con.wait()        # 等待通知
            sleep(2)
            c += 1
            if c == 4:
                break


def consume():
    global product
    print('con.acquire():  ', con.acquire())
    if con.acquire():
        c = 0
        while True:
            if product is not None:
                print('consume...')
                product = None
                con.notify()  # 通知生产者，商品已经没了
            con.wait()        # 等待通知
            sleep(2)
            c += 1
            if c == 4:
                break

t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t1.start()
t2.start()

# Semaphore是计算机科学史上最古老的同步指令之一，用来控制对共享资源的访问数量，例如线程最大连接数。
# Semaphore管理一个内置的计数器：每当调用acquire()时内置计数器-1；调用release() 时内置计数器+1；
# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()

# Semaphore限制最多有2个线程同时执行
semaphore = threading.Semaphore(2)


def func():
    # 请求Semaphore，成功后计数器-1，计数器为0时阻塞
    if semaphore.acquire():
        print((threading.currentThread().getName() + ' get semaphore'))
        time.sleep(2)
        # 释放Semaphore，计数器+1
        semaphore.release()

for i in range(5):
    t1 = threading.Thread(target=func)
    t1.start()
