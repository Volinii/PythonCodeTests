#字符串格式化
x='hello'
intX=123456789
fX=1.1234567
print('haha%s'% x)
print('ha'*4+'%-3d'% intX)
print('hahah%03.4f'% fX)
fx=1.1234467
print('hahah%03.4f'% fX)
print('%+05.4f'% fX)
print('%e'% fx)
intX=123.1
print('%06.1f'%intX)#6位包含小数点、小数
print('%-09.2f'%intX)
print('%0*.*f'%(7,3,1.1))#*计算元组中的3为其精度
a=4
print('%.*f'%(a,1.1))#变量控制精度
'''
基于字典的字符串格式化表达式
'''
print('name:%(name)s has %(money).2f Yuan'%{'name':'Jameery','money':1.1})
# %[(keyname)][flags][width][.precision]typecode

replay='name:%(name)s has %(money).2f Yuan'
pInfo={'name':'Jameery','money':1.1}
print(replay % pInfo)

#通过变量,vars()
a='hi'
b=1.1
print('%(a)s %(b)f'% vars())

'''
字符串格式化方法
'''
a='{0},{2}'
print(a.format('h1','h2','h3','h4'))