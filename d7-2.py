lines = open('d7.txt').readlines()
lines = [l.split() for l in lines]
cards = "J23456789TQKA"

def get_hand_val(hand):
    m = []
    for card in cards:
        harley = hand[0].replace('J', card)

        # can just use Counter but I dont want to.
        c = {}
        for h in harley:
            c[h] = c[h] + 1 if h in c else 1
        
        v = sorted(c.values(), reverse=True)
        m = max(v, m)
    
    return m

ans = 0

def hand_comparator(hand):
    return [cards.index(c) for c in hand[0]]

hands = sorted(lines, key=hand_comparator)
hands = sorted(hands, key=lambda x: get_hand_val(x))

for rank, (_, bid) in enumerate(hands, start=1):
    ans += rank * int(bid)

print("answer ", ans)