def lage_exp(num):
    rezult_exp = 2
    exp = 1
    while True:
        rezult_exp *= 2
        if rezult_exp > num:
            break
        else:
            exp +=1

    return exp


def main():
    list_int = list()
    num = int(input().strip())
    for _ in range(num):
        list_int.append(int(input()))

    for each in list_int:
        print(lage_exp(each))


# start program
main()