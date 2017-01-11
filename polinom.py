def factorial(n):
    rez = 1
    if n > 1:
        rez *= n * factorial(n-1)

    return rez


def m_elem(m, n):
    return factorial(n) // (factorial(m)*factorial(n-m))


def tetraeder(n):
    return n * (n + 1) * (n + 2) // 6


def string_trianlepaskal(n):
    zer = list()
    rez = list()

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

        # print(elem, end=" ")
        zer.append(elem)
        rez.append(elem)

    if n % 2 == 0:
        for each in zer[-2::-1]:
            # print(each, end=" ")
            rez.append(each)
    else:
        for each in zer[::-1]:
            # print(each, end=" ")
            rez.append(each)

    return rez


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    # k0a^nb^0 + k1a^n-1b^1+ ... + kna^0b^n - rezult formula
    k = string_trianlepaskal(n) # find koef k - n-string of triangule Pascal
    typing = ""
    rezult = 0
    for i in range(n+1):
        operand = k[i] * (a ** (n-i)) * (b ** i)
        if typing:
            typing += "+"
        if operand:
            if not k[i] == 1:
                typing += str(k[i])
            if not a ** (n-i) == 1:
                if typing and not typing[len(typing)-1] == "+":
                    typing += "*"
                typing += "a"
                if not (n-i) == 1:
                    typing += "^"
                    typing += str(n-i)
            if not b ** i == 1:
                if typing and not typing[len(typing)-1] == "+":
                    typing += "*"
                typing += "b"
                if not i == 1:
                    typing += "^"
                    typing += str(i)
        rezult += operand

    print(typing,"=",rezult)


main()