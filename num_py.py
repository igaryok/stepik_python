import numpy as np


def main():
    shape = tuple(int(x) for x in input().strip().split())
    data  = list()

    for _ in range(shape[0]):
        data.append(input().strip().split())

    matrix = np.array(data)

    tr_matrix = matrix.transpose()
    for line in tr_matrix:
        for each in line:
            print(each, end=" ")
        print("")


# start program
main()