

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

