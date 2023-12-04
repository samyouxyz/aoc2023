m = {
	'one': "1",
	'two': "2",
	'three': "3",
	'four': "4",
	'five': "5",
	'six': "6",
	'seven': "7",
	'eight': "8",
	'nine': "9"
}

def letters_to_digits(s: str, start_idx: int, rev = False):
	for k, v in m.items():
		if rev:
			if k == s[start_idx-len(k)+1:start_idx+1]:
				return v
		else:
			if k == s[start_idx:start_idx+len(k)]:
				return v
	return False

def get_num(s: str):
	num1 = 0
	num2 = 0
	p0 = 0
	p1 = len(s) - 1

	while p0 < len(s):
		if (s[p0].isdigit()):
			num1 = s[p0]
			break
		ld = letters_to_digits(s, p0)
		if (ld):
			num1 = ld
			break

		p0 += 1
	
	while p1 >= 0:
		if (s[p1].isdigit()):
			num2 = s[p1]
			break
		ld = letters_to_digits(s, p1, True)

		if (ld):
			num2 = ld
			break

		p1 -= 1

	return num1 + num2
	

with open('d1.txt') as f:
	lines = f.readlines()
	s = 0
	for line in lines:
		s += int(get_num(line.strip()))
	print("answer ", s)


	
