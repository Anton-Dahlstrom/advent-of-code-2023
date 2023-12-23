
with open("day15/day15input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip().split(",")
    total = 0
    for line in lines:
        for value in line:
            temp = 0
            for char in value:
                temp += ord(char)
                temp *= 17
                temp %= 256
            total += temp
print(total)