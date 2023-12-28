with open("day7/day7input.txt", "r") as file:
    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    lines = file.readlines()
    hands = []
    hmap = {}
    sortedHands = []
    for line in lines:
        hands.append(line.strip().split(" "))
    for hand in hands:
        cards = "".join(reversed(sorted(hand[0])))
        temp = []
        hmap = {}
        for card in cards:
            if card not in hmap:
                hmap[card] = 1
            else:
                hmap[card] += 1
        for key in hmap:
            if key in values:
                value = values[key]
            else:
                value = int(key)
            temp = [hmap[key], value]
        temp.sort(reverse=True)
        sortedHands.append([[temp], hand[1]])

    
    finalHands = []
    while sortedHands:
        highest = [0,0,0]
        for i in range(len(sortedHands)):
            print(sortedHands[i][0][0][0])
            count, cardvalue, = sortedHands[i][0][0][0], sortedHands[i][0][0][1]
            print(highest)
            if count > highest[0]:
                highest = [count, cardvalue, i]
        toPop = highest[2]

        finalHands.append(sortedHands.pop(toPop))
    for hand in finalHands:
        print(hand)