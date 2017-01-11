def gsd(a, b):
    while b:
        t = b
        b = a % b
        a = t

    return a


def lcm(a, b):
    return a // gsd(a, b) * b


def main():
    a, b = input().strip().split()
    print(lcm(int(a), int(b)))


# start program
main()