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


    seeds = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds)-1, 2)]

    
    ans = float('inf')
    
    for t in range(7):
        next_seeds = []
        for start, length in seeds:
            new_s = start
            new_l = length
            end = start + length
            
            # start chopping
            for dest, src_start, l in m[t]:
                src_end = src_start + l
                if start >= src_start and end <= src_end:
                    new_s = start - src_start + dest
                    new_l = length
                elif start < src_start and end > src_end:
                    new_s = dest
                    new_l = l
                elif start < src_start and end > src_start and end < src_end:
                    new_s = dest
                    new_l = end - src_start
                elif start >= src_start and start < src_end and end > src_end:
                    new_s = start - src_start + dest
                    new_l = src_end - start
            next_seeds.append([new_s, new_l])
        seeds = next_seeds
    
    ans = sorted(next_seeds)[0][0]

    print('answer ', ans)


'''
EXPLAIN

we have seed range: seed_start -> seed_end

from seed-to-soil map, we can calculate:
- range: src_start -> src_end
- range: dest_start -> dest_end


let assume in case 1, seed_start and seed_end are both between src_start and src_end,

src_start         seed_start    seed_end    src_end
  |-----------------S-----------------E--------|

            |-----------------S-----------------E--------|
         dest_start      (NEW_start)        (NEW_end)    dest_end

when they are mapped to destination, it must intersect. so the new range for 
the next mapping = NEW_start -> NEW_end (use this as input for the next mapping)


CASE 1:
src_start         seed_start    seed_end    src_end
  |-----------------S-----------------E--------|
intersection mapping: seed_start -> seed_end


CASE 2:
seed_start        src_start        src_end     seed_end
  (S)-----------------|-----------------|--------(E)
intersection mapping: src_start -> src_end


CASE 3:
seed_start        src_start        seed_end    src_end
  (S)-----------------|-----------------(E)--------|
intersection mapping: src_start -> seed_end


CASE 4:
src_start      seed_start         src_end    seed_end
  |-----------------(S)-----------------|--------(E)
intersection mapping: seed_start -> src_end

'''