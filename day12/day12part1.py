
def charReplace(text, index, value):
    # print(index)
    # print("HERE", text)
    finished = str(text[:index]) + value + str(text[index + 1:])
    # print("AFTER", finished)
    return finished

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
    values = []
    num = 0
    temp = []
    for spring in springs:
        for char in spring[0]:
            if char == "#":
                num += 1
            else:              
                if num:
                    temp.append(num)
                    num = 0
        if temp:
            values.append(temp)
            temp = []
    values.reverse()

    permutations = []
    for i, spring in enumerate(springs):
        goalCount = 0
        consecutive = 0
        adding = False
        goal = int(spring[1][goalCount])
        upcoming = 0
        stop = len(spring[0])
        tempPerm = spring[0]
        for i, char in enumerate(spring[0]):
            
        # If we find the amount of broken springs we are looking for we break, reset consecutive counter and search for the next goal.
            if consecutive == goal:
                consecutive = 0
                if goalCount < len(spring[1])-1:
                    goalCount += 1
                    goal = int(spring[1][goalCount])
                else:
                    break
                tempPerm = charReplace(tempPerm, i, ".")
                continue

            if char == "#":
                consecutive += 1
                continue
            if char == "?":
                open = 0
                guaranteed = 0  
                for x in spring[0][i+1:]:
                    if x == ".": 
                        break
                    open += 1
                for y in spring[0][i+1:]:
                    if y != "#":
                        break
                    guaranteed += 1 

                if consecutive + open +1 >= goal:
                    if consecutive + guaranteed + 1 <= goal:
                        tempPerm = charReplace(tempPerm, i, "#")
                        consecutive += 1
                        continue
            consecutive = 0
        print(tempPerm)

    # Find a way to create one solution, then work with pointers to create the rest. Count how many you can create.
        