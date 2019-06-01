import re
a = 'hello     world!'
b = re.match('hello[ \t](.*)world!', a)
print(len(b.group()))
