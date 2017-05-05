# Google Code Jam 2017 Qualification Round
# https://code.google.com/codejam/contest/3264486/dashboard
# Python 3
'''
- Make pancake into list of chars
- for every sequence of consecutive characters of length k, flip from "-" to "+"
- determine maximum number of flips possible, make that the maximum number of attempts (length of pancakes - k possibly?)

'''


f = open('A-small-practice.in', 'r')
# Number of testcases
t = int(f.readline())


for item in range(t):
    pancake, k = f.readline().split(" ")
    print(pancake)
    print(k)