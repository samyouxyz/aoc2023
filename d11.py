lines = open('d11.txt').read().splitlines()
data = [list(l) for l in lines]

rows, cols = len(data), len(data[0])

# expand the universe
r = rows - 1
while r >= 0:
    if all(d == '.' for d in data[r]):
        data.insert(r, ['.'] * cols)
    r -= 1

rows, cols = len(data), len(data[0])
c = cols - 1
while c >= 0:
    skip = False
    r = 0
    while r < rows:
        if data[r][c] != ".":
            skip = True
            break
        r += 1
    if not skip:
        for row in range(rows):
            data[row].insert(c, '.')
    c -= 1

rows, cols = len(data), len(data[0])
stars_loc = []
for r in range(rows):
    for c in range(cols):
        if data[r][c] == "#":
            stars_loc.append((r, c))

stars_count = len(stars_loc)
# num_pairs = ((stars_count - 1) * (stars_count - 2)) // 2

ans = 0
for i in range(stars_count-1):
    for j in range(i+1, stars_count):
        x1, y1 = stars_loc[i]
        x2, y2 = stars_loc[j]
        ans += abs(x2 - x1) + abs(y2 - y1)

print('answer ', ans)

