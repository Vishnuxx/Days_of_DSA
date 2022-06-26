#Q) Given an array nums of integers, return how many of them contain an even number of digits.
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

array = [12 , 134 , 132434 , 122 , 2323 , 23,1, 2244]

for i in array:
    if len(str(i)) % 2 == 0:
        print(i)
