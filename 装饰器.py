'''
import time

def show_time(func):
	def dec(*args,**kwargs):
		time_start = time.time()
		func(*args,**kwargs)
		time_end = time.time()
		t = time_end - time_start
		# print('函数运行时间为 {} '.format(t))
		print('函数的运行时间为 %s'%t )
	return dec
@show_time
def yanghui(*args,**kwargs):
	for i in range(1,10):
		for j in range(1,i+1):
		    print('*', end = ' ')
		print(' ')
yanghui()
'''
# def dec(func):
# 	def show(*args,**kwargs):
# 		print('呵呵')
# 		func(*args,**kwargs)
# 	return show
# @dec
# def add(a,b):
# 	print(a+b)
# add(1,2)
import time
def show_time(func):
	def dec(*args,**kwargs):
		time_start = time.time()
		func(*args,**kwargs)
		time_end = time.time()
		t = time_end - time_start
		print('函数运行时间为 %s'% t)
	return dec

@show_time
def yanghui(*args,**kwargs):
	for i in range(1,10):
		for j in range(1,i+1):
			print('*', end = ' ')
		print('\t')
yanghui()
