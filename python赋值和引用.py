# def extendList(val,list = []):
# 	list.append(val)
# 	return list

# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')

# print(list1)
# print(list2)
# print(list3)


from copy import copy,deepcopy
from pickle import dumps,loads


a = [1,2,3]
b = [a] * 3
c = copy(b)
d = deepcopy(b)
e = loads(dumps(b,4))

b[1].append(999)
c[1].append(999)
d[1].append(999)
e[1].append(999)

print(b)
print(c)
print(d)
print(e)