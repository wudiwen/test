from 日志 import Logger

userList = ['a', 'b', 'c']
l = Logger('单例类')
l.info('开始输入')
user = input('输入用户名：')
if user not in userList:
    l.error('用户名不存在')
else:
    l.info('输入完成')
