def factorial(n):
    rez = 1
    if n > 1:
        rez *= n * factorial(n-1)

    return rez

def m_elem(m, n):
    return factorial(n) // (factorial(m)*factorial(n-m))


def tetraeder(n):
    return n * (n + 1) * (n + 2) // 6


def main():
    n = int(input())
    zer = list()
    if n % 2 == 0:
        number = (n // 2) + 1
    else:
        number = n // 2
    for i in range(number):
        if i == 0 or i == n:
            elem = 1
        elif i == 1 or i == n-1:
            elem = n
        elif i == 2:
            elem = n * (n - 1) // 2
        elif i == 3:
            elem = tetraeder(n-2)
        else:
            elem = m_elem(i, n)

        print(elem, end=" ")
        zer.append(elem)

    if n % 2 == 0:
        for each in zer[-2::-1]:
            print(each, end=" ")
    else:
        for each in zer[::-1]:
            print(each, end=" ")


main()