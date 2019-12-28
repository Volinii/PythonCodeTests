import os

file_format = '.url'
file_dir = r'C:\Users\volin\Music'

# 遍历目录
files_path_list = []
format_list = []
for r, d, f in os.walk(file_dir):
    for ff in f:
        file_path = os.path.join(r, ff)
        if ff.endswith(file_format):
            # 删除file
            print('del %s' % file_path)
            os.remove(file_path)
        ff_format = ff.split('.')[-1]
        if ff_format not in format_list:
            format_list.append(ff_format)
        if os.path.getsize(file_path) < 5557817:
            if ff_format.upper() not in [
                    'PNG', 'CUE', 'M3U8', 'JPG', 'TIF', 'INI'
            ]:
                print('size too small ', file_path)

print('format_list %s' % str(format_list))
