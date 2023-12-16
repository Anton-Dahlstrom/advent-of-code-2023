with open("day12/day12input.txt", "r") as file:
    lines = file.readlines()
    springs = []
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        spring, nums = lines[i].split(" ")
        numArray=[]
        for num in nums.split(","):
            numArray.append(int(num))
        springs.append([spring, numArray])
    for a in springs:
        print(a)