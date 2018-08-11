a = [1,4,6,7,8,23,56,344,444,552,634,764,866,879,999,3645,4567,6587,7890,9996,999999]

def binary_search(a,key,low,high):
    while low <= high:
        mid = int((low + high)/2)
        #print(low,mid,high)
        if(a[mid] < key):
            low = mid + 1
        elif(a[mid]>key):
            high = mid - 1
        else:
            return mid
    return -1


print (a)
key = 6
print ("searching for key " , key)

position = binary_search(a,key,0,len(a))

print("Found at ",position)
