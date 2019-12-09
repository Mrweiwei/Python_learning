#简单插入排序
def insertionSort(arr):
    '''对于未排序数据，在已排序序列中从后向前扫描，
找到相应位置并插入'''
    for i in range(len(arr)):
        preIndex=i-1
        current=arr[i]
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1]=arr[preIndex]
            preIndex-=1
        arr[preIndex+1]=current
    return arr

arr=[213,123213,123213,23432,454,657,6576,787]
print(insertionSort(arr))
