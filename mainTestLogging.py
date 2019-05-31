import logging
import os
import testLogging1
import testLogging
thisPath = os.path.dirname(os.path.realpath(__file__))
print(thisPath)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')
logging.info('main')
t1 = testLogging1.test1()
t2 = testLogging.test2()
t1.testA()
t2.test2A()
t1.testA()
t2.test2A()
logging.info('3333')
