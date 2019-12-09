# 1.插入排序算法:
def insertion_sort(sort_list):
    iter_len=len(sort_list)
    if iter_len<2:
        return sort_list
    for i in range(1,iter_len):
        key=sort_list[i]
        j=i-1
        while j>=0 and sort_list[j]>key:
            sort_list[j+1]=sort_list[j]
            j-=1
            sort_list[j+1]=key
    return sort_list

a=[14,17,15,13,12,18,11]
print("使用插入排序的算法计算数组a得到的结果是",insertion_sort(a))


# 2.选择排序算法:
def selection_sort(sort_list):
	iter_len = len(sort_list)
	if iter_len < 2:
		return sort_list
	for i in range(iter_len-1):
		smallest = sort_list[i]
		location = i
		for j in range(i, iter_len):
			if sort_list[j] < smallest:
				smallest = sort_list[j]
				location = j
				if i != location:
					sort_list[i], sort_list[location] = sort_list[location], sort_list[i]
	return sort_list

b=[4,7,5,3,2,8,1]
print("使用选择排序算法计算的数组b的结果是",selection_sort(b))

# 3.冒泡排序算法：
def bubble_sort(sort_list):
	iter_len = len(sort_list)
	if iter_len < 2:
		return sort_list
	for i in range(iter_len-1):
		for j in range(iter_len-i-1):
			if sort_list[j] > sort_list[j+1]:
				sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
	return sort_list

c=[41,71,51,31,21,81,11]
print("使用冒泡排序算法计算的数组b的结果是",bubble_sort(c))