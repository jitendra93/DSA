'''
Video to learn about this algo : https://www.youtube.com/watch?v=2fA1FdxNqiE
Heaps can be used in sorting an array. In max-heaps, maximum element will
always be at the root. Heap Sort uses this property of heap to sort the array.
'''
def max_heapify(arr,heap_size,root):
    print(arr,heap_size,root)
    largest = root
    left = (2 * root) + 1
    right = left + 1

    #Check if left child of root exists and is greater than the root
    if left < heap_size and arr[largest] < arr[left]:
        print("swapping ",left, largest)
        largest = left

    #Check if right child exists and is greater than the largest
    if right < heap_size and arr[largest] < arr[right]:
        print("swapping",right,largest)
        largest = right

    #detect change in largest
    if largest != root:
        print("largest not root swapping ",arr[root],arr[largest])
        arr[root], arr[largest] = arr[largest],arr[root]
        #heapify the root
        max_heapify(arr,heap_size,largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(int(n/2)-1,-1,-1):
        print("iteration ",i)
        max_heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        max_heapify(arr,i,0)


arr = [34,3,23,27]
print(arr)
heap_sort(arr)
print(arr)

'''
output
[34, 3, 23, 27]
iteration  1
[34, 3, 23, 27] 4 1
swapping  3 1
largest not root swapping  3 27
[34, 27, 23, 3] 4 3
iteration  0
[34, 27, 23, 3] 4 0
[3, 27, 23, 34] 3 0
swapping  1 0
largest not root swapping  3 27
[27, 3, 23, 34] 3 1
[23, 3, 27, 34] 2 0
[3, 23, 27, 34] 1 0
[3, 23, 27, 34]

'''
