def sum_loop(list_int):
    rez = 0
    for each in list_int:
        rez += int(each)

    return(rez)


def main():
    num_list = input().split()
    print(sum_loop(num_list))


# start program
main()