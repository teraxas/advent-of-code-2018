
def calculate_adjacent_taken_pos(plane_map: list[list], x, y):
    occupied_seats = 0
    for hx in range(x-1, x+2):
        if hx < 0 or hx >= len(plane_map[0]):
            continue
        for hy in range(y-1, y+2):
            if hx == x and hy == y:
                continue
            if hy < 0 or hy >= len(plane_map):
                continue

            value = plane_map[hy][hx]

            if value == '#':
                occupied_seats += 1

    return occupied_seats


def switching_round(plane_map: list[list]):
    plane_map_copy = list(map(lambda l: l.copy(), plane_map))
    changes_count = 0
    for x in range(0, len(plane_map_copy[0])):
        for y in range(0, len(plane_map_copy)):
            status = plane_map_copy[y][x]

            if status == '.':
                continue

            occupied_seats = calculate_adjacent_taken_pos(plane_map_copy, x, y)

            if status == 'L' and occupied_seats == 0:
                plane_map[y][x] = '#'
                changes_count += 1
            elif status == '#' and occupied_seats >= 4:
                plane_map[y][x] = 'L'
                changes_count += 1

    return changes_count


def print_map(plane_map: list[list[str]]):
    for line in plane_map:
        print("".join(line))


def solve(plane_map: list[list]):

    while True:
        changes_count = switching_round(plane_map)
        # print("---")
        # print("Changes: ", changes_count)
        # print_map(plane_map)
        if changes_count == 0:
            break

    occupied_count = 0
    for x in range(0, len(plane_map[0])):
        for y in range(0, len(plane_map)):
            status = plane_map[y][x]
            if status == '#':
                occupied_count += 1

    return occupied_count


input_file = open("2020/11/day11.input", "r")
content_list = list(map(lambda l: list(l.strip()), input_file.readlines()))
result = solve(content_list)
print(result)
