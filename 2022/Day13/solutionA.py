with open("..\..\Inputs\Day 13\Day13SampleInput.txt", "r") as f:
    input_file = f.read().strip().split()

from ast import literal_eval

temp = []
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


def convert(list):
    return tuple(list)


def parse():
    for list in input_file:
        temp.append(literal_eval(list))


def main():
    parse()

    for i in range(0, len(temp), 2):
        sub_arr_1 = temp[i]
        sub_arr_2 = temp[i + 1]

        pair = [sub_arr_1, sub_arr_2]

        arr.append(convert(pair))

    num_of_pairs = len(arr)

    for i in range(num_of_pairs):
        pair_to_search = arr[i]
        arr_1 = pair_to_search[0]
        arr_2 = pair_to_search[1]

        if compare(arr_1, arr_2) < 0:
            index_of_arr_in_order.append(i)

    total = 0
    for index in index_of_arr_in_order:
        total += index+1

    print(total)


main()
