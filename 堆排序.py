'''
# 打印树函数（辅助函数）
import math
def print_tree(array):
    
    # 深度 前空格 元素间空格
    # 1     7       0
    # 2     3       7
    # 3     1       3
    # 4     0       1 
    
    index = 1
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()
# print_tree([0, 30, 20, 80, 40, 50, 10, 60, 70, 90, 22])
# print_tree([0, 30, 20, 80, 40, 50, 10, 60, 70, 90, 22, 33, 44, 55, 66, 77])
# print_tree([0, 30, 20, 80, 40, 50, 10, 60, 70, 90, 22, 33, 44, 55, 66, 77, 88, 99, 11])
'''
# 堆排 
# 大根堆：左右子节点的值都小于父节点   l(i) >= l(2i) 且 l(i) >= l(2*i+1)
# 小根堆：左右子节点的值都大于父节点   l(i) <= l(2i) 且 l(i) <= l(2*i+1)

# 建立大根堆的算法
# array --> 待排序列表，   length --> 列表长度-1
def buildMaxHeap(array, length):
    # length//2  --> 找到最后一个有孩子的节点
    for i in range(length//2,0,-1):  # 从下往上循环调整
        ajustUp(array, i, length)
  
# array-->待排序数组（数组第一个元素加了0，辅助元素） 
# k --> 数组长度-1
def ajustUp(array, start, end):  
    temp = array[start]

    i = start   # 找到起点
    j = 2*i     # 找到该起点的左子节点

    while j <= end:
        if j < end and array[j] < array[j+1]:  # 说明该节点下面有两个子节点 且右节点大于左节点
            j += 1
        if temp < array[j]:
            array[i] = array[j]
            i = j
            j = 2*i
        else:
            break
    array[i] = temp  # 起点的值找到最终位置


# array-->待排序数组（数组第一个元素加了0，辅助元素）
# k --> 数组长度-1
def heapSort(array, length):
    # 下面4行也是初始化大根堆
    # count = length//2
    # for i in range(count):
    #     ajustUp(array, count-i, length) 
    # print_tree(a)

    buildMaxHeap(array, length)  # 初始化大根堆
    for i in range(length):
        # 将堆顶元素交换到最后一位
        array[1], array[length-i] = array[length-i], array[1]
        ajustUp(array, 1, length-i-1)
    array.remove(0)
    return array
    
if __name__ == '__main__':
    # 列表前面补 0 的目的是 让堆的序号和列表的索引一致
    a = [0, 87, 45, 78, 32, 17, 65, 53, 9, 63]
    l = heapSort(a, len(a)- 1)
    print(l)
