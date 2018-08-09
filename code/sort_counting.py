
'''
In Counting sort, the frequencies of distinct elements of the array to be
sorted is counted and stored in an auxiliary array, by mapping its value
as an index of the auxiliary array.
'''


'''
a -> unsorted array
aux -> auxiliary array
sorted_a

'''
def counting_sort(a , aux , sorted_a):

    N = len(a)

    # Find the max value in K
    k = 0
    for i in range(N):
        k = max(k,a[i])


    #Initialize the elements of Aux[] with 0
    aux = [0] * (k+1)

    print(aux)
    #Store the frequencies of each distinct element of A[],
    # by mapping its value as the index of Aux[] array
    for i in range(N):
        aux[a[i]] = aux[a[i]] + 1


    j = 0
    for i in range(k+1):
        temp = aux[i]
        #Aux stores which element occurs how many times,
        #Add i in sortedA[] according to the number of times i occured in A[]
        while temp > 0:
            print(i,j,sorted_a)
            sorted_a[j] = i
            temp = temp -1
            j+=1




a = [1,4,32,52,124,543,2,6]
aux = []
sorted_a = [None] * len(a)
print(a)
counting_sort(a,aux,sorted_a)
print(sorted_a)
