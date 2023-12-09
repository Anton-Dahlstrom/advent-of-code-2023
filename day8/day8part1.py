import re
with open("day8/day8input.txt", "r") as file:
    values = {"T": 10, "J": 11, "Q": 12, "K": 13}

    lines = file.readlines()
    hmap = {}
    current = "AAA"
    for line in lines:
        row = re.sub("[^a-zA-Z ]", "", line).split()
        if len(row) == 3:
            hmap[row[0]] = {"L": row[1], "R": row[2]}
    count = 0
    while current != "ZZZ":
        for char in lines[0].strip():
            count += 1
            current = hmap[current][char]
print(count)
