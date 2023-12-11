lines = open('d10.txt').readlines()
lines = [list(l.strip()) for l in lines]

# find S
start = ()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S": start = (i, j)

east, west, north, south = (0, 1), (0, -1), (-1, 0), (1, 0)

m = {
    "|": [north, south],
    "-": [east, west],
    "L": [north, east],
    "J": [west, north],
    "7": [west, south],
    "F": [south, east],
    "S": [east, west, north, south],
    ".": []
}

ans = 0
visited = set()

for direction in east, west, north, south:
    steps = 0
    x, y = start
    while not steps or (x, y) != start:
        visited.add((x,y))
        dx, dy = direction
        x += dx
        y += dy
        td = m[lines[x][y]]
        if (-dx, -dy) not in td: # in case .
            break
        for nd in td:
            if nd != (-dx, -dy):
                direction = nd
        steps += 1

    ans = max(steps, ans)

print('answer ', ans // 2)