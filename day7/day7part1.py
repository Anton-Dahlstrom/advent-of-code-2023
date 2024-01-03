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
            temp.append([hmap[key], value])
        temp.sort(reverse=True)
        sortedHands.append([temp, hand[1]])

    def sorter(first, second, index, position):
        if first[index][position] == second[index][position]:
            return False
        elif first[index][position] > second[index][position]:
            return 1
        else:
            return 2

    finalHands = []
    while sortedHands:
        index = 0
        highest = [[0]]
        for i in range(len(sortedHands)):
            hand = sortedHands[i][0]
            stop = False
            for j in range(len(hand[0])):
                if stop:
                    break
                for k in range(len(hand)):
                    result = sorter(hand, highest, k, j)
                    if result:
                        if result == 1:
                            highest = hand
                            index = i
                        elif result == 2:
                            stop = True
                        break
        finalHands.append(sortedHands.pop(index))
    answer = 0
    for i in range(len(finalHands)):
        print(finalHands[i])
        # print(i)
        answer += (i+1) * int(finalHands[i][1])
        # print(finalHands[i][1])
        # print(answer)
    print(answer)
    # 252997218 too high