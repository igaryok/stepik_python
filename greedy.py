def greedy(backpack, w):
    sum = 0.0
    cost = 0.0
    for each in sorted(backpack.items(), key=lambda x: x[1][2], reverse=True):
        print(each)
        if sum + each[1][1] <= w:
            sum += each[1][1]
            cost += each[1][0]
        else:
            ostatok = w - sum
            sum += ostatok
            cost += ostatok * each[1][2]

    return cost


def main():
    n, w = map(int, input().strip().split())
    backpack = {}
    for i in range(n):
        cost, volume = input().strip().split()
        backpack[i] = [float(cost), float(volume), float(cost) / float(volume)]

    rezult = greedy(backpack, float(w))
    print("{0:.3f}".format(rezult))


# start program
main()