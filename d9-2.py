lines = open('d9.txt').readlines()
lines = [[int(n) for n in l.strip().split(' ')] for l in lines]

ans = 0

def diff(line):
    res = []
    n = len(line)
    for i in range(n-1):
        res.append(line[i+1] - line[i])
    return res
        
def find_prev(line):
    if all(v == 0 for v in line):
        return 0
    else:
        n_line = diff(line)
        n = find_prev(n_line)
        return n_line[0] - n

for line in lines:
    ans += line[0] - find_prev(line)

print('answer ', ans)