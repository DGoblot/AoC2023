input_file = open("02_input.txt", "r")
input = input_file.readlines()
res = 0

max_r, max_g, max_b = 12, 13, 14

for line in input:
    r, g, b = 0, 0, 0
    line = line.replace(':', '')
    line = line.replace(',', '')
    line = line.replace(';', '')
    line = line.split()
    
    for i, word in enumerate(line):
        if word == 'red':
            if r < int(line[i-1]):
                r = int(line[i-1])
        if word == 'green':
            if g < int(line[i-1]):
                g = int(line[i-1])
        if word == 'blue':
            if b < int(line[i-1]):
                b = int(line[i-1])

    if r <= max_r and g <= max_g and b <= max_b:
        res += int(line[1])

print(res)