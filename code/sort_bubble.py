a = [2,53,23,52,56]


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
     print("Actual swaps = ",swap)
     break
print("total passes = ",passes)
