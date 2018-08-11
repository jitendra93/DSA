
a = [3,53,632,3,52,35,23]

def selection_sort(a):
    passes = swaps = 0
    print(a)
    # temporary variable to store the position of minimum element
    pos_of_minimum = 0

    for i in range(0,len(a)):
        #assuming the first element to be the minimum of the unsorted array .
        pos_of_minimum = i

        # the effective size of array is i+1 to len(a)
        for j in range(i+1,len(a)):
            passes = passes + 1
            if(a[j]<a[pos_of_minimum]): #finds the minimum element
                pos_of_minimum = j

                if( i != pos_of_minimum):
                    swaps = swaps + 1
                    #putting minimum element on its proper position.
                    temp = a[i]
                    a[i] = a[pos_of_minimum]
                    a[pos_of_minimum] = temp
                    print("loop number",i,a)
                    print(a)

    print ("passes = ",passes)
    print("swaps = ",swaps)
selection_sort(a)

'''
[3, 53, 632, 3, 52, 35, 23]
loop number 0 [3, 53, 632, 3, 52, 35, 23]
loop number 1 [3, 3, 632, 53, 52, 35, 23]
loop number 2 [3, 3, 23, 53, 52, 35, 632]
loop number 3 [3, 3, 23, 35, 52, 53, 632]
loop number 4 [3, 3, 23, 35, 52, 53, 632]
loop number 5 [3, 3, 23, 35, 52, 53, 632]
loop number 6 [3, 3, 23, 35, 52, 53, 632]
[3, 3, 23, 35, 52, 53, 632]
passes =  21
swaps =  3

'''
