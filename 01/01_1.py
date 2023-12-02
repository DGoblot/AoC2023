import re

input_file = open("01_input.txt", "r")
input = input_file.readlines()
res = 0
letters_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

for line in input:
    index_start = 0
    index_end = 0
    for letters in letters_dict:
        index_start = line.find(letters)
        if index_start != -1:
            line = line[:index_start+1] + letters_dict[letters] + line[index_start+1:]

        index_end = line.rfind(letters)
        if index_end != -1:
            line = line[:index_end+1] + letters_dict[letters] + line[index_end+1:]

    digits = re.findall(r"\d", line)
    res_line = int(digits[0]+digits[-1])
    res += res_line

print(res)
