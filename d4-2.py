lines = open('d4.txt').read().splitlines()

ans = 0

store = []

for line in lines:
	l0 = [l.strip() for l in line.split(":")][1].split(" | ")
	l1 = [l.strip().split(" ") for l in l0]
	correct = 0

	for e in l1[1]:
		if e != '' and e in l1[0]:
			correct += 1
	store.append((1, correct))

for i, (card_count, correct_count) in enumerate(store):
	for p in range(i+1, i+correct_count+1):
		store[p] = (store[p][0] + card_count, store[p][1])
	
	ans += store[i][0]
		
print('answer ', ans)
