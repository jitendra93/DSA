a = [3,53,632,3,52,35,23]


#assuming that left side of current element is always sorted
def insertion_sort(a):
    passes = 0
    swaps = 0
    for i in range(0,len(a)):

        # storing current element whose left side is checked for its
        #         correct position .

        temp = a[i]
        j = i

        # check whether the adjacent element in left side is greater or
        #         less than the current element.
        while (j > 0  and temp < a[j-1]):
            passes = passes +1
            swaps = swaps +1
            a[j] = a[j-1]
            j = j-1
            a[j] = temp
            print(a)

    print("passes ",passes)
    print("swaps ",swaps)

insertion_sort(a)
