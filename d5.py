seeds = []
m = [[] for _ in range(7)]

with open('d5.txt') as f:
    cur = -1
    for line in f.readlines():
        line = line.strip()
        if not line: continue

        if line.startswith('seeds:'):
            seeds = [int(s) for s in line.split(": ")[1].split()]
        else:
            if line and not line[0].isdigit():
                cur += 1
            else:
                m[cur].append([int(n) for n in line.split()])

    
    ans = float('inf')
    for s in seeds:
        cur = s
        loc = 0
        for t in range(7):
            for row in m[t]:
                if cur >= row[1] and cur < row[1] + row[2]:
                    cur = cur - row[1] + row[0]
                    break
        ans = min(cur, ans)
    
    print('answer ', ans)


