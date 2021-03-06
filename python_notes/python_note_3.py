# 数值类型
# 完整的数值类型工具包括：
#     整数和浮点数对象
#     复数对象
#     小数：固定精度对象
#     分数：有理数对象
#     集合：带有数值运算的集合体
#     布尔值：真和假
#     内置函数和模块：round match random 等
#     表达式；无限制整数精度；位运算；十六进制、八进制和二进制格式
#     第三方扩展：向量、库、可视化、作图等

# 浮点数在标准CPython中采用C语言中的‘双精度’来实现

# yield x                     生成器函数send协议
# lambda args:expression      创建匿名函数
# x if y else z               三元选择表达式（仅当y为真时，x才会被计算）
# x or y                      逻辑或
# x and y                     逻辑与
# not x                       逻辑非
# x in y, x not in y          成员关系（可迭代对象、集合）
# x is y, x is not y          对象同一性测试
# x<y,x<=y,x>y,x>=y           大小比较、集合的子集和超集
# x ==y, x != y               值等价性运算符
# x|y                         按位或、集合并集
# x^y                         按位异或、集合对称差集
# x&y                         按位与、集合交际
# x << y, x >> y              将x左移或右移y位
# x+y                         加法、拼接
# x-y                         剑法、集合差集
# x * y                       乘法、重复
# x % y                       求余数、格式化
# x/y,x//y                    真除法、向下取整除法
# -x,+x                       取负、取正
# ~x                          按位非（取反码）
# x**y                        幂运算（指数）
# x[i]                        索引（）序列、映射等
# x[i:j:k]                    分片
# x(...)                      调用
# x.attr                      属性引用
# (...)                       元组、表达式、生成器表达式
# [...]                       列表、列表推导
# {...}                       字典、集合、集合和字典推导

# 混合类型向上转换
print(40 + 3.14)

print(int(3.14))  # 通常不需要这么做，
print(float(3))   # 因为python 在表达式中自动升级成更复杂的类型，其结果往往就是你想要的

# 多态指的时：操作的意义由操作对象来决定

# str 和 repr
print(repr('spam'))  # 'spam'
print(str('spam'))

# python3中总是执行真除法，不管操作的类型，都返回包含任何小数部分的一个浮点数结果
# 真除法,python2 中/表示经典除法，即结果向下取整
print(10/4)
print(10/4.0)

# //运算符有一个非正式的别名，叫做截断除法，不过更准确的说法应该是向下取整除法，对负数也有效

# pow 和 abs 用于分别计算幂和绝对值

# Python 和 Numpy的组合往往可以比作一款免费的、更加灵活的matlab
