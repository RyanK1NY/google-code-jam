# Google Code Jam 2017 Qualification Round
# https://code.google.com/codejam/contest/3264486/dashboard
# Python 3
'''
- Make pancake into list of chars
- for every sequence of consecutive characters of length k, flip from "-" to "+"
- determine maximum number of flips possible, make that the maximum number of attempts (length of pancakes - k possibly?)

'''

def flip_element(element):
    if element == "+":
        element = "-"
    else:
        element = "+"
    return element


f = open('A-small-practice.in', 'r')
# Number of testcases
t = int(f.readline())

for item in range(1):
    # k is substring length
    pancake, k = f.readline().split(" ")
    k = int(k)
    pancake_list = [i for i in pancake]
    combo_list = []
    print(pancake)
    print(k)
    for index, value in enumerate(pancake_list):
        temp_list = pancake_list[index:index+k]
        if len(temp_list) == k:
            combo_list.append(temp_list)
    print(combo_list)