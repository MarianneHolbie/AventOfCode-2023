#####################
#     Part One      #
#####################

# Open and read File
with open('input.txt', "r") as file:
    # store lines in a list
    lines = file.readlines()
    game_sum = 0

    # read each line
    for line in lines:
        possible_game = True
        # separate game infos and results
        games, results = line.split(":")
        # split number of game
        game, number_game = games.split()

        # separate results
        for result in results.split(";"):

            # separate each set of cubes
            for cubes in result.split(","):

                # separate color and count of each set
                count, color = cubes.split()

                if (color == "red" and int(count) > 12) or (color == "green" and int(count) > 13) or (color == "blue" and int(count) > 14):
                    possible_game = False

        if possible_game:
            game_sum += int(number_game)
    print(game_sum)

#####################
#     Part Two      #
#####################

# Open and read File
with open('input.txt', "r") as file:
    # store lines in a list
    lines = file.readlines()
    game_power = 0

    # read each line
    for line in lines:
        possible_game = True
        # separate game infos and results
        games, results = line.split(":")
        # split number of game
        game, number_game = games.split()
        max_red = 1
        max_green = 1
        max_blue = 1

        # separate results
        for result in results.split(";"):

            # separate each set of cubes
            for cubes in result.split(","):

                # separate color and count of each set
                count, color = cubes.split()

                if color == "red" and int(count) > max_red:
                    max_red = int(count)
                if color == "green" and int(count) > max_green:
                    max_green = int(count)
                if color == "blue" and int(count) > max_blue:
                    max_blue = int(count)

        game_power += (max_red * max_green * max_blue)
    print(game_power)