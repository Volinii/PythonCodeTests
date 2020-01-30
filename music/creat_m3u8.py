import os

# 用户设置的路径
music_dir = r'C:\Users\volin\Music\抖音热歌2019'

# 播放列表保存的路径
root_dir = r'C:\Users\volin\Music'

# 音频文件的后缀名，为判断是否是音频文件作依据
music_format = ['FLAC', 'DSF', 'DFF', 'APE', 'WAV']

# 创建播放列表文件
list_name = os.path.basename(music_dir) + '.M3U8'

f = open(os.path.join(root_dir, list_name), 'w', encoding='utf-8')

# 写.M3U8文件的第一行标志信息
f.write('#EXTM3U')

# 遍历目录
for r, d, files in os.walk(music_dir):
    # 对每个文件名进行迭代判断
    for file_ in files:
        # 截取文件名file_的后缀名
        file_format = file_.split('.')[-1]
        # 拼接文件的完整路径
        file_path = os.path.join(r, file_)

        # 不是文件时跳过本轮，continue跳过本轮
        if file_format.upper() not in music_format:
            print('not a music format file: ', file_path)
            continue

        # 得到相对路径（播放列表中的歌曲都是相对播放列表文件的相对路径）
        file_path = file_path.replace(root_dir, '')

        # 路径以\开头时删除\符号
        if file_path[0] == '\\':
            file_path = file_path[1:]
        file_path = file_path.replace('\\', '/')
        print(file_path)

        # 转换成播放列表记录的信息格式，注意添加换行符\n
        txt = '\n#EXTINF:,\n'
        txt += file_path

        # 写入播放列表文件
        f.write(txt)

# 关闭播放列表的文件
f.close()
