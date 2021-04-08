
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
    number = input('Tell me an odd number between 1 and 50  ')
    if number.isdigit () and  int(number) <50 and int(number)%2 != 0:
        break
    
number = int(number)
for n in range (1,50,2):
    if n == number

number = input('Tell me an odd number between 1 and 50')

