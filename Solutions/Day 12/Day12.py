from collections import deque

with open("..\..\Inputs\Day 12\Day12Input.txt", "r") as f:
    input_file = f.read().strip().split("\n")

height_map = [list(line) for line in input_file]
grid = []
n = 0
m = 0


def convert_to_int_map():
    global grid, n, m
    for row in input_file:
        temp1 = row.replace("S", "a")
        temp2 = temp1.replace("E", "z")
        row_height_map = []

        chars = list(temp2)

        for char in chars:
            num = ord(char) - 97
            row_height_map.append(num)

        grid.append(row_height_map)

    n = len(grid) - 1
    m = len(grid[0]) - 1


def main():
    global grid, n, m

    convert_to_int_map()

    for r, row in enumerate(height_map):
        for c, item in enumerate(row):
            if item == "S":
                sr = r
                sc = c
                height_map[r][c] = "a"
            if item == "E":
                er = r
                ec = c
                height_map[r][c] = "z"

    q = deque()
    q.append((0, sr, sc))

    vis = {(sr, sc)}

    while q:
        d, r, c = q.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if (nr, nc) in vis:
                continue
            if grid[nr][nc] - grid[r][c] > 1:
                continue
            if nr == er and nc == ec:
                print(d + 1)
                exit(0)
            vis.add((nr, nc))
            q.append((d + 1, nr, nc))


main()
