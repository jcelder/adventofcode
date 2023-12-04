import aoc_lube

# get_calibration_value(line: String)
def get_calibration_value(line):
    # create first and initialize to None
    first = None
    # create second and initialize to None
    second = None
    # iterate over the line, starting at the beginning and iterating up to (length of line/2)
    for i in range(len(line)):
        end = len(line) - 1 - i
        # if first is none and if value at i is a digit
        if first == None and line[i].isdigit():
            # set first to the value of the string at i
            first = line[i]
        # if second is none and if value at length of (line - 1 - i) is a digit
        if second == None and line[end].isdigit():
            # set second to the value of the string at (line - 1 - i)
            second = line[end]
        # if first and second are numbers
        if first != None and second != None:
            # break out of the loop
            break
    # create calibration value string by concatenating first and second
    # parse to int to convert string to number
    # return calibration value
    if first == None and second == None:
        print(line)
    return int(first + second)

# get_sum_of_calibration_values()
def get_sum_of_calibration_values():
    # Get input string
    # Split input string into substrings separated by newline characters
    lines = aoc_lube.fetch(2023,1).splitlines()
    print(len(lines))
    # Create variable to keep track of current sum
    sum = 0
    # for each line in list of lines
    for line in lines:
        # get the calibration value for that individual string
        # add the value to the sum
        sum += get_calibration_value(line)
    # return the current sum
    return sum

print(get_sum_of_calibration_values())