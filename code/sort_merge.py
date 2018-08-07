a =  [3,53,632,3,52,35,23]

def merge(arr,start,mid,end):
    print("merge ",arr[start:mid],arr[mid:end])
    a = [None] * (end-start +1)
    k = 0
    p = start
    q = mid+1

    for i in range(start,end + 1):

        if(p > mid):
            a[k] = arr[q]
            q = q + 1

        elif (q > end):
            a[k] = arr[p]
            p = p + 1

        elif (arr[p] <arr[q]):
            a[k] = arr[p]
            p = p+1
        else :
            a[k] = arr[q]
            q = q + 1
        k = k + 1

    for p in range(0,k):
        arr[start] = a[p]
        start = start + 1



def merge_sort(a ,start,end):
    print("Merge sort", a[start:end])
    mid = int((start + end) / 2)
    if(start < end):

         merge_sort(a,start,mid)
         merge_sort(a,mid+1,end)
         merge(a,start,mid,end)

print(a)
merge_sort(a,0,len(a)-1)
print(a)
