
'''
def quick_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)
 
def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i+1]
    print(i+1)
    # array[left], array[i+1] = array[i+1], array[left]
    return i + 1


array1 = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
quick_sort(array1,0,len(array1)-1)
print(array1)

'''


'''
# from time import time
# def showTime(func):
#     def dec(*args, **kwargs):
#         start = time()
#         func(*args, **kwargs)
#         end = time()
#         need_time = end - start
#         print('需要时间为', need_time)
#     return dec


# @showTime
def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        print(p)
        quick_sort(array, low, p)
        quick_sort(array, p+1, high)

def partition(array, low, high):
    pivot = array[low]  # 将第一个元素作为基准值
    while low < high:
        while low < high and array[high] >= pivot:
            high -= 1
        array[low] = array[high]  # 将比基准值小的往左移动
        while low < high and array[low] <= pivot:
            low += 1
        array[high] = array[low]  # 将比基准值大的往右移动
    array[low] = pivot   # 将基准值放到正确的位置
    return low


if __name__ == '__main__':
    array = [2,8,7,1,4,5,16,10,2]
    quick_sort(array, 0, len(array)-1)
    print(array)
'''