lines = open('d8.txt').readlines()

seq = lines[0].strip().replace('R', "1").replace('L', "0")


m = {}

for i in range(2, len(lines)):
    line = lines[i].split(" = ")
    lr = line[1][1:-2].split(", ")
    m[line[0]] = (lr[0], lr[1])

cur = "AAA"
lr = 0
c = 0

while cur != 'ZZZ':
    cur = m[cur][int(seq[lr])]
    lr += 1
    c += 1
    if lr == len(seq):
        lr = 0

print('answer ', c)
