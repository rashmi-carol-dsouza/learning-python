This documents records all my learnings and references of python during the 100DaysOfCode challenge

## Functions:

## all functions @ https://docs.python.org/3/library/functions.html

# print() 
The print function outputs the content inputted into the paranthesis. The output is always a string value
D'ont forget to add double quotes around the input

# input() 
To ask the user for an input
ex. print('Your number is ' + input('What is your number?'
))

# len() 
Returns interger value of input i.e. output the no of characters of the input
Only works with strings
can be used to calculate no of inputs in a list

# sum()
returns sum 
can be used to calculate sum of a list

# min()

# max()

# type()
To check the type of data in the parantheses

# round()
To round of numbers
If you want to round of the specific decimal places – use ‘,(No of digits for preferred rounding) – ex. (10/3,3)

# to round up
import math
a_r = math.ceil(a)

# count()
sentence = 'Mary had a little lamb'
sentence.count('a')

# lower()
s = "Kilometer"
print(s.lower())

## Types of Data

# String
Text = String concatenation. Strings beings and ends with ' ' or " "

# Integers (int)
Whole numbers

#Floating Point Number(float)
Decimals

#Boolean
Only two values i.e. True and False

#  Comments
Python ignores statements that start with # - useful to write notes/reminders to yourself
Use 'control + /' (Windows) - to comment out lines 
To go back to original 'control + /' or 'control + z'

# Variables 
Values can be stored in variables
Assignment Statement ex. Rashmi = me
Variables can also be used in expressions ex me + 1
Ex - age = (input('What is your age?'))
print (age)

## Shortcuts:

\n - to skip input to the next line
Typecasting – convert types of data using str, int, etc and add data inside the paranthesis

Subscripting = If you want to print the first letter of a string - ex . print(“Rashmi”[0])

## Mathematical operators

# +
To add

# -
Subtraction

# *
Multiplication

# /
Division 
Division always outputs as floating number
If you want an integer use // instead of /

# **
Exponent / To raise a number to a certain power

# %
Modulo is used to get the remainder after divison of two numbers

# Order of priority
Parentheses
Exponents
Multiplication - Division
Addition – Subtraction
(Order is from the left to the right)

To use mathematical operations on variables use = ex. /=, += , marks += 1

# Comparison opertor

  > greater than
  >= greater than or equal to
  < less than  
  <= less that or equal to
  == equal to
  != not equal to

## Control Flow:

# if else
example:
if age > 25:
   print('You can enter')
else:
   print('Ypu cannot enter')

# Nested if/else
example:
if contition:
   if another contition:
     do this
       else:
     do this
else:
   do this

# elif
If there are more than two conditions, you can use elif statement:
example:
if condition:
   print(message)
elif:
   print(Other message)
else:
print(Last message)

You can add as many elif's as you may need.

# For loop
example
furniture = ['Sofa','Bed','Chair']
for stuff in furniture:
  print(stuff)

for sum
total_height = 0
for height in student_heights:
  total_height += height 

for no of inputs
total_users = 0
for height in student_heights:
  total_users += 1

resouce - https://developers.google.com/edu/python/lists#for-and-in

# while loop

while something_is_true:
   #do this
   #then do this
   #then do this

loop will continue as long as underlying condition is true.
   

## Logical Operators

# and
both conditions have to be true for the entire line of code to be true

# or
for only one condition is required to be true

# not
revereses a condition

## Modules

# Random

python documentation - https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

ex. import random
a = random.randint(0,9)
print (a)

random.random()
a num between 0 to 1

random.choice(list)
to pick randomly from a list

random.shuffle(list)
to shuffle list items

## Lists

Always start with [ and close with ] and items are seperated with a comma
ex age = [21,22,23]
print(age[0])

To pull out things 
age[0] or age[-1]

To change list data
age[0] = 20
 
To add items to list
age.append(24)

more functions - https://docs.python.org/3/tutorial/datastructures.html

A list can contain other lists within it

## Dictionary

example - 

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

bug is the key and the definition is the value 
ensure the "" for string values to avoid errors

Formating for more than one enteries -

programming_dictionary = {
   "Bug": "An error in a program that prevents the program from running as expected.", 
   "Function": "A piece of code that you can easily call over and over again."
   }

To retrive value - 
print(programming_dictionary["Bug"])

expect errors in case of typos

To add new entries:
programming_dictionary["New_Entry"] = "Definition/Value"

To see all entries:
print(programming_dictionary)

To wipe a dictionary:
programming_dictionary = {}

To edit entires:
programming_dictionary["Entry"] = "New entry"

To loop thru
for thing in programming_dictionary:
    print(thing)

To print all values:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

Nesting:
Value of string or number and be replaced by a list or another dictionary


 ## General tips:

To concatonate strings add + between inputs

When faced with errors - take entire error message and drop into google. Check results from stackoverflow.com 

Look out for syntax highlighting to understand problems

Install and use Thony for breakdown of how code is interpreted by python

f-String – Use f and add other values inside curly braces 
ex. Print(f“ Your age is {age}”)

To round of decimal places in float numbers:
ex. float = 7.54651
    format_float = "{:.2f}".format(float)
    print(format_float)

To add int to value
ex instead of age = age + 3 use age +=3

# Split strings
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

## Using other applications for learning

Use replit for quick exercises
Use Thony to see how the interpreter evaluates the code
Use draw.io for drawing flowcharts or you can install extension in vs code https://www.diagrams.net/blog/embed-diagrams-vscode
for artwork - https://ascii.co.uk/art
 