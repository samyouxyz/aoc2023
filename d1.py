def get_num(s: str):
	p0 = 0
	p1 = len(s) - 1
	while p0 < len(s):
		if (s[p0].isdigit()):
			break
		p0 += 1
	
	while p1 >= 0:
		if (s[p1].isdigit()):
			break
		p1 -= 1
	
	return s[p0] + s[p1]

with open('d1.txt') as f:
	lines = f.readlines()
	s = 0
	for line in lines:
		s += int(get_num(line))
	print("answer ", s)


	
