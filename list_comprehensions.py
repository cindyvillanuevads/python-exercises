# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 
# - rewrite the above example code using list comprehension syntax.
#  Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2
#  - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits =[fruit.title() for fruit in fruits] #using title() capitalize each word (Mandarin Orange')
capitalized_fruits

capitalized_fruits =[fruit.capitalize() for fruit in fruits] # using capitalize() capitalize the first word  (Mandarin orange')
capitalized_fruits


# Exercise 3 
# - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

#  how many vowels are in a sttring
ca = 'Cindy'
len([let for let in ca if let in 'aeiou'])

y = [let for let in ca if let in 'aeiou']
y

ca = 'dgfghsagvghkdva'
x = len([let for let in ca if let in 'aeiou'])
x 

fruits_with_more_than_two_vowels= [fruit for fruit in fruits if len([let for let in fruit if let in 'aeiou'])> 2]
fruits_with_more_than_two_vowels 



# Exercise 4 
# - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if len([let for let in fruit if let in 'aeiou'])== 2]
fruits_with_only_two_vowels

# Exercise 5 
# - make a list that contains each fruit with more than 5 characters
nlist = [fruit for fruit in fruits if len(fruit) > 5 ]
nlist 

# Exercise 6 
# - make a list that contains each fruit with exactly 5 characters
nlist = [fruit for fruit in fruits if len(fruit) == 5 ]
nlist 

# Exercise 7 
# - Make a list that contains fruits that have less than 5 characters
nlist = [fruit for fruit in fruits if len(fruit) < 5 ]
nlist 

# Exercise 8 
# - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
nlist = [len(fruit) for fruit in fruits ]
nlist 

# Exercise 9 
# - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if x for fruit in "a"]
fruits_with_letter_a

# Exercise 10 
# - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 ==0 ]
even_numbers 

# Exercise 11 
# - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0 ]
odd_numbers

# Exercise 12 
# - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0 ]
positive_numbers

# Exercise 13 
# - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0 ]
negative_numbers

# Exercise 14 
#-  use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
nlist = [number for number in numbers if number >9 or number <-9]
nlist 

# Exercise 15 
# - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number*number for number in numbers ]
numbers_squared 

numbers_squared = [number**2 for number in numbers ]
numbers_squared 

# Exercise 16 
# - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]
odd_negative_numbers

# Exercise 17 
# - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [number+5  for number in numbers ]
numbers_plus_5



# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

#ways to solve

#function
def is_prime(num):
    if type(num) != int:
        return False
    if num <= 0:
        return False
    if num == 1:
        return False
    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
primes = [ number for number in numbers if is_prime(number)]
primes
#  list comprehension.

[x for x in numbers if all(x % y != 0 for y in range(2, x)) and  x > 1]