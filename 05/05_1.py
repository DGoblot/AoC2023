input_file = open("05_input.txt", "r")
input = input_file.readlines()
res = 0

first_line = input[0].split()[1:]
seed = []
ran = []
for i in range(len(first_line)):
    if i%2:
        ran.append(int(first_line[i]))
    else:
        seed.append(int(first_line[i]))

seed_flag = [0 for i in range(len(seed))]

for x,line in enumerate(input):
    line = line.split()
    if line != []:
        if line[0].isdigit():
            for y,s in enumerate(seed):
                if seed_flag[y] == 0:
                    s = int(s)
                    r = int(ran[y])-1
                    dest = int(line[0])
                    ori = int(line[1])
                    map_r = int(line[2])- 1
                    if s >= ori and s+r <= ori+map_r:
                        seed[y] = dest+s-ori
                        seed_flag[y] = 1
                    elif s < ori and s+r > ori+map_r:
                        seed[y] = dest
                        ran[y] = dest+map_r
                        seed_flag[y] = 1
                        seed.append(ori+map_r+1)
                        ran.append(s+r-ori+map_r+1)
                        seed_flag.append(0)
                        seed.append(s)
                        ran.append(ori-1)
                        seed_flag.append(0)
                    elif s >= ori and s <= ori+map_r and s+r > ori+map_r:
                        seed[y] = dest+s-ori
                        ran[y] = ori+map_r-s
                        seed_flag[y] = 1
                        seed.append(ori+map_r+1)
                        ran.append(s+r-ori+map_r+1)
                        seed_flag.append(0) 
                    elif s < ori and s+r >= ori and s+r <= ori+map_r:
                        seed[y] = dest
                        ran[y] = s+r-ori
                        seed_flag[y] = 1
                        seed.append(s)
                        ran.append(ori-1-s)
                        seed_flag.append(0)

                    if x+1 == len(input):
                        seed_flag = [1 for i in range(len(seed))]
                    elif input[x+1] == '':
                        seed_flag = [1 for i in range(len(seed))]
        print(seed)
        print(ran)
        print(x)
    else:
        seed_flag = [0 for i in range(len(seed))]  

res = min(seed)
print(res)