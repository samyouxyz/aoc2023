lines = open('d7.txt').readlines()
lines = [l.split() for l in lines]

cards = "23456789TJQKA"

store = []

def get_hand_val(hand):
    # can just use `Counter` but I dont want to.
    c = {}
    for h in hand[0]:
        c[h] = c[h] + 1 if h in c else 1

    v = sorted(c.values(), reverse=True)
    # output sth like: [[3, 1, 1], [2, 1, 1, 1], ...]

    return v

ans = 0

def hand_comparator(hand):
    return [cards.index(c) for c in hand[0]]

hands = sorted(lines, key=hand_comparator)

hands = sorted(hands, key=lambda x: get_hand_val(x))

for rank, (_, bid) in enumerate(hands, start=1):
    ans += rank * int(bid)

print("answer ", ans)