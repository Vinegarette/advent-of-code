import collections

filename = "q4.txt"


def calc_score(winning, nums):
    winning = set(winning.split(" "))
    ans = -1
    for num in nums:
        num = num.strip()
        if num in winning and num:
            ans += 1
    return 2**ans if ans >= 0 else 0


def calc_winners(winning, nums):
    winning = set(winning.split(" "))
    ans = 0
    for num in nums:
        num = num.strip()
        if num in winning and num:
            ans += 1
    return ans


with open(filename, "r") as FILE:
    cards = [card for card in FILE.readlines()]
    ans = len(cards)

    c = collections.Counter([i for i in range(len(cards))])
    print(c)
    for i, line in enumerate(cards):
        #

        start, numbers = line.split("|")
        winning = start.split(":")[1].strip()
        numbers = numbers.strip().split(" ")

        wins = calc_winners(winning, numbers)
        print(wins)
        for j in range(i + 1, i + 1 + wins):
            c[j] += c[i]

        print(c)
    print(sum(c.values()))
