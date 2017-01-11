def filter_positive(list_of_number):
    new_list = list()
    for each in list_of_number:
        if each > 0:
            new_list.append(each)

    return new_list


def main():
    in_list = input().strip().split()
    for n in range(len(in_list)):
        in_list[n] = int(in_list[n])

    print(filter_positive(in_list))


# start program
main()