lines = open('d8.txt').readlines()

seq = lines[0].strip().replace('R', "1").replace('L', "0")


m = {}

for i in range(2, len(lines)):
    line = lines[i].split(" = ")
    lr = line[1].replace("(", "").replace(")", "").strip().split(", ")
    m[line[0]] = (lr[0], lr[1])


lr = 0
c = 0

curs = [k for k in m.keys() if k.endswith('A')]

def lcm(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = lcm(current_lcm, number)

    return current_lcm

def go_z(curr):
    lr = 0
    c = 0

    while not curr.endswith('Z'):
        curr = m[curr][int(seq[lr])]
        lr += 1
        c += 1
        if lr == len(seq):
            lr = 0
    return c

zes = []

for c in curs:
    zes.append(go_z(c))

print('answer ', lcm(zes))
