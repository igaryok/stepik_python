def div_num(x):
    return lambda y: True if y % x == 0 else False


def main():
    div6 = div_num(6)
    n = int(input().strip())
    suma = 0
    for _ in range(n):
        num = int(input().strip())
        if num % 6 == 0:
            suma += num

    print(suma)


# start program
main()