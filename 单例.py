'''
# __new__ 方法实现单例

class Singleton(object):
    def __new__(self, *args, **kwargs):
        #  hasattr 判断对象是否包含某某属性
        if not hasattr(self, '_instance'):
            # 用于调用父类的方法
            orign = super(Singleton, self)
            self._instance = orign.__new__(self)
        return self._instance

class A(Singleton):
    att = 1

a = A()
print(a)

b = A()
print(b)
'''

'''
# 共享属性
# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法

class Singleton2(object):
    _state = {'显卡':'泰坦', '内存条':'金士顿32g', '硬盘':'1tSSD'}
    def __new__(cls, *args, **kwargs):
        ob = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

class A(Singleton2):
    att = 1

a = A()
print(a.__dict__)

b = A()
print(b.__dict__)
'''


'''

# 装饰器实现

def singleton(cls):
    instance = {}
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance

@singleton
class A(object):
    a = 1

a = A()
b = A()
print(a)
print(b)

'''

'''
from 单例类 import singleton
from 单例类 import singleton as s


print(singleton is s)
'''

'''
import sys

# print(sys.modules)
dic = sys.modules
# print(type(dic))
# for key in dic.keys():
#     print(key)


print(dic['zope'].__dict__)
'''



