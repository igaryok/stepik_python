def min_max(minmax, num):
    if minmax[0] is None:
        minmax[0] = num
        minmax[1] = num
    else:
        if num > minmax[1]:
            minmax[1] = num
        if num < minmax[0]:
            minmax[0] = num

    return minmax


def main():
    string = input()
    num1 = ""
    num2 = ""
    item = 0
    minmax = [None, None] # first - minimum of numbers, second - maximum of numbers
    while item < len(string):
        if string[item].isdigit():
            num1 += string[item]
        else:
            if string[item] == "+": # if adding operation
                item += 1
                while item < len(string) and string[item].isdigit():
                    num2 += string[item]
                    item += 1
                if num1 and num2:
                    print(int(num1) + int(num2))
                    minmax = min_max(minmax, int(num1) + int(num2))
                    num1 = ""
                    num2 = ""
                elif num2:
                    print(int(num2))
                    minmax = min_max(minmax, int(num2))
                    num2 = ""
            elif string[item] == "-": # if subs operation
                item += 1
                while item < len(string) and string[item].isdigit():
                    num2 += string[item]
                    item += 1
                if num1 and num2:
                    print(int(num1) - int(num2))
                    minmax = min_max(minmax, int(num1) - int(num2))
                    num1 = ""
                    num2 = ""
                elif num2:
                    print(int(num2))
                    minmax = min_max(minmax, int(num2))
                    num2 = ""
            elif string[item] == "*": # if multiply operation
                item += 1
                while item < len(string) and string[item].isdigit():
                    num2 += string[item]
                    item += 1
                if num1 and num2:
                    print(int(num1) * int(num2))
                    minmax = min_max(minmax, int(num1) * int(num2))
                    num1 = ""
                    num2 = ""
                elif num2:
                    print(int(num2))
                    minmax = min_max(minmax, int(num2))
                    num2 = ""
            elif string[item] == "/": # if dividion operation
                item += 1
                while item < len(string) and string[item].isdigit():
                    num2 += string[item]
                    item += 1
                if num1 and num2:
                    print(int(num1) // int(num2))
                    minmax = min_max(minmax, int(num1) // int(num2))
                    num1 = ""
                    num2 = ""
                elif num2:
                    print(int(num2))
                    minmax = min_max(minmax, int(num2))
                    num2 = ""
            else:
                if num1:
                    print(int(num1))
                    minmax = min_max(minmax, int(num1))
                    num1 = ""
        item += 1

    if num1: # print last digits in string
        print(int(num1))
        minmax = min_max(minmax, int(num1))

    print("Max: ", minmax[1])
    print("Min: ", minmax[0])

main()