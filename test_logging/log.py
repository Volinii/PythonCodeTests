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

# [loggers]
# keys=root,example01

# [logger_root]
# level=DEBUG
# handlers=hand01,hand02

# [logger_example01]
# handlers=hand01,hand02
# qualname=example01
# propagate=0

# [handlers]
# keys=hand01,hand02

# [handler_hand01]
# class=StreamHandler
# level=INFO
# formatter=form01
# args=(sys.stderr,)

# [handler_hand02]
# class=FileHandler
# level=DEBUG
# formatter=form02
# args=('log.log', 'a')


# [formatters]
# keys=form01,form02

# [formatter_form01]
# format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s

# [formatter_form02]
# format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s