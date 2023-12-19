# Find a way to create one solution, then work with pointers to create the rest. Count how many you can create.
# Implement multiple loops over the same string to find all permutations. 
# Needs to start at the correct goal, change index that we turned broken into a working spring and keep going until it fails the first time.
# Then we look at the previous goal until there are no more.

def charReplace(text, index, value):
    finished = str(text[:index]) + value + str(text[index + 1:])
    return finished

with open("day12/day12input.txt", "r") as file:
    lines = file.readlines()
    springs = []
    for j in range(0, len(lines)):
        lines[j] = lines[j].strip()
        spring, nums = lines[j].split(" ")
        goalNums=[]
        for num in nums.split(","):
            goalNums.append(int(num))
        springs.append([spring, goalNums])


    indexes = []
    for i, spring in enumerate(springs):
        # Index of current goal, value of first goal and the counter for found broken springs.
        goalIndex = 0
        goal = int(spring[1][goalIndex])
        consecutive = 0

        # The temparary string with current solution and a temporary array that saves index where the first change of a sequence is made
        # and the index of the goal it fulfilled.
        solutionString = spring[0]
        changes = []
        # Saves the index of the first change. If no changes were made it's set below zero to indicate the goal was solved without changes.
        changeIndex = -1

        # If we found a permutation that fulfills all our goals, turn the beginning of the last sequence of broken springs into a 
        # working spring then iterate through the remainder of the original string while trying to fit in the goal that the removed 
        # sequence of springs solved. 
        # When this fails to fulfill all goals we move backwards removing the last and second last sequence of broken springs and
        # turning the first broken spring of the first sequence into a working spring.
        # Reapeat until we've found all possible permutations that fulfill all goals.
         
        for j, char in enumerate(spring[0]):            
            # If we find the amount of broken springs we are looking for we break, reset consecutive counter and search for the next goal.
            if consecutive == goal:
                # solutionString = charReplace(solutionString, j, ".")
                if changeIndex >= 0:
                    changes.append([changeIndex, goalIndex])
                    changeIndex = -1
                consecutive = 0
                if goalIndex < len(spring[1])-1:
                    goalIndex += 1
                    goal = int(spring[1][goalIndex])
                else:
                    break
                continue
            if char == "#":
                consecutive += 1
                continue

            # Calculates how long the streak of broken springs can and has to be if we change ? to a broken spring.
            if char == "?":
                open = 0
                guaranteed = 0  
                for x in spring[0][j+1:]:
                    if x == ".": 
                        break
                    open += 1
                for y in spring[0][j+1:]:
                    if y != "#":
                        break
                    guaranteed += 1 
                # Calculates the largest possible streak that can be made and checks if it's big enough to satisfy the next goal.
                if consecutive + 1 + open >= goal:
                    # Checks if the smallest possible streak is too big for our goal.
                    if consecutive + guaranteed + 1 <= goal:
                        # If both tests are passed we replace the ? with a broken spring and add to the consecutive counter.
                        solutionString = charReplace(solutionString, j, "#")
                        consecutive += 1

                        # Saves where this streak of changes started so we can check for more possible permutations.
                        if changeIndex < 0:
                            changeIndex = j
                        continue

            # If the code reaches this point the spring has to be working so he consecutive counter resets.

            consecutive = 0
            # solutionString = charReplace(solutionString, j, ".")  
        print(solutionString)
        if changes:
            print("J", i)
            indexes.append(changes)
for ind in indexes:
    print(ind)

        
