lines = open('d11.txt').read().splitlines()
data = [list(l) for l in lines]

rows, cols = len(data), len(data[0])

# expand the universe
expanded_rows = []
expanded_cols = []
r = rows - 1
while r >= 0:
    if all(d == '.' for d in data[r]):
        expanded_rows.append(r)
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
        expanded_cols.append(c)
    c -= 1


rows, cols = len(data), len(data[0])
stars_loc = []
for r in range(rows):
    for c in range(cols):
        if data[r][c] == "#":
            stars_loc.append((r, c))

stars_count = len(stars_loc)
# num_pairs = ((stars_count - 1) * (stars_count - 2)) // 2

def in_expanded_count(x1, x2, type='col'):
    if x2 < x1:
        x1, x2 = x2, x1
    c = 0
    for e in expanded_cols if type == 'col' else expanded_rows:
        if x1 < e < x2:
            c += 1
    return c


ans = 0
for i in range(stars_count-1):
    for j in range(i+1, stars_count):
        x1, y1 = stars_loc[i]
        x2, y2 = stars_loc[j]

        nums_expanded_rows = in_expanded_count(x1, x2, 'row')
        x = abs(x2 - x1)
        x = (x - nums_expanded_rows) + (nums_expanded_rows * 1e6)

        nums_expanded_cols = in_expanded_count(y1, y2, 'col')
        y = abs(y2 - y1)
        y = (y - nums_expanded_cols) + (nums_expanded_cols * 1e6)
        length = x + y
        ans += length

print('answer ', int(ans))

