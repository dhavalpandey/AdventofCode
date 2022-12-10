def clean_input():
    global input_file
    global index_to_add_data

    for i in range(len(input_file) - 1):
        command = input_file[i][0:4]
        if command == 'addx':
            index_to_add_data.append((i + 1) + len(index_to_add_data))

    last_index = input_file[-1][0:4]
    if last_index == 'addx':
        index_to_add_data.append(len(input_file) + len(index_to_add_data))

    for index_to_push in index_to_add_data:
        input_file.insert(index_to_push, 'addx 0')


with open('../../Inputs/Day 10/Day10Input.txt', 'r') as f:
    input_file = f.read().strip().split("\n")
    index_to_add_data = []
    # clean_input()

X = 1

interesting = [20, 60, 100, 140, 180, 220]
op = 0
ans = 0


def solve_q1():
    global input_file, X, op, interesting, ans
    for line in input_file:
        parts = line.split(" ")

        if parts[0] == "noop":
            op += 1

            if op in interesting:
                ans += op * X

        elif parts[0] == "addx":
            V = int(parts[1])
            X += V

            op += 1

            if op in interesting:
                ans += op * (X - V)

            op += 1

            if op in interesting:
                ans += op * (X - V)


solve_q1()
print(ans)
