target = {
	"red": 12,
	"green": 13,
	"blue": 14
}

lines = open('d2.txt')
lines = list(map(lambda l: l.split(";"), lines))
lines = list(map(lambda ll: [l.strip() for l in ll], lines))

ans = 0
for l in lines:
	game_num = 0
	for ll in l:
		t = ll.split(':')
		t = [e.strip() for e in t]
		if len(t) > 1:
			game_num = int(t[0].split()[1])
			t = t[1:]
		r = t[0].split(',')
		r = [e.strip() for e in r]
		valid = True
		for e in r:
			es = e.split(' ')
			if int(es[0]) > target[es[1]]:
				valid = False
				break
		if valid == False:
			break
			
	ans += game_num if valid else 0

print('answer ', ans)