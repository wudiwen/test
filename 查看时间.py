import time

def dec(func):
	def see(*args,**kwargs):
		time_begin = time.time()
		func(*args,**kwargs)
		time_end = time.time()
		t = time_end - time_begin
		print('檀少洋只能坚持 {} 秒'.format(t))
	return see

@dec
def yanghui(*args,**kwargs):
	for i in range(1,1000):
		for j in range(1,i+1):
			print('檀少洋牛逼',end = ' ')
		print(' ')
print('yanghui')
yanghui()



