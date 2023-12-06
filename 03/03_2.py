input_file = open("03_input.txt", "r")
input = input_file.readlines()
res = 0
flag = 0
nb = ""

check_x = [0]
check_y = [0]

for x, line in enumerate(input):
    for y,car in enumerate(line):

        if y == len(line) and flag == 1:
            res += int(nb)
            nb = ""
            flag = 0

        if car.isdigit():

            nb += car

            if y > 0:
                check_y.append(-1)
            if y < len(line)-1:
                check_y.append(1)
            if x > 0:
                check_x.append(-1)
            if x < len(input)-1:
                check_x.append(1)

            for i in check_x:
                for j in check_y:
                    if input[x+i][y+j] != "." and not input[x+i][y+j].isdigit():
                        flag = 1

            check_x = [0]
            check_y = [0]

        else:
            if flag == 1:
                    res += int(nb)
            nb = ""
            flag = 0
                

print(res)