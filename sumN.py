def main():
    n = int(input())
    i = 1
    suma = 0;
    ls = list()
    while(suma < n):
        suma += i
        ls.append(i)
        i += 1

    if not suma == n:
        ls.remove(suma - n)

    print(len(ls))
    print(" ".join(map(str, ls)))


main()