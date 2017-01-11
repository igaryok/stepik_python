import json


def find_foo(item):
    suma = 0
    if type(item) is dict:
        if item.get("foo"):
            suma += item["foo"]
        for each in item:
            if type(item[each]) is dict or type(item[each]) is list:
                suma += find_foo(item[each])
    elif type(item) is list:
        for each in item:
            suma += find_foo(each)

    return suma


def main():
    suma = 0
    with open("file.txt") as file:
        text = file.read()

    inputs = json.loads(text)
    print(inputs)
    if type(inputs) is dict:
        for each in inputs:
            suma += find_foo(inputs[each])
    else:
        for each in inputs:
            suma += find_foo(each)

    print(suma)


# start program
main()