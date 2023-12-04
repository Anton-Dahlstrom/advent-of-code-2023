with open("day4/day4input.txt", "r") as file:
    left = True
    hmap = {}
    tempSum = 0
    total = 0
    for line in file:
        left, right = line.strip().split("|")
        for number in left.split(" "):
            if number.isnumeric():
                hmap[number] = 1
        for number in right.split(" "):
            if number in hmap:
                if tempSum:
                    tempSum = tempSum * 2
                else:
                    tempSum = 1
        hmap = {}
        total += tempSum
        tempSum = 0
print(total)
