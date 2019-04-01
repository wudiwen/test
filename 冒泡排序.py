list1 = [2,1,6,4,5,9,7,4]
for i in range(len(list1)):
	for j in range(i+1,len(list1)):
		if list1[i] > list1[j]:
			list1[j] , list1[i] = list1[i] , list1[j]
print(list1)