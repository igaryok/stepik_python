def sum_dig(number):
    # number is digit in string format
    sum = 0
    for each in number:
        sum += int(each)

    return sum


def find_number(number):
    sum = sum_dig(number)
    count = 0
    for each in range(int(number)):
        if sum == sum_dig(str(each)):
            count += 1
    return count


def main():
    num = input().strip()
    print(find_number(num))


# start program
main()