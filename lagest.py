def main():
    rezult = 0
    num = True
    while num:
        num = int(input().strip())
        if rezult < num:
            rezult = num

    print(rezult)


# start program
main()