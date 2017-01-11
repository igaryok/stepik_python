def evklid(a, b):
    while a and b:
        if a > b:
            a -= b
        else:
            b -= a
    return a if a > 0 else b


def main():
    a, b = input().strip().split()
    print(evklid(int(a), int(b)))


# start program
main()