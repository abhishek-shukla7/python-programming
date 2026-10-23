# Write a program that prints your name, degree, college, and career goal on separate lines.

from concurrent.futures.process import _ExecutorManagerThread


name="Abhishek"
print("Name: ",name)

degree="BCA (BIG DATA ANALYST)"
print(degree)

college="Lovely Professional University"
print(college)

career="Data Analyst"
print(career)

print("\n")
'''
this is how you can right comments

'''


# type identification

a=7
print(type(a))

b=9.6
print(type(b))

c=True
print(type(c))

d=[1,2,3]
print(type(d))

e=None
print(type(e))


print("\n")

# Convert the string '250' to an integer and add 50 to it.

string="250"


print(type(string))

n=int(string)+50

print(n,type(n))

print("\n")

# Q8. Swap variables

# Swap the values of two variables without creating a third variable

f=1
g=5

print("Before swapping:", f,g)

f,g=g,f
print("After Swapping: ", f,g)

# Q9. Dynamic typing

# Assign an integer to a variable, then assign a string to the same variable. Print its type after each assignment.
print("\n")

i=2

print(type(i))

i="hello"

print(type(i))


print("\n")

# Q10. Predict the output

# Predict the output of x = 10; x = x + 5; x = x * 2. Then verify it in Python.


x=10

x=x+5

x=x*2

print(x)

print("\n")

# C. Input and output
# Q11. User greeting

# Take a user's name as input and print 'Hello, name!' using their actual name.

# print("\n")

# j=input("Enter your name: ")

# print("Hello,",j)


# Q12. Age calculator

# Take birth year and current year as input and calculate the approximate age.

import datetime

current_year = datetime.datetime.now().year

print(current_year)

birth_year=int(input("Enter your birth year: "))

print("your age",current_year-birth_year)

