with open("day7/day7input.txt", "r") as file:
    values = {"T": 10, "J": 11, "Q": 12, "K": 13}

    lines = file.readlines()
    hands = []
    hmap = {}
    for line in lines:
        hands.append(line.strip().split(" "))
    for hand in hands:
        cards = "".join(reversed(sorted(hand[0])))
        for card in cards:
            if card not in hmap:
                hmap[card] = 1
            else:
                hmap[card] += 1
        print(max(hmap))
        hmap = {}
# print(hands)