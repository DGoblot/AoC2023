input_file = open("04_input.txt", "r")
input = input_file.readlines()
res = 0

for line in input:
    card = 0
    line = line.split()
    win = line[2:12]
    my = line[13:]
    for nb in win:
        if nb in my:
            card += 1
    if card != 0:
        res += 2**(card-1)
print(res)