import numpy
from mxnet import np, numpy_extension
# numpy_extension.set_np()

x = np.arange(12)
print(x)

x = np.array([[1,2,3],[1,3,5]])
print(x.shape) # 张量

print(x.size) # 元素的个数

print(x.reshape(1,6))

print(x.reshape(3,2))

print(np.zeros((2,3)))  # 0000
print(np.ones((2,2)))   # 111

print(np.random.normal(0,1,size=(3,4))) #random

print(np.exp(1)) # 指数   #2.718281828459045 自然常数

print(np.concatenate([x, np.zeros((2,3))], axis=0)) # 连接 axis=0  y插入行到x
print(np.concatenate([x, np.zeros((2,3))], axis=1)) # 连接 axis=1  y插入列到x

# https://zh-v2.d2l.ai/chapter_preliminaries/ndarray.html

print(numpy.array([1.,2.,3.,4.]))