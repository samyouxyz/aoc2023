lines = open('d4.txt').read().splitlines()

ans = 0

for line in lines:
	l0 = [l.strip() for l in line.split(":")][1].split(" | ")
	l1 = [l.strip().split(" ") for l in l0]
	correct = 0
	for e in l1[1]:
		if e != '' and e in l1[0]:
			correct += 1
	
	if correct:
		ans += 2**(correct-1)
		
print('answer ', ans)
