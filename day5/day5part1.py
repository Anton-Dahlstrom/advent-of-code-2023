with open("day5/day5input.txt", "r") as file:
    numbers = []
    lines = file.readlines()
    for number in lines[0].strip().split(" "):
        if number.isdigit():
            numbers.append(int(number))
    next = [0]*len(numbers)
    ranges = []
    for line in lines:
        line = line.strip()
        if line:
            if line[0].isnumeric():
                for value in line.split(" "):
                    ranges.append(int(value))
                for i in range(0, len(numbers)):
                    if numbers[i] in range(ranges[1], ranges[1] + ranges[2]):
                        difference = numbers[i] - ranges[1]
                        if not next[i]:
                            next[i] = ranges[0] + difference
                ranges = []
            else:
                for i in range(0, len(next)):
                    if next[i]:
                        numbers[i] = next[i]
                next = [0]*len(numbers)

    for i in range(0, len(next)):
        if next[i]:
            numbers[i] = next[i]
    next = [0]*len(numbers)

print(min(numbers))