import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import psutil as p
import win32gui
import win32con
from time import sleep
import json


def show():  # 增加窗口置顶功能
    global hwnd
    # win32gui.SetForegroundWindow (hwnd)#这句好象不行
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 500, 400,
                          win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE |
                          win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW)


POINTS = 300
# 设置上下两个图、面板色。#,edgecolor='#7FFF00'好象无效
fig, ax = plt.subplots(2, facecolor='#FFDAB9')
fig.canvas.set_window_title(u'电脑性能(cpu、内存、网速）实时监测')  # 设置窗口标题
fig.canvas.toolbar.destroy()  # 取消工具栏
fig.canvas.callbacks.callbacks.clear()  # 清除回调信息

# ax为列表，分别设置
ax[0].set_ylim([0, 100])
ax[0].set_xlim([0, POINTS])
ax[0].set_autoscale_on(False)
ax[0].set_xticks([])
ax[0].set_yticks(range(0, 101, 20))
# ax[0].set_facecolor('#A9A9A9')#可设置底色，支持'black')#matplotlib颜色分层设置
ax[0].grid(True)

ax[1].set_ylim([-5, 50])  # 设置0线上浮
ax[1].set_xlim([0, POINTS])
ax[1].set_autoscale_on(False)
ax[1].set_xticks([])
ax[1].set_yticks(range(0, 51, 10))
ax[1].grid(True)

# 设置CPU、内存横坐标数据位
cpu = [None] * POINTS
mem = [None] * POINTS
# 设置接收字节(下载）横坐标数据位
down = [None] * POINTS
# 设置第一个图
cpu_l, = ax[0].plot(range(POINTS), cpu, label='Cpu%')
mem_l, = ax[0].plot(range(POINTS), mem, label='Mem%')
ax[0].legend(loc='upper center', ncol=4,
             prop=font_manager.FontProperties(size=10))  # 打标
# 设置第二个图
down_l, = ax[1].plot(range(POINTS), down, label='Down(M)')
ax[1].legend(loc='upper center', ncol=4,
             prop=font_manager.FontProperties(size=10))

before = p.net_io_counters().bytes_recv  # 获取网络字节数
# 把查找窗口句柄放在这里，不在SHOW()里，
hwnd = win32gui.FindWindow(None, u'电脑性能(cpu、内存、网速）实时监测')  # 查找本窗口句柄
print(hwnd)  # 调试用
# 把win32gui.SetWindowPos(放在这里不行列。


def get_delta(delta_type='dl'):  # 获取下载变化值
    global before
    now = p.net_io_counters().bytes_recv
    delta = (now-before)/125000  # mbps。
    before = now
    return delta  # 返回改变量


def save_delta(keep_time):  # 保存下载直的数据
    delta_data = []
    for _ in range(keep_time):
        delta_data.append(get_delta())
        sleep(1)
    return delta_data


def rec_to_json(file_path, keep_time=60):
    data_dict = {}
    data_dict['data'] = save_delta(keep_time)
    _dump_json(data_dict, file_path)


def show_local_data(file_path, points=300):
    data_dict = _loadJson(file_path)
    data = data_dict['data']
    plt.plot(range(points), data)
    plt.show()

# load_json
def _loadJson(jsonPath):
    '''
    load json文件
    Args：
        jsonPath: json文件的路径
    return：
        返回json文件内容，通常为一个字典
        打开json文件失败时，返回None
    '''
    print('jsonManager.loadJson:jsonPath:'+str(jsonPath))
    try:
        with open(jsonPath, 'r', encoding='utf-8') as f:
            jDict = json.load(f)
            return jDict
    except OSError:
        # logging.error('judgePassFail.loadStandard:open jsonPath fail!')
        return None


# dump_json
def _dump_json(jdict, file_path):
    '''jdict->file_path
    字典内容dump到文件中
    Args：
        jdict：字典
        file_path:文件路径
    Return：
        None
    '''
    print('dump_json start: ', file_path)
    with open(file_path, 'w') as jf:
        json.dump(jdict, jf, ensure_ascii=False, sort_keys=False, indent=2)
        jf.write('\n')
    print('dump_json end')


def OnTimer(ax):
    global cpu, mem, down
    show()
    tmp = get_delta()  # 得到下载字节数的变化值
    cpu_p = p.cpu_percent()  # 读取CPU使用百分比
    cpu = cpu[1:] + [cpu_p]  # 加入到数据末尾
    mem_p = p.virtual_memory().percent  # 读取内存使用百分比
    mem = mem[1:] + [mem_p]  # 加入到数据末尾
    cpu_l.set_ydata(cpu)  # 设置新数据
    mem_l.set_ydata(mem)  # 设置新数据
    down = down[1:] + [tmp]
    down_l.set_ydata(down)  # 设置新数据
    # 下面这部分可以忽略
    #    while True:
    #        try:
    #            ax.draw_artist(cpu_l)
    #            ax.draw_artist(mem_l)
    #            ax.draw_artist(down_l)
    #            break
    #        except:
    #            pass
    ax.figure.canvas.draw()  # 刷新画布


def start_monitor():
    # 1秒刷新一次
    timer = fig.canvas.new_timer(interval=1000)
    timer.add_callback(OnTimer, ax[1])  # 只加一个即可
    #timer.add_callback(OnTimer, ax[0])
    timer.start()
    plt.show()


if __name__ == '__main__':
    # start_monitor()
    rec_to_json(r'C:\Users\volin\Downloads\16324_20161202165106\test_data.json', 300)
    show_local_data(r'C:\Users\volin\Downloads\16324_20161202165106\test_data.json')