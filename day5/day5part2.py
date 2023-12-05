
with open("day5/day5input.txt", "r") as file:
    numbers = []
    lines = file.readlines()
    for number in lines[0].strip().split(" "):
        if number.isdigit():
            numbers.append(int(number))
    next = 0
    ranges = []
    lowest = 0
    while numbers:
        start = numbers.pop(0)
        steps = numbers.pop(0)
        for num in range(start, start+steps):
            for line in lines:
                line = line.strip()
                if line:
                    if line[0].isnumeric():
                        for value in line.split(" "):
                            ranges.append(int(value))
                        if num in range(ranges[1], ranges[1] + ranges[2]):
                            difference = num - ranges[1]
                            if not next:
                                next = ranges[0] + difference
                        ranges = []
                    else:
                        if next:             
                            num = next
                            next = 0
            if next:
                num = next
                next = 0
            if not lowest:
                lowest = num
            if num < lowest:
                lowest = num
print(lowest)
