a = [1,4,6,7,8,23,56,344,444,552,634,764,866,879,999,3645,4567,6587,7890,9996,999999]


def ternary_search(a,left,right,key):
    if(left <= right):

        mid1 = left + int((right - left)/3)
        mid2 = right - int((right - left)/3)

        if(a[mid1] == key):
            return mid1
        elif a[mid2] == key:
            return mid2
        elif a[mid1] > key:
            return ternary_search(a,left,mid1-1,key)
        elif a[mid2] < key:
            return ternary_search(a,mid2 + 1, right,key)
        else:
            return ternary_search(a,mid1+1,mid2-1,key)

    return -1


print (a)
key = 9996
print ("searching for key " , key)

position = ternary_search(a,0,len(a),key)

print("Found at ",position)
