def sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    else:
        if a < 0 or b < 0:
            raise ValueError

    return int(a) + int(b)

print(sum("5", -6))