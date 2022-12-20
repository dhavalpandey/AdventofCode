with open("../../Inputs/Day 15/input.txt", "r") as f:
    input_file = f.read().strip().split("\n")

sensors_cords = []
beacons_cords = []


def remove(string):
    temp = string.replace(",", "")
    temp1 = temp.replace(":", "")
    temp2 = temp1.replace("y=", "")
    return temp2.replace("x=", "")


def parse():
    for line in input_file:
        line_cleaned = line.split()

        sx, sy = remove(line_cleaned[2][2:]), remove(line_cleaned[3][2:])
        bx, by = remove(line_cleaned[len(line_cleaned)-2][2:]), remove(line_cleaned[len(line_cleaned)-1][2:])

        sensor_cord = (int(sx), int(sy))
        beacon_cord = (int(bx), int(by))

        sensors_cords.append(sensor_cord)
        beacons_cords.append(beacon_cord)


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    parse()
    sensors = sensors_cords
    beacons = beacons_cords

    N = len(sensors)
    dists = []

    for i in range(N):
        dists.append(dist(sensors[i], beacons[i]))

    Y = 2000000

    intervals = []

    for i, s in enumerate(sensors):
        dx = dists[i] - abs(s[1] - Y)

        if dx <= 0:
            continue

        intervals.append((s[0] - dx, s[0] + dx))

    allowed_x = []
    for bx, by in beacons:
        if by == Y:
            allowed_x.append(bx)

    min_x = min([i[0] for i in intervals])
    max_x = max([i[1] for i in intervals])

    ans = 0
    for x in range(min_x, max_x + 1):
        if x in allowed_x:
            continue

        for left, right in intervals:
            if left <= x <= right:
                ans += 1
                break

    print(ans)


main()
