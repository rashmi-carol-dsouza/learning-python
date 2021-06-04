## Functions:

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

#type()
To check the type of data in the parantheses

#round()
To round of numbers
If you want to round of the specific decimal places – use ‘,(No of digits for preferred rounding) – ex. (10/3,3)


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

# Order of priority
Parentheses
Exponents
Multiplication - Division
Addition – Subtraction
(Order is from the left to the right)

To use mathematical operations on variables use = ex. /=, += , marks += 1

## General tips:

To concatonate strings add + between inputs

When faced with errors - take entire error message and drop into google. Check results from stackoverflow.com 

Look out for syntax highlighting to understand problems

Install and use Thony for breakdown of how code is interpreted by python

f-String – Use f and add other values inside curly braces 
ex. Print(f“ Your age is {age}”)

To round of decimal places in float numbers:
ex. float = 2.154327
    format_float = "{:.2f}".format(float)
    print(format_float)
