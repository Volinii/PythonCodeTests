import os

spath=r'F:\PSP中文游戏'
a=os.listdir(spath)
print(a)

for p in a:
    print('=='*25,p)
    b=str.split(p,']')
    if len(b) >= 3:
        if '0' not in b[0]:
            continue
        print(b)
        name = ''
        for i in range(len(b)):
            if i == 0:
                continue
            name += b[i]+']'
        print('-'*25, name)
        s=os.path.join(spath,p)
        t=os.path.join(spath,name)
        os.rename(s,t)
