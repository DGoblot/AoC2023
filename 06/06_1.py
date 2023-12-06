input_file = open("06_input.txt", "r")
input = input_file.readlines()
res = 1

time = input[0].split()[1:]
dist = input[1].split()[1:]

for i in range(len(time)):
    tmp = 0
    for j in range(int(time[i])):
        d = (int(time[i]) - j)*j
        if d > int(dist[i]):
            tmp += 1
    res *= tmp

print(res)