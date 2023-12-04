lines = open('d2.txt')
lines = list(map(lambda l: l.split(";"), lines))
lines = list(map(lambda ll: [l.strip() for l in ll], lines))

ans = 0
for l in lines:
	max_set = {
		"red": 0,
		"green": 0,
		"blue": 0
	}
	for ll in l:
		t = ll.split(':')
		t = [e.strip() for e in t]
		if len(t) > 1:
			game_num = int(t[0].split()[1])
			t = t[1:]
		r = t[0].split(',')
		r = [e.strip() for e in r]
		for e in r:
			es = e.split(' ')
			max_set[es[1]] = max(max_set[es[1]], int(es[0]))

		prod = 1
		for value in max_set.values():
			prod *= value 
			
	ans += prod

print('answer ', ans)