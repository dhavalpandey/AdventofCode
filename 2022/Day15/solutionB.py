import sys
file_name = "input.in"

if len(sys.argv) == 2:
    file_name = "sample.in"

with open('./'+file_name, 'r') as f:
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

    pos_lines = []
    neg_lines = []

    for i, s in enumerate(sensors):
        d = dists[i]
        neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
        pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

    pos = None
    neg = None

    for i in range(2 * N):
        for j in range(i + 1, 2 * N):
            a, b = pos_lines[i], pos_lines[j]

            if abs(a - b) == 2:
                pos = min(a, b) + 1

            a, b = neg_lines[i], neg_lines[j]

            if abs(a - b) == 2:
                neg = min(a, b) + 1

    x, y = (pos + neg) // 2, (neg - pos) // 2
    ans = x * 4000000 + y
    print(ans)


main()
