'''
import logging

def func(a,b):
	try:
		c = a/b
		return c
	except:
		logging.debug('除数不可以为0')

func(1,0)
'''

#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message') 











