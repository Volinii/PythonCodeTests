import cv2
from time import sleep
import threading

print('='*25)


def start_play(status):
    print('start   ' * 8)
    print('.'*25)
    print(status)
    print(type(status))

    video_path = r'F:\BaiduNetdiskDownload\325.童话镇\S01\S01E01.mkv'
    cap = cv2.VideoCapture(video_path)
    # if status[0] =='stop':
    #    break
    while True:
        ret, frame = cap.read()
        if ret is True:
            cv2.imshow('test', frame)
            if status[0] == 'pause':
                while status[0] != 'pause':
                    cv2.waitKey(25)
            if status[0] == 'shot':
                cv2.save(frame)

            if status[0] == 'next':
                break
            cv2.waitKey(25)

playsta = ['continue']
print('*'*25)
p = threading.Thread(name='videoPlay', target=start_play, args=(playsta,))
# p = multiprocessing.Process(name='videoPlay', target=start_play)
print('-'*25)
p.start()
print('sleep  '*10)
sleep(2)
playsta[0] = 'next'
print(a[0])
print('end'*25)