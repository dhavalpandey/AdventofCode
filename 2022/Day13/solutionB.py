with open("..\..\Inputs\Day 13\Day13Input.txt", "r") as f:
    input_file = f.read().strip().split()

from ast import literal_eval

arr = []
index_of_arr_in_order = []


def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    for a, b in zip(x, y):
        v = compare(a, b)
        if v:
            return v

    return len(x) - len(y)


def parse():
    for list in input_file:
        arr.append(literal_eval(list))


def main():
    parse()

    i2 = 1
    i6 = 2

    for a in arr:
        if compare(a, [[2]]) < 0:
            i2 += 1
            i6 += 1
        elif compare(a, [[6]]) < 0:
            i6 += 1

    print(i2 * i6)


main()
