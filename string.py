testString='Volin'

print(testString.find('li'))
print('--------test find--------')
print(testString.find('a'))

print(testString.isalpha())
print(testString.isdigit())
print('--------isdigit:12--------')
print('12'.isdigit())
print('--------isdigit:-12--------')
print('-12'.isdigit())
print('aa'.isalpha())
print('-aa'.isalpha())
print('string'.isidentifier())#标识符
print('as'.islower())#小写
print('1223'.isnumeric())
'''
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''
print('-12.33'.isprintable())
print('Abcd'.istitle())#首字母大写
print('ABC'.isupper())
print('--------isdigit:12.56--------')
print('12.56'.isdigit())
print('12'.isdecimal())#十进制
print('--------isdigit:-12.56--------')
print('-12.56'.isdigit())
print('--------isdigit:12abcd--------')
print('12abcd'.isdigit())
print('12abcd'.isalnum())
