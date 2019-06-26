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


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False
print('----------123:')
print(is_number('123'))
print('----------abcd:')
print(is_number('abcd'))
print('----------123abcd:')
print(is_number('123adcd'))
print('---------- -123:')
print(is_number('-123'))
print('----------1.234:')
print(is_number('1.234'))
print('---------- -1.234:')
print(is_number('-1.234'))
print('----------0:')
print(is_number('0'))
a="   sdads\r\n"
print(a.strip())