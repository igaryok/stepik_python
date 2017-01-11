def main():
    rezult_list = list()
    while True:
        rezult_list.append(int(input()))
        if sum(rezult_list) == 0:
            break

    summa2 = 0
    for each in rezult_list:
        summa2 += each ** 2

    print(summa2)


# start program
main()