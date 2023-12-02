import re

input_file = open("01_input.txt", "r")
input = input_file.readlines()
res = 0

for line in input:
    digits = re.findall(r"\d", line)
    res_line = int(digits[0]+digits[-1])
    res += res_line

print(res)
