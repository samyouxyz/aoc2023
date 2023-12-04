from collections import defaultdict


ans = 0

def is_star(c):
	return c == "*"

lines = open('d3.txt').read().splitlines()
data = [list(line) for line in lines]

rows = len(data)
cols = len(data[0])

start = 0
end = 0

cache = defaultdict(list) 

r = 0
while r < rows:
	c = 0
	while c < cols:
		p = 0
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
				
				if is_star(cur):
					cache[(start_row, running_col)] += [num]
					break
				running_col += 1
			
			if (start[1]-1 >=0 and is_star(data[r][start[1]-1])):
				cache[(r, start[1]-1)] += [num]

			if (end[1]+1 < cols and is_star(data[r][end[1]+1])):
				cache[(r, end[1]+1)] += [num]
			
			start_row = start[0] + 1
			running_col = start[1] - 1
			while start_row < rows and end[1]+1 < cols and running_col <= end[1]+1:
				cur = data[start_row][running_col]
				if is_star(cur):
					cache[(start_row, running_col)] += [num]
					break
				running_col += 1

		c = p if p > c else c + 1
		p = 0
	r += 1


for k, v in cache.items():
	if len(v) == 2:
		ans += v[0] * v[1]
		

print('answer: ', ans)