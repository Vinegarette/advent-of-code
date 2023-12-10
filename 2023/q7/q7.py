from collections import Counter
from functools import cmp_to_key


def read_line(line):
    hand, bid = line.split(" ")

    # Determine type of hand
    c = Counter(hand)
    print(c)
    # Determine Type,

    # Max_Count is now max count not equal to J
    # Special case where all 'J'?
    # Find Max Count char
    max_key, max_count = max(
        (item for item in c.items() if item[0] != "J"),
        key=lambda x: x[1],
        default=("J", 5),
    )
    max_count += c["J"]

    # Replace c.values()
    # Extremely scuffed honestly
    new_c = ""
    for c in hand:
        if c == "J":
            new_c += max_key
        else:
            new_c += c

    c = Counter(new_c)

    # First Card, Same Label, Second Card....
    # Rank....

    # Rank 7 = Five of a Kind
    # Rank 6 = Four of a Kind
    # Rank 5 = Full House...
    # Rank 4 = Three of a Kind
    # Rank 3 = 2 Pair
    # Rank 2 = 1 Pair
    # Rank 1 = High Card

    # Figure out for purpose of J...
    # Need to determine ranks here too!

    # TODO:
    # Must Change c.values()!

    rank = -1
    if max_count < 2:
        rank = max_count
    elif max_count == 2:
        # Check if 1 pair or 2 pair
        if sorted(list(c.values())) == [1, 2, 2]:
            # print(f"{hand} supposedly 2, 2, 1")
            rank = 3
        else:
            rank = 2
    elif max_count == 3:
        if sorted(list(c.values())) == [2, 3]:
            rank = 5
        else:
            rank = 4
        # Deal w/ Full House vs Three of a Kind
    else:
        rank = max_count + 2
    return (rank, hand, int(bid))


cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]
strength_order = {cards[i]: i for i in range(len(cards))}


def hand_cmp(hand1, hand2):
    if hand1[0] != hand2[0]:
        return hand1[0] - hand2[0]
    else:
        # Hand ranks are different, compare by strings
        # print(f"Same rank, {hand1[1]}, {hand2[1]}")

        # A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
        for a, b in zip(hand1[1], hand2[1]):
            a_strength, b_strength = strength_order[a], strength_order[b]

            # If same, skip to next
            if a_strength == b_strength:
                continue
            elif a_strength > b_strength:
                # If larger, swap; stronger must be on the right!
                return 1
            else:
                # Don't swap...
                return -1
        return 0


filename = "q7.txt"
with open(filename, "r") as FILE:
    lines = [line.strip() for line in FILE]
    # Determine type of hand
    hand_info = []
    for line in lines:
        hand_info.append(read_line(line))

    hand_info = sorted(hand_info, key=cmp_to_key(hand_cmp))
    ans = 0
    # Weakest to Strongest
    for i in range(len(hand_info)):
        ans += (i + 1) * hand_info[i][2]
        # print(ans)
    print(hand_info)
    print(ans)
    with open(f"{filename}-ans.txt", "w") as other:
        for hand in hand_info:
            other.write(f"{hand[0]}, {hand[1]}, {hand[2]}\n")
        other.write(str(ans))
