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

'''
import logging

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message') 
'''


# 单例模式实现日志记录
# 日志参考： https://www.jianshu.com/p/d5ed1d5bc976

import logging
'''
class Logger(object):
	def __init__(self):
		self.log_file_path = './test.log'
		file_handler = logging.FileHandler(self.log_file_path, 'a', encoding='utf-8')
		file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(filename)s[line: %(lineno)d] :  %(message)s"))

		self.logger = logging.Logger('cmdb', level=logging.INFO)
		self.logger.addHandler(file_handler)

	def info(self,msg):
		self.logger.info(msg)
	def error(self,msg):
		self.logger.error(msg)

logger = Logger()

'''

class Singleton(object):
	def __new__(self, *args, **kwargs):
		if not hasattr(self, 'instance'):
			self.instance = super(Singleton, self).__new__(self)
		return self.instance

class Logger(Singleton):
	def __init__(self,name):
		self.name = name
		# 创建logger
		self.logger = logging.getLogger(name=self.name)
		self.logger.setLevel(logging.INFO)

		# 创建屏幕输出
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		# 创建文件输出 
		fh = logging.FileHandler('test1.log', encoding='utf-8')
		fh.setLevel(logging.DEBUG)

		# 创建日志格式器
		style = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s[line: %(lineno)d] : %(message)s')

		# 添加到ch, fh
		ch.setFormatter(style)
		fh.setFormatter(style)

		#添加ch, fh 到logger
		self.logger.addHandler(ch)
		self.logger.addHandler(fh)

	def debug(self,msg):
		self.logger.debug(msg)

	def info(self,msg):
		self.logger.info(msg)

	def warn(self,msg):
		self.logger.warn(msg)

	def error(self,msg):
		self.logger.error(msg)

	def critical(self,msg):
		self.logger.critical(msg)


















