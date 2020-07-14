import multiprocessing
import time,threading

'''
def thread_run():
    print(threading.get_ident())   # get_ident 获取当前线程的ID

def run(name):
    time.sleep(2)
    print('hello',name)
    t = threading.Thread(target=thread_run,)  # 在进程中起了一个线程
    t.start()


if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=run,args=('tom%d'%i,))
        p.start()
'''

# 多个线程抢占一个内存空间，如果量大的时候就会出问题
'''
number = 0
def run(num):
    global number
    number += 1
    print(number)
    time.sleep(1)

for x in range(1000):
    t = threading.Thread(target=run,args=(x,))
    t.start()
'''
# 给线程加锁
number = 0
lock = threading.RLock()  # 创建锁的实例
def run(num):
    lock.acquire()  # 开始加锁
    global number
    number += 1
    lock.release()  #线程解锁
    print(number)
    
    time.sleep(1)
    

for x in range(1000):
    t = threading.Thread(target=run,args=(x,))
    t.start()



# QLDTYDUVEYVATPAY

# XZEDRZZNDPZHZQVJ
