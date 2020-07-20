'''
import random
class Solution:

    def __init__(self, nums):
        self.array = nums
        self.reset_arr = nums

    def reset(self) :
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.reset_arr
        return self.nums

        

    def shuffle(self) :
        """
        Returns a random shuffling of the array.
        """
        arr = []
        while True:
            index = random.randint(0,len(self.array)-1)
            if self.array[index] not in arr:
                arr.append(self.array[index])
            if len(arr) == len(self.array):
                break
        return arr


a = Solution([2,1,3])
print(a.shuffle())
print(a.reset())
'''

'''
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        arr = []
        s = str(N)
        for x in s:
            arr.append(int(x))
        arr.sort()
        s1 = ''
        for i in range(len(arr)):
            s1 += str(arr[i])
        l = len(s1)
        print(s1)
        
        for y in range(32):
            num = str(2**y)
            print(num)
            if len(num) > l:
                return False
            arr1 = []
            for z in num:
                arr1.append(int(z))
            arr1.sort()
            s2 = ''
            for j in range(len(arr1)):
                s2 += str(arr1[j])
            if s2 == s1:
                return True
        return False
            

a = Solution()
b = a.reorderedPowerOf2(16)
print(b)

'''


'''
def isNull(l):
    flag = 1
    for x in l:
        if x != None:
            flag = 0
            break
    return flag

a = [None,None,None,None,1]
print(isNull(a))

'''




