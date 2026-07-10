# 3 parts in lc

squares = [i for i in range(1,21) if i % 2 == 0 ]
print(squares)

# Square no. btw 1 -20 which are divisible bt 3 and 5

squares = [i for i in range(1,101) if i % 3 == 0 or i % 7 == 0]
print(squares)


# From 1 to 100, make a list of prime numbers
def is_prime(num):
    factors = 0
    for i in range(1,101):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False
prime_no = [i for i in range(1,101) if is_prime(i)]
print(prime_no)