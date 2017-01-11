import itertools


def is_prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return False if count else True


def primes():
    start = 1
    while True:
        start += 1
        if is_prime(start):
            yield start




print(list(itertools.takewhile(lambda x : x <= 31, primes())))
print([1,2,3,4,5,6,7,8,9,10,11])