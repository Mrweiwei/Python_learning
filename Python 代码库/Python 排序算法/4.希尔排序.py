#希尔排序（算法还需研究没太明白）
def shellSort(arr):
    import math
    gap=1
    while(gap<len(arr)/3):
        gap=gap*3+1
    while gap>0:
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i-gap
            while j>=0 and arr[j]>temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap]=temp
        gap=math.floor(gap/3)
    return arr


arr=[123,3245,456,567,345,1234,32546547,56875]
print(shellSort(arr))
