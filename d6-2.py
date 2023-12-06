lines = open('d6.txt').readlines()
lines = [l.split(":")[1] for l in lines]
lines = [l.strip() for l in lines]

# day 2: line change
time_val, distance_val = ["".join(l.split(" ")) for l in lines]

time_val = [int(t) for t in time_val if t]
distance_val = [int(d) for d in distance_val if d]

data = list(zip(time_val, distance_val))

ans = 1

for (time, distance) in data:
    win_count = 0
    for i in range(time):
        total_distance = i * (time - i)
        if (total_distance > distance): 
            win_count += 1
    ans *= win_count

print('answer ', ans)