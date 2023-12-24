
with open("day15/day15input.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines = lines[i].strip().split(",")
    total = 0
    for slot in lines:     
        label = slot[0:2]
        operator = slot[2]
        if slot[2] == "=":
            value = slot[3]
