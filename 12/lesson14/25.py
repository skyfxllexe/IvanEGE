def is_prime(n): # определяет простоту числа
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

count = 1
for i in range(245_690, 245_756+1):
    if is_prime(i) == True:
        print(count, i)
    count += 1
    