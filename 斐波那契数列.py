'''
def fib(max_num):
	n,a,b = 0,0,1
	while n < max_num:
		a,b = b,a+b
		n = n + 1
		print(a)
	return 'got it'

print(fib(10))
'''

# def fib(max_num):
# 	n,a,b = 0,0,1
# 	while n < max_num:
# 		yield b
# 		a,b = b,a+b
# 		n = n + 1
# 	return 'got it'

# c = fib(10)
# print(c)

# print(c.__next__())
# print(c.__next__())
# print(c.__next__())


def fib(max_num):
	n,a,b = 0,0,1
	while n < max_num:
		yield b
		a,b = b,a+b
		n = n + 1
	return 'got it'

c = fib(10)
while 1:
	try:
		x = next(c)
		print('generator :' ,x)
	except StopIteration as e:
		print('return返回值 :',e.value)
		break


# print(c)

# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())

# for i in c:
# 	print(i)






