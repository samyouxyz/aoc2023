ans = 0

def is_symbol(c):
	return c != '.' and not c.isdigit()

lines = open('d3.txt').read().splitlines()
data = [list(line) for line in lines]

rows = len(data)
cols = len(data[0])

start = 0
end = 0

r = 0
while r < rows:
	c = 0
	while c < cols:
		valid = False
		if data[r][c].isdigit():
			start = (r, c)
			p = c
			while p < cols:
				if not data[r][p].isdigit():
					break
				p += 1
			end = (r, p-1)
			num = int(''.join(data[r][c:p]))

			start_row = start[0] - 1
			running_col = start[1] - 1
			while start_row >= 0 and end[1]+1 < cols and running_col <= end[1]+1:
				cur = data[start_row][running_col]
				
				if is_symbol(cur):
					valid = True
					break
				running_col += 1
			
			if (start[1]-1 >=0 and is_symbol(data[r][start[1]-1])) or (end[1]+1 < cols and is_symbol(data[r][end[1]+1])):
				valid = True
			
			start_row = start[0] + 1
			running_col = start[1] - 1
			while start_row < rows and end[1]+1 < cols and running_col <= end[1]+1:
				cur = data[start_row][running_col]
				if is_symbol(cur):
					valid = True
					break
				running_col += 1

		if valid:
			c = p
			ans += num
		else:
			c += 1
	r += 1

print('answer: ', ans)