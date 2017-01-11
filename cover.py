def main():
    n = int(input().strip())
    otr = list()
    for _ in range(n):
        a, b = map(int, input().strip().split())
        otr.append({i for i in range(a, b+1)})

    print(otr)
    rez = list()
    #rez.update(otr[0])

    for i in range(len(otr)-1):
        for j in range(i+1, len(otr)):
            rez.append(otr[i] & otr[j])

    print(rez)

main()