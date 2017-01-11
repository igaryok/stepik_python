def main():
    with open("code.txt") as file:
        string = file.read()

    group = ""
    number = ""
    rezult_string = ""
    for each in string:
        if each.isdigit():
            number += each
        else:
            if group:
                rezult_string += group * int(number)
                number = ""
                group = ""
            group += each
    else:
        rezult_string += group * int(number)

    with open("encode.txt", "w") as file:
        file.write(rezult_string)


# start program
main()