import math


def len_dots(A1, A2):
    return math.sqrt((A1[0] - A2[0]) ** 2 + (A1[1] - A2[1]) ** 2)


def main():
    dots = {
        "A1": [],
        "A2": [],
        "A3": [],
        "A4": []
    }

    for n in range(1, 5):
        string = input().strip().split()
        dots["A" + str(n)].append(float(string[0]))
        dots["A" + str(n)].append(float(string[1]))

    print(round(len_dots(dots["A1"], dots["A2"]) * len_dots(dots["A2"], dots["A3"]), 3))


# start program
main()