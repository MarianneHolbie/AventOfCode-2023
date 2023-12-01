
#####################
#     Part One      #
#####################

# initialize sum
finalSum = 0

# Open and read File
with open('input.txt', "r") as file:
    lines = file.readlines()

    # read each line
    for line in lines:
        # add number if char is digit
        numbers = [char for char in line if char.isdigit()]

        if numbers:
            finalNumber = numbers[0]  # Initialize with the first digit
            if len(numbers) > 1:
                finalNumber += numbers[-1]  # Concatenate the last digit if there is more than one digit
            else:
                finalNumber += numbers[0]
            finalSum += int(finalNumber)

print(f"Total sum of first and last digits: {finalSum}")

#####################
#     Part Two      #
#####################

# Tips : if you replace only by number sometimes you cut essential char for another number word

# construct dict with corresponding replacement string
dict = {'one': 'o1e', 'two': 't2w', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t',
        'nine': 'n9e'}

# Replace word by digit in each line
for i, line in enumerate(lines):
    for word in dict:
        if word in line:
            line = line.replace(word, dict[word])
    lines[i] = line  # update lines

# Recalculate the sum after replacing words with numbers
updatedSum = 0
finalNumber = 0
numbers = []
for line in lines:
    numbers = [char for char in line if char.isdigit()]

    if numbers:
        finalNumber = numbers[0]  # Initialize with the first digit
        if len(numbers) > 1:
            finalNumber += numbers[-1]  # Concatenate the last digit if there is more than one digit
        else:
            finalNumber += numbers[0]
        print(finalNumber)
        updatedSum += int(finalNumber)

print(f"Total sum after replacing words: {updatedSum}")
