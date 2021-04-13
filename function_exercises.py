# 1. Define a function named is_two. It should accept one input and 
# return True if the passed input is either the number or the string 2,False otherwise.


def is_two(number):
    if number == 2 or number == '2':
        return True
    else:
        return False

# other way 
# def is_two(x):
#     return x == 2 or x == "2"

print ("Exercise 1")
print (is_two(2))
print( is_two(2.0)) 
print( is_two("2")) 
print( is_two(5)) 
print( is_two("coffee"))

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter):
    if letter.lower()  in "aeiou":
        return True
    else:
        return False

# a complete way to do it 
# def is_vowel(string):
#     if type(string) == str:
#         result = string.lower() in ["a", "e", "i", "o", "u"]
#         return result
#     else:
#         return False
print("Exercise 2")
print(is_vowel("A"))
print(is_vowel("p"))
print(is_vowel("1"))

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#     Use your is_vowel function to accomplish this.

def is_consonant(letter):
    if type(letter) == str:
        only_letters =  letter.isalpha()
        return only_letters and not is_vowel(letter)
    else:
        return False
print("Exercise 3")
print(is_consonant("B"))
print(is_consonant("E"))
print(is_consonant("O"))
print(is_consonant("2")) 
print(is_consonant("+"))


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word 
#    if the word starts with a consonant.

def cap_cons_word(word):
    if type(word) != str:
        return False
    let = word[0]
    if is_consonant(let):
        word = word.capitalize()
    return word
print("Exercise 4")    
print(cap_cons_word("coffee"))
print (cap_cons_word("another string"))

# 5. Define a function named calculate_tip. 
#    It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip (tip, bill_total):
    if  0 < tip < 1:
        total_tip = bill_total * tip
        return total_tip
    else:
        return " The tip must be  betwwen 0 and 1"
print("exercise 5")
print (calculate_tip(.20,50))

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
#    and return the price after the discount is applied.

def apply_discount(price, disc):
    total = price - (price * disc)
    return total
print("exercise 6")
print (apply_discount(100, .20))    


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input,
#  and return a number as output.

def remove_commas(string):
    string = string.replace(",", "")
    return string
print("exercise 7")
print(remove_commas("30,456"))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"
print("Exercise 8")
print(get_letter_grade(48))   

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

 
def remove_vowels(string):
    new_word=" "
    for letter in string:
        if is_vowel(letter):
            new_word = new_word +letter
    return(new_word)
print("Exercise 9")
print(remove_vowels("Cindyaes"))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#  anything that is not a valid python identifier should be removed
#  leading and trailing whitespace should be removed
#  everything should be lowercase
#  spaces should be replaced with underscores
#  for example:
#  Name will become name
#  First Name will become first_name
#  % Completed will become completed

# replace  " " for _ and making my string lowercase
def repl_us(string):
    """
    this function replace all spaces with _ . lowercase the string
    """
    string = string.replace(" ", "_")
    string = string.lower()
    print(string)
    return string


def second_valid(string):
    """
    this function calculate  the position of the first letter of the string, so we can 
    have a nre string strating from the first letter 
    """
    x=0
    print(x)
    if string[0].isdigit:
        for letter in range (len(string)): 
            #if string[letter].isdigit: 
            if string[letter] in "0123456789":
                x+= 1
                if x!= len(string) and string[x].isalpha(): # we are checking if after a number is a letter.
                    break
    print(string, "valor x", x)        
    if x == len(string):
        string = " "
    else:
        string = string [x-1:] #x has the position of the first letter
    return string

def third_valid (string):
    """
    removes everything except numbers, leters and underscore"
    """
    new_string =" "
    for letter in string:
        if letter.isalnum() or letter == "_":
            new_string = new_string +letter
    return new_string


def normalize_name(string):
    res = third_valid(second_valid(repl_us(string)))
    if res == " ":
        print("Invalid python identifier")
    else:
        print("the valid python identifier is: ", res)
        return res 

string =  input('Enter a string :  ')
normalize_name(string)


#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#  cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#  cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

my_list = [1,2,3,4]
def cumulative_sum(my_list):
    new_list=[]
    new_list.append(my_list[0])
    for number in range(1,len(my_list)):
        res = new_list[number -1] + my_list[number]
        new_list.append(res)
    return new_list


