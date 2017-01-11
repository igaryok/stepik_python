def resheto_er(n=2750160):
    #n = 2750160
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1

    return lst

def main():
    n = int(input().strip())
    numbers_prime = input().strip().split()
    rez = resheto_er()
    for each in numbers_prime:
        print(rez[int(each)-1], end=" ")


# start program
main()