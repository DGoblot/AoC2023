input_file = open("06_input.txt", "r")
input = input_file.readlines()
res = 0

time = input[0].split()[1:]
time = int(''.join(time))
dist = input[1].split()[1:]
dist = int(''.join(dist))

for j in range(time):
    if (time - j)*j > dist:
        res += 1

print(res)