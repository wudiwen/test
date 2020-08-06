# a ---> 左列表  b ---> 右列表
# j ---> 左列表起始索引   h ---> 右列表起始索引
def merge(a,b):
	c = []
	h = j = 0
	while j < len(a) and h < len(b):
		if a[j] < b[h]:
			c.append(a[j])
			j += 1
		else:
			c.append(b[h])
			h += 1
	if j == len(a):
		for i in b[h:]:
			c.append(i)
	elif h == len(b):
		for i in a[j:]:
			c.append(i)

	return c 

def merge_sort(lists):
	if len(lists) <= 1:
		return lists
	middle = int(len(lists)//2)
	left = merge_sort(lists[:middle])       
	right = merge_sort(lists[middle:])   
	return merge(left,right)

if __name__ == '__main__':
	list1 = [3,40,7]
	print(merge_sort(list1))

'''
#  简易模拟递归流程
def merge_sort([3,40,7]):
    if len([3,40,7]) <= 1:
        return [3,40,7]
    middle = 1
    left = merge_sort([3])
        if len([3]) <= 1:
            return [3]
    right = merge_sort([40,7]) 
        if len([40,3]:) <= 1:
            return [40,3]
        middle = 1
        left = merge_sort([40])
            if len([40]) <= 1:
                return [40]
        right = merge_sort([7])
            if len([7]) <= 1:
                return [3]
        return merge(left,right)
    return merge(left,right)

'''



'''
# 输入 3  
import time,random
def show_time(func):
	def dec(*args,**kwargs):
		time_start = time.time()
		a = func(*args,**kwargs)
		time_end = time.time()
		t = time_end - time_start
		print('函数运行时间为 %s'% t)
		return a
	return dec

@show_time
def MergeTopOf(num,*args):
	array = sum(args, [])
	# print(array)
	return merge_sort(array)[0:num]

a = MergeTopOf(10000,[1,3,4], [2,7], [5])
print(a)

'''
