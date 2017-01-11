def resheto_er():
    n = 2750160
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            yield a[i], lst.index(a[i])+1
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1

def primeof(gen, number):
    rez = next(gen)
    while not rez[1] == number:
        rez = next(gen)

    return rez[0]

def main():
    n = int(input().strip())
    numbers_prime = input().strip().split()
    g = resheto_er()
    for item in range(n):
        rez = primeof(g, int(numbers_prime[item]))
        print(rez, end=" ")


# start program
main()