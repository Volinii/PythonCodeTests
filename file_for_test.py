f1=open(r'C:\codeSpace\PythonCodeTests\testResource\file.txt','w')
f1.write('hello,world!\r\n')

#print('===a===')
#f=open(r'C:\codeSpace\PythonCodeTests\testResource\file.txt','a')
#for line in f:
#    print(line)

print('===r===')
f=open(r'C:\codeSpace\PythonCodeTests\testResource\file.txt','r')
for line in f:
    print(line)

#文件对象未销毁时，还在w模式下，只有文件对象关闭或者销毁时才保存。
f1.write('test line2\r\n')
f1.close()
n=0
for line in f:
    print(n)
    print(line)
    n+=1

#f.seek()偏移文件指针