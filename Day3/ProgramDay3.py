#####################
#     Part One      #
#####################

import re


# function to test if a character is a special character
def is_special_character(char):
    return bool(re.match(r'[^a-zA-Z0-9.]', char))


with open('input.txt', 'r') as f:
    lines = f.readlines()

    total_sum = 0

    for j in range(len(lines)):
        line = lines[j]
        number = ""
        # flag to check if there is a special character adjacent to the number
        flag = False

        for i in range(len(line)):
            character = line[i]

            if character.isdigit():
                number += character

                # define all position of adjacent
                position = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
                for x, y in position:
                    if (j + x) in range(len(lines)) and (i + y) in range(len(lines[0])):
                        if is_special_character(lines[j + x][i + y]) and lines[j + x][i + y] != '\n':
                            flag = True
                            break
            else:
                if len(number) > 0 and flag:
                    total_sum += int(number)
                flag = False
                number = ""

print(f"Sum of every number adjacent to a symbol: {total_sum}")


#####################
#     Part Two      #
#####################


def find_gear_positions(row, col):
    positions = [[0, -1], [-1, 0], [1, 0], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    adjacent_positions = []

    for x, y in positions:
        if (row + x) in range(len(lines)) and (col + y) in range(len(lines[0])):
            if lines[row + x][col + y] == "*":
                adjacent_positions.append([row + x, col + y])
    return adjacent_positions


with open('input.txt') as f:
    lines = f.readlines()

    total_gear_ratio = 0
    gear_data = [[[1, 0]] * len(lines[0]) for _ in range(len(lines))]
    for j in range(len(lines)):
        line = lines[j]
        num = ""
        flag = []
        for i in range(len(line)):
            character = line[i]

            if character.isdigit():
                num += character
                flag.extend(find_gear_positions(j, i))
            else:
                visit = []
                for x in flag:
                    if x not in visit:
                        visit.append(x)
                if len(num) > 0 and len(visit) > 0:
                    for x, y in visit:
                        gear_data[x][y] = [gear_data[x][y][0] * int(num), gear_data[x][y][1] + 1]
                    print(i, j, gear_data[x][y])
                flag = []
                num = ""

    for i in range(len(gear_data)):
        for j in range(len(gear_data[0])):
            if gear_data[i][j][1] == 2:
                total_gear_ratio += gear_data[i][j][0]

    print(total_gear_ratio)
