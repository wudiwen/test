generator_list = (i*i for i in range(1,5))
print(generator_list)

#print(next(generator_list))
#print(next(generator_list))
#print(next(generator_list))
#print(next(generator_list))
#print(next(generator_list))

for j in generator_list:
	print(j)

'''
a = [1,2,3]     # 可迭代对象
b = iter(a)     # iter方法将iterable 变成 迭代器 iterator
print(type(a))
print(type(b))
print(b.__next__())   # 通过next方法获取元素
print(next(b))
# 迭代器是有状态的对象，会记录当前迭代的位置，以便下次可以获取正确的值
'''
'''
# 生成器 generator
def iter_sth():
    for i in range(10):
        yield i

print(next(iter_sth()))
'''
'''
# 迭代器 斐波那契数列
class Fab:
    def __init__(self,m):
        self.max = m
        self.n = 0
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.a
            self.a,self.b = self.b,self.a+self.b
            self.n += 1
            return r
        raise StopIteration('over')

a = Fab(20)
for x in a:
    print(x)
# print(next(a))
'''
# 生成器  斐波那契数列

def fab(m):
    n,a,b = 0,1,1
    while n < m:
        yield a
        a,b = b,a+b
        n += 1

for i in fab(10):
    print(i)








