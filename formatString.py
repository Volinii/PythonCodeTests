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