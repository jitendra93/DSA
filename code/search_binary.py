a = [1,4,6,7,8,23,56,344,3645,9996,999999]


def binary_search(a,key,low,high):
    while low <= high:
        mid = int((low + high)/2)
        #print(low,mid,high)
        if(a[mid] < key):
            low = mid + 1
        elif(a[mid]>key):
            high = mid - 1
        else:#if(a[mid] == key):
            return mid
    return -1


print (a)
key = 56
print ("searching for key " , key)

position = binary_search(a,key,0,len(a))

print("Found at ",position)
