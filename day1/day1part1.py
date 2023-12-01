with open("day1/day1input.txt", "r") as file:
    total = 0
    for line in file:
        toAdd = ""
        for letter in line.strip():
            if letter.isnumeric():
                toAdd += letter
                break
        for letter in line.strip()[::-1]:
            if letter.isnumeric():
                toAdd += letter
                break
        toAdd = int(toAdd)
        total += toAdd
    print(total)