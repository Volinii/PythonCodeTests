import tkinter as tk
from time import sleep
from threading import Thread


def pf():
    print('hahaa')


top = tk.Tk()  # 画布/顶层窗体
top.title('volin')
top.geometry('800x400')  # 长宽
bt = tk.Button(top, text='test', bg='red', fg='blue', command=pf)
bt.pack(fill=tk.X)
bt2 = tk.Button(bt, text='aaa', bg='red', fg='black')
bt2.pack(ipadx=100)
m1 = tk.Menubutton(top, text='set')
m1.pack(after=bt)
s1 = tk.Scale(from_=1, to=300, orient=tk.HORIZONTAL)
s1.pack(fill=tk.X)
c1 = tk.Canvas(top, width=200, height=300)
c1.pack()


def t():
    for n in [250, 100, 200, 220, 150, 160]:
        y = n
        for x in [40,50,60,70,80,90]:
            p2 = [0, 250, 200, 250]
            c1.create_text(80, 250, text='hahahhhhhhhhhh')
            c1.create_line(p2, fill='black')
            p = [0, 300, 10, 250, 20, 217, 30, 290, x, y]
            sleep(1)
            print(p)
            ttt=c1.create_line(p, fill='red')
            
            
c1.delete()
ppp=Thread(target=t).start()
top.mainloop()
