def rightmost_one_in_binary(num):
    return num ^ (num & (num -1))

def set_nth_bit(num,n):
    return num | (1<<n)

num = 13

print(num,rightmost_one_in_binary(num))
print(num,set_nth_bit(num,1))
