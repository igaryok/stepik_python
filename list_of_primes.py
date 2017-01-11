def is_prime(n, range_div):
    count = 0
    if (n > 10) and (n % 10 == 5):
        count = 1
    else:
        i = 0
        while range_div and n >= range_div[i] * range_div[i]:
            if n % range_div[i] == 0:
                count = 1
                break
            i += 1

    return False if count else True


def primes():
    rez = 1
    pozition = 0
    list_primes = []
    while True:
        rez += 1
        if is_prime(rez, list_primes):
            pozition += 1
            list_primes.append(rez)
            yield rez, pozition



def primeof(gen, number):
    rez = next(gen)
    while not rez[1] == number:
        rez = next(gen)

    return rez[0]


def main():
    n = int(input().strip())
    numbers_prime = input().strip().split()
    g = primes()
    for item in range(n):
        rez = primeof(g, int(numbers_prime[item]))
        print(rez, end=" ")


# start program
main()