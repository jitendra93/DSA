a =  [3,53,632,3,52,35,23]

def bubble_sort(a):
    swap =0
    passes = 0
    for i in range(0,len(a)):
        is_sorted = True
        for j in range(0,len(a) - i - 1):
            passes = passes + 1
            print(a[j] , a)
            if(a[j] > a[j+1]):
                swap= swap+1
                is_sorted = False
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                if is_sorted:
                    break
    print("total passes = ",passes)
    print("Actual swaps = ",swap)
bubble_sort(a)
'''
2 [2, 53, 23, 52, 56]
53 [2, 53, 23, 52, 56]
53 [2, 23, 53, 52, 56]
53 [2, 23, 52, 53, 56]
2 [2, 23, 52, 53, 56]
23 [2, 23, 52, 53, 56]
52 [2, 23, 52, 53, 56]
Actual swaps =  2
total passes =  7
'''
