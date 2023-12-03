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
