
def countMatches(left, right):
    hmap = {}
    matches = 0
    for number in left.split(" "):
        if number.isnumeric():
            hmap[number] = 1
    for number in right.split(" "):
        if number in hmap:
            matches += 1
    hmap = {}
    return matches

with open("day4/day4input.txt", "r") as file:
    stack = []
    totalCards = 0
    for i, line in enumerate(file):
        cardMultiplier = 1
        left, right = line.strip().split("|")
        if stack:
            cardMultiplier += stack.pop(0)
        for j in range(0, cardMultiplier):            
            totalCards += 1
        matchCount = countMatches(left, right)

        while cardMultiplier:
            cardMultiplier -= 1
            for k in range(0, matchCount):
                if stack and len(stack) >= k+1:
                    stack[k] += 1        
                else:
                    stack.append(1)
print(totalCards)

