def choice_sort(array,left,right):
	# min_index = 0
	for i in range(right):
		min_index = i
		for j in range(i+1,right+1):
			if array[j] < array[min_index]:
				min_index = j
	# print(min_num)
		array[i],array[min_index] = array[min_index],array[i]


array1 = [6,5,2,3,4,1]
choice_sort(array1,0,len(array1)-1)
print(array1)