#Heap sort 堆排序
#建立大顶堆
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

#筛选堆的函数
def heapify(arr,i):
    left=2*i+1
    right=2*i+2
    largest=i
    if left <arrLen and arr[left]>arr[largest]:
        largest=left
    if right<arrLen and arr[right]>arr[largest]:
        largest=right
    if largest !=i:
        swap(arr,i,largest)
        heapify(arr,largest)

#交换函数
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]  #序列解包的形式不需要temp

#堆排序
def heapSort(arr):
    global arrLen
    arrLen=len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen-=1
        heapify(arr,0)
    print(arr)

array=[34,32,56,45,78,98,48,100,115,1444,15149]
heapSort(array)
    
    
