import logging

logger = logging.getLogger('errorLogger')
fh = logging.FileHandler(r'C:\codeSpace\resource\1.txt')
logger.setLevel(logging.ERROR)
a=logging.Formatter('%(message)s')
fh.setLevel(logging.DEBUG)
fh.setFormatter(a)
logger.addHandler(fh)
logger.info('haha')

# https://www.jianshu.com/p/feb86c06c4f4