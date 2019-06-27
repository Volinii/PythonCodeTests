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
import math
print('math.pi: ', math.pi)
print('math.sqrt(85): ', math.sqrt(85))

# 随机模块
import random
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
import re
match = re.match('hello[ \t]*(.*)world', 'hello python world')
print(match.group(1))

# 字典的键从左到右的顺序是被打乱的
# 利用sorted对字典的key排序
a = {'ba': 1, 'bc': 2, '1': 3, '2': 4}

for k in sorted(a):
    print(k)

# 任何一个从左到右扫描一个对象的python工具都使用迭代协议
