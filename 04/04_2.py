input_file = open("04_input.txt", "r")
input = input_file.readlines()
res = 0
copy = [1 for i in range(len(input))]
print

for x, line in enumerate(input):
    match = 0
    line = line.split()
    win = line[2:12]
    my = line[13:]
    for nb in win:
        if nb in my:
            match += 1
    for i in range(copy[x]):
        for j in range(match):
                if x + j + 1 < len(input):
                    copy[x + j + 1] += 1
    res += copy[x]
print(res)