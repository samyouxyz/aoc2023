# this solution works, but stupid, cos I am a dumdum.

lines = open('d7.txt').readlines()
lines = [l.split() for l in lines]
a_cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
a_cards.reverse()
cards = {c: i+1 for i, c in enumerate(a_cards)}

def comparator(card0, card1):
    if card0[0] > card1[0]: return 1
    elif card0[0] < card1[0]: return -1
    elif card0[0] == card1[0]:
        hand0 = card0[1]
        hand1 = card1[1]
        for i in range(len(hand0)):
            if cards[hand0[i]] > cards[hand1[i]]: return 1
            elif cards[hand0[i]] < cards[hand1[i]] : return -1
            else: continue
        return 0


def get_type(hand):
    h = {}
    for c in hand:
        h[c] = h[c] + 1 if c in h else 1

    a = [(v, k) for k, v in h.items()]
    a.sort(reverse=True)

    if a[0][0] == 5:
        return 6 # five of a kind
    elif a[0][0] == 4 and a[1][0] == 1:
        return 5 # four of a kind
    elif a[0][0] == 3 and a[1][0] == 2:
        return 4 # full house
    elif a[0][0] == 3 and a[1][0] == 1 and a[2][0] == 1:
        return 3
    elif a[0][0] == 2 and a[1][0] == 2 and a[2][0] == 1:
        return 2
    elif a[0][0] == 2 and a[1][0] == 1 and a[2][0] == 1 and a[3][0] == 1:
        return 1 # one pair
    else:
        return 0

store = []

ans = 0

for hand, bid in lines:
    store.append((get_type(hand), hand, bid))

from functools import cmp_to_key

store = sorted(store, key=cmp_to_key(comparator))

for rank, (_, _, bid) in enumerate(store):
    ans += (rank+1) * int(bid)

print("answer ", ans)