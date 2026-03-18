# what is loop?
# A loop is used to repeat a block of code multiple times until a condition is  not .

#range() function is commonly used to generate a sequences of numbers.

#range comes with 3 parameters.
#1. start (inclusive)
#2. stop (exclusive)
#3. step (optional,default is 1)

#Types of loops in python 

# 1.for loop : #Used when we know how many times we want to repeat
#syntax:
#for variable in sequence:
     #code

for i in range(1,6):
    print(i)

# key points:
# 1.range (start ,stop) generates numbers
# 2.loop runs fixed numbers of times

# 2.while loop: used when we repeat until a comdition becomes False

# syntax:
# while condition:
#     ConnectionAbortedError

# ex:
i=1
while i<=5:
    print(i)
    i+=1
o/p=1,2,3,4,5

#TAsk 1:
# print numbers from 1 to 10 :
 for i in range(1,11):
     print(i)

#Task 2
#print even numbers from 1 to 20
 for i in range(1,21):
     if i % 2 == 0:
         print(i)

#task 3
#print odd number to 1 to 15
#example
#start:1
#end:16
#steps:2

 for i in range(1, 16, 2):
     print(i, end=' ')

 for i in range(21, 1, -2):
     print(i, end=' ')

#output
#1 3 5 7 9 11 13 15
#21 19 17 15 13 11 9 7 5 3

#task 4
#print each chaaracter of the string.
text="Python"

for char in text:
    print(char)
#output 
# p
# y
# t
# h
# o
# n

#task 5
#print all items in the list.

data = ["data","science","ai"]
for item in data:
    print(item)
#output 
# data
# science
# ai

#task 6
#find the sum of numbers from 1 to 10
total = 0
for i in range(1,11):
    total += i
    print(total)

#output
#55

#task 7
#print multiplication table of 5
for i in range(1,11):
    print("5 x",i,"=",5*i)
# #output
# #5 x 1 = 5
# 5 x 2 = 10
# .........
# 5 x 10 = 50

#task 8
# count how many vowels are in a string.
text = "hello world"
vowels = "aeiouAEIOU"
count = 0
for char in text: 
    if char in vowels:
        count +=1
    print(f"number of vowels",count)
#output
# number of vowels 0
# number of vowels 1
# number of vowels 1
# number of vowels 1
# number of vowels 2
# number of vowels 2
# number of vowels 2
# number of vowels 3
# number of vowels 3
# number of vowels 3
# number of vowels 3

#task 9 
#print number in revers order from 10 to 1
 for i in range(10,0,-1):
     print(i)
# #output
# # 10 9 8 7 6 5 4 3 2 1 

#task 10
#print square of number from 1 to 5
for i in range(1,6):
    print(i ** 2)
#output
#1 4 9 16 25