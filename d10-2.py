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

visited = set()
S = []
for direction in east, west, north, south:
    steps = 0
    x, y = start
    dir = direction
    while not steps or (x, y) != start:
        visited.add((x,y))
        dx, dy = dir
        x += dx
        y += dy
        td = m[lines[x][y]]
        if (-dx, -dy) not in td:
            steps = None
            break
        for nd in td:
            if nd != (-dx, -dy):
                dir = nd
        steps += 1
    if steps:
        S.append(direction)

m['S'] = S
ans = 0
hand = None

for i in range(len(lines)):
    inside = False
    for j in range(len(lines[0])):
        if (i, j) in visited:
            directions = m[lines[i][j]]

            # horizontal pipe
            if west in directions and east in directions:
                continue
            inside = not inside
            
            # vertical pipe
            if north in directions and south in directions:
                continue

            # if it is U-shaped pipes, continue inside
            # if it is chair-shaped pipes, stop inside
            thand = None
            for d in directions:
                if d != west and d != east:
                    thand = d # north or south only
            if hand == None:
                hand = thand
            else:
                if thand != hand:
                    inside = not inside
                hand = None
        else:
            ans += 1 if inside else 0

print('answer ', ans)




# source: https://topaz.github.io/paste/#XQAAAQC3BwAAAAAAAAAyGEruliPhOEAkMm9/68Tg8AdoCTQWxGHSseFlIbYyBnI55rEeSqm3eiYjk9ZuSnTgFzi/2ShOY71s1/bQKgKfCoYnUxpxtI4bfEhqTSQpXHqXVN7SKmGObar/oP5A1SRPv0oMlkpAwUkYUoDM+3WjSg+JUQITITXeUCwOo2NIUEusM5drnwGruQL2jfk5W4egTk/EJ15cG/yQHowq1KHnBEcneoiaKHeUJJweL4D4pHdJjvJzDOjyz+0ePKW1vSv2mZCMxOJN+/HuVR6Uw1pC/Cm2DBNRW7ElB4O0e0SdEBZ4xCawQz0Iw2ktOfuR0CbV/o9nuzwkgb1iIit+ivEiz3Q3urSqJKnWAjrOkOvoCe3H8o6dJqS7D8uyas32RsW+IQBynhtcSXTuxk7KQp+3/+Bu7aFkst2YDHWHv2GAcGLDVTve379+wafWFpDPTcA/PZc4GafNvgCS5yZZkspGeEoh0srM8uZOR651EQMr+Rl3L3QDegKJh1jJ+cIMpDyqnBigvsaSvK0K5Bl9HpmyhKjDOn+9CV5l8/JYOjMe/ssICxHen66FVUSh4J5qpWdf2t4IK6qWdAnoIJn9R8Hh+urAduziXPf36/kRWyWuMsie1B1zlSKFFP5yeg7dELFzdL8iTIye6dwS1TGebnsMJfNw3hGdUVpBvinNqApt8+OUbvMhgnNJWa523H3VhOyFgkSuJl9RIOqxKA5iaxN5+0YM+/SOnnn+a9aRevjGJ2jVh4Glz4GlGh7/ZXQU95UiEbTrj2Rvc6kt9DIjhq/8IuW6+15wX/5QcqTzN/80iGVuRYrhQmvPCIFp1lPNToG5Nognd+lkjFbacL22mA0Huu9T1i0pNABM4bcNx9MQ2LcVDsCBhYe15H53foFv+9N74w==
# my original code is too messy. i like the simplicity of this code, so i just copied it here and learn from this.