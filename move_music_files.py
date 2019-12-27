import os
import shutil

root = r'E:\音乐\新建文件夹'

file_list = []
for r, d, f in os.walk(root):
    for ff in f:
        file_list.append(os.path.join(r, ff))

for f in file_list:
    shutil.move(f, root)
