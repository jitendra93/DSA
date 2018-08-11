
import cProfile


BIG_POWER_OF_TWO= int(5.357543035931337e+300)

def is_power_of_base_n(x,base):
    if(x == 0 or base ==0):
        raise Exception("Invalid inputs")
    while x % base == 0:
        x = int (x/base)
    return x == 1

base = 2
# print (f" 72 is power of {base} ",is_power_of_base_n(72,base))
# print (f" 512 is power of {base} ",is_power_of_base_n(512,base))
# print (f" 1024 is power of {base} ",is_power_of_base_n(1024,base))
#


def is_power_of_two(x):
    return x and not(x & (x-1))


def number_of_ones_in_binary(num):
    count = 0
    while num :
        num = num & (num -1)
        count+=1
    return count

num = 15
print("No. of ones in binary of ",num ," is ",number_of_ones_in_binary(num) )



def check_ith_bit_is_set(num, i):
    return (num & (1 << i)) != False

i = int(input("ith bit "))
print("Checking if ith bit is set for ",num,check_ith_bit_is_set(num,i))

# print (f" 512 is power of {base} ",is_power_of_two(512))

cProfile.run('is_power_of_base_n(BIG_POWER_OF_TWO,2)')
cProfile.run('is_power_of_two(BIG_POWER_OF_TWO)')
