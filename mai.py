def create_dic(dic, string):
    a = string.split(" - ")
    dic[a[0]] = a[1].split(", ")


def rez_dic(dic, dic2):
    for key, item in dic.items():
        for each in item:
            if each not in dic2.keys():
                dic2[each] = list()

            dic2[each].append(key)


def main():
    lat_dic = {}
    span_dic = {}
    num = int(input().strip())
    for _ in range(num):
        create_dic(lat_dic, input().strip())

    rez_dic(lat_dic, span_dic)
    print(len(span_dic))
    for key, item in sorted(span_dic.items(), key = lambda x: x[0]):
        print(key + " - ", end="")
        item.sort()
        for each in item:
            if each == item[-1]:
                print(each)
            else:
                print(each + ", ", end="")

# start program
main()
