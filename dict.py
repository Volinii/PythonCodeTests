#字典可以映射函数名
def a():
    print('aaaaaaaaaaa')
def b():
    print('bbbbbbbbbbbb')
d={'a':a,'b':b}

c=d.get('a',None)
c()
#

d={'a':1,'b':2}
print(d['a'])
d['a']+=1
print(d)

#字典其它创建方法
d=dict(a=1,b=2,c=3)
e=dict(zip(['a','b','c'],[1,2,3]))
print(d)
print(e)

#重访嵌套

d={'name':{'first':'hi','second':'hello'},
    'ga':[1,2,3]}
print(d['name']['first'],d['ga'][1])

#创建新的key和值
d['good']='bad'
print(d)

#判断key是否存在
if 'good' in d:print('true')

print(d.get('bad','null key'))