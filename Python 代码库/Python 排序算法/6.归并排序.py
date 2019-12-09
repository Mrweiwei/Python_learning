#归并排序算法

def mergeSort(arr):
    '''归并排序(Merge sort)是建立在归并操作上的一种有效的
排序算法。该算法是采用分支(Divide and Conquer)的一个非常典型
的应用'''
    import math
    if(len(arr)<2):
        return arr
    middle=math.floor(len(arr)/2)
    left,right=arr[0:middle],arr[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result=[]
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


arr=[123,324,435,5466,657,34,234,546,2,345,34523]
print(mergeSort(arr))
            
