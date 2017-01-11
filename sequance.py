def main():
    number = int(input().strip())
    num = 1
    count = 0
    for _ in range(number):
        if count < num:
            count += 1
        else:
            num += 1
            count = 1

        print(num, end=" ")


# start program
main()