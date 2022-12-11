import math

with open('../../Inputs/Day 11/Day11Input.txt', 'r') as f:
    input = f.read().strip().split("\n")

starting_arr = []

# Input details
formulas = []
items = []
new_items = [[], [], [], []]
div = []
true_monkey_id = []
false_monkey_id = []

# Tracking vars
curr_monkey_num = 0
curr_round = 0
temp_num = 2


def create_starting_arr():
    global starting_arr, input, items

    for i in range(len(input)):
        if input[i][0:6] == 'Monkey':
            temp = input[i + 1].strip().split()[2:]
            str = ' '.join(temp)
            new_str = str.replace(",", "")
            arr = new_str.strip().split()
            final = [int(num) for num in arr]

            starting_arr.append(final)
            items = starting_arr


def parse_input():
    global input, curr_monkey_num, items, curr_round, starting_arr, temp_num, div, formulas, true_monkey_id, \
        false_monkey_id

    while temp_num != len(input):
        if input[temp_num] == "":
            temp_num += 3
        else:
            if input[temp_num][0:12] == "  Operation:":
                temp_formula = input[temp_num][19:]
                formula = temp_formula.strip().split()
                formulas.append(formula)

            elif input[temp_num][0:7] == "  Test:":
                divisible_by = int(input[temp_num][21:])
                div.append(divisible_by)

            elif input[temp_num][0:12] == "    If true:":
                monkey_id = int(input[temp_num][29])
                true_monkey_id.append(monkey_id)

            else:
                monkey_id = int(input[temp_num][30])
                false_monkey_id.append(monkey_id)
            temp_num += 1


def solve_q1():
    create_starting_arr()
    parse_input()

    global input, curr_monkey_num, items, curr_round, starting_arr, temp_num, div, formulas, true_monkey_id, \
        false_monkey_id, new_items

    # Solution
    for i in range(len(items)):
        for j in range(len(items[i])):
            curr_num = items[i][j]
            temp_formula = formulas[i]
            curr_formula = ''.join(temp_formula)
            curr_monkey_id_if_true = true_monkey_id[i]
            curr_monkey_id_if_false = false_monkey_id[i]

            execute = curr_formula.replace('old', str(curr_num))
            new_num = eval(execute)
            test_int = div[i]

            if math.floor(new_num / 3) % test_int == 0:
                items[i].pop(j)
                items[curr_monkey_id_if_true].append(math.floor(new_num / 3))
            else:
                items[i].pop(j)
                items[curr_monkey_id_if_false].append(math.floor(new_num / 3))

    print(new_items)


solve_q1()
