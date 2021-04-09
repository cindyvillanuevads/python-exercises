
# Conditional Basics

# a.prompt the user for a day of the week, print out whether the day is Monday or not


if (input('What day is today?')).lower()== 'monday':
    print('yes! it is Monday')
else:
    print('It is NOT Monday')



#b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

if (input('Tell me a day of the week:  ')).lower() in ['saturday', 'sunday']:
    print('It is weekend!')
else:
    print('It is a weekday')

""""
c. create variables and make up values for

the number of hours worked in one week
the hourly rate
how much the week's paycheck will be
write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
"""
worked_hrs = 41
hr_rate= 20

if worked_hrs > 40:
    paycheck = worked_hrs * hr_rate * 1.5
else:
    paycheck =  hr_rate * ( ((worked_hrs -40) *1.5) +40 )
print(' Your weekly paycheck is for $',paycheck)

#2.Loop Basics

#a. While

"""
Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.
"""

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

n = 0
while n <=100:
    print(n)
    n+=2


#Alter your loop to count backwards by 5's from 100 to -10.
n = 100
while n >= -10:
    print(n)
    n-=5


#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
# Output should equal:

n = 2
while n < 1000000:
    print(n)
    n= n**2

"""
Write a loop that uses print to create the output shown below.


100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
"""
n = 100
while n >0:
    print(n)
    n-=5


#For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.


number = int(input('Tell me a integer number '))

for n in range (1,11):
   
    print(n,' X ',number,' = ', n * number)
    

#For example, if the user enters 7, your program should output:

# Create a for loop that uses print to create the output shown below.

for n in range (1,10):
    number = str(n)
    print (number*n)

"""
break and continue

Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user 
if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
except for the number the user entered.
"""

while True:
    number = input('Tell me an odd number between 1 and 50:  ')
    if number.isdigit () and  int(number) <50 and int(number)%2 != 0:
        break
    
number = int(number)
for n in range (1,51,2):
    if n == number:
        print('Yikes! Skipping number: ', number)
    else:
        print('Here is an odd number:',n )

"""
d.The input function can be used to prompt for input and use that input in your python code.
 Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
 (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, 
 so you'll need to convert this to a numeric type.)
"""
while True:
    number = input('Tell me a positive number:  ')
    if number.isdigit () and  int(number) > 0:
        break

number = int(number)
for n in range (0,number+1):
    print (n)

"""
Write a program that prompts the user for a positive integer.
 Next write a loop that prints out the numbers from the number the user entered down to 1.
"""


while True:
    number = input('Tell me a positive number:  ')
    if number.isdigit () and  int(number) > 0:
        break

number = int(number)
for n in range (number,0,-1):
    print (n)

"""
3.Fizzbuzz

One of the most common interview questions for entry-level programmers is the FizzBuzz test.
 Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""


for n in range(1,101):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

"""
Display a table of powers.

Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
"""
while True:
    number = input('Enter a number:  ')
    if number.isdigit ():
        break

if (input('Do you want to continue:Y/N ?')).lower() in ['yes','y']:
    number = int(number)
    print('number  |  squared   |   cubed',) 
    for n  in range (1,number +1):
        print(n,'      |    ', n**2,'     |   ', n**3)
        # other way print(f'{n: 6} | {n**2: 7} | {n**3: 5}')
else:
    print('Thank you')

#  with  print(f'{n: 6} | {n**2: 7} | {n**3: 5}')
if (input('Do you want to continue:Y/N ?')).lower() in ['yes','y']:
    number = int(number)
    print('number | squared |   cubed',) 
    print('________________________________')
    for n  in range (1,number +1):
        print(f'{n: 6} | {n**2: 7} | {n**3: 5}')
else:
    print('Thank you')


"""
Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
"""

while True:
    number = input('Enter a number:  ')
    if number.isdigit () and 0 <= int(number) < 101:
        break

if (input('Do you want to continue:Y/N ?')).lower() in ['yes','y']:
    number = int(number)
    print('GRADE RANGE:')
    if number >= 88 and number <= 100: # if grade in range(88,101):
        print('A') 
    elif number >= 80 and number <= 87:
        print('B')
    elif number >= 60 and number <= 79:
        print('C') 
    elif number >= 0 and number <= 66:
        print('D')
    else:
        print('F') 
else:
    print('Thank you')

#Bonus

#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

while True:
    number = input('Enter a number:  ')
    if number.isdigit () and 0 <= int(number) < 101:
        break

if (input('Do you want to continue:Y/N ?')).lower() in ['yes','y']:
    number = int(number)
    print('GRADE RANGE:')
    if number >= 88 and number <= 100: # if number in range(88,101):
        if number >=99:
            print('A+')
        else:
            print('A') 
    elif number >= 80 and number <= 87:
        if number >=86:
            print('B+')
        else:
            print('B') 
    elif number >= 60 and number <= 79:
        if number >=78:
            print('C+')
        else:
            print('C') 
    elif number >= 0 and number <= 66:
        if number >=65:
            print('D+')
        else:
            print('D') 
    else:
        print('F') 
else:
    print('Thank you')

# BONUS
"""
Create a list of dictionaries where each dictionary represents a book that you have read. 
Each dictionary in the list should have the keys title, author, and genre. 
Loop through the list and print out information about each book.

Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
"""

books = [
    {'Title': "The Miracle Morning",
    'Author': ' Hal Elrod',
    'Genre': 'Self-help book'
    },
    {'Title': "The Power of Now ",
    'Author': ' Eckhart Tolle',
    'Genre': 'Self-help book'
    },
    {'Title': "The Shack",
    'Author': '  William P. Young',
    'Genre': ' Novel, Thriller, Suspense, Religious Fiction'
    }
]
books[0]['Title']
# this wa is using list comprehension
for book in books:
    [print(key,': ', book[key]) for key in book]
    print('--------')

#this is other way

for book in books:
    for key in book:
        print(key,' : ', book[key])
    print('--------')

option = input('Please choose a genre to give you the titles of the books that we have')