# 核心数据类型

# 数字 1234，3.14，3+4j,0b111,Decimal(),Fraction()
# 字符串
# 列表
# 字典
# 元组
# 文件
# 集合 set('abc'), {'a','b','c'}
# 类型
# None
# 布尔型
# 函数
# 模块
# 类
# Python实现相关类型： 已编译代码、调用栈跟踪

# 数学模块
import re
import random
import math
print('math.pi: ', math.pi)
print('math.sqrt(85): ', math.sqrt(85))

# 随机模块
print('random.random(): ', random.random())
print('random.choice([1,2,3,4]): ', random.choice([1, 2, 3, 4]))

# 字符串

# 字符串是列表
a = 'hahahaha'
print('the length of string :', len(a))

# find
print('find string index: ', a.find('a'))

# replace
print('replace a to b:', a.replace('a', 'b'))

# split
print('a.split(): ', a.split('h'))

# 字符串转列表
a = 'abcd12'
print(a.split())  # ['abcd12']
# upper
print('a.upper():', a.upper())

# rsplit 从右向左分割maxsize次
print('hahahaha.rsplit(): ', a.rsplit('h', 4))

# rstrip
print('haha\n'.rstrip())
print('haha\r\n'.rstrip())

# python3禁止再没有显示转型的情况下，将普通字符串和字节串混合使用
# print(u'x' + b'y')  # 报错
print(u'x' + 'y')

# encode 字符串转字节串
print('x'.encode())
# decode 字节串转字符串
print(b'x'.decode())

# re模块：模式匹配（如：正则表达式）
match = re.match('hello[ \t]*(.*)world', 'hello python world')
print(match.group(1))

# 字典的键从左到右的顺序是被打乱的
# 利用sorted对字典的key排序
a = {'ba': 1, 'bc': 2, '1': 3, '2': 4}

for k in sorted(a):
    print(k)

# 任何一个从左到右扫描一个对象的python工具都使用迭代协议

# 列表推导和相关的函数编程工具（如map和filter）在某些代码上通常运行得比for循环快（甚至可能快了两倍）

# 测试代码速度得time 和 timeit模块，以及分离性能瓶颈得profile模块

# 只含一个元素得元组需要一个逗号作为结尾
# 包住元组元素得圆括号通常都可以被省略
a = 1,
print(a)

# namedtuples 有名元组
# seek工具 用于移动文件读取指针到指定位置
# fileObject.seek(offset[, whence])
#       offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
#       whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
#       0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

# 读取一个文件得最佳方式就是根本不读它，而是通过文件提供得一个迭代器在for循环或其他上下文中自动地逐行读取
# for line in open('data.txt'):print(line)

# struct.pack  按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
# https://blog.csdn.net/lis_12/article/details/52777983

# 集合通过set函数创建
x = set('abc')
print(x)
y = set('bc')
print(y)
print(x-y)
print(x & y)
print(x | y)
print(x > y)

# 把集合当作处理例如：过滤重复对象、分离集合间差异，进行非舒徐得等价判断等任务得利器
print(set('sayaa') - set('aa'))
print(set('hei') == set('hie'))

