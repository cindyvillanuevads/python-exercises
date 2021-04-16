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

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
#     Use your is_vowel function to accomplish this.

def is_consonant(letter):
    if type(letter) == str:
        only_letters =  letter.isalpha()
        return only_letters and not is_vowel(letter)
    else:
        return False



# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word 
#    if the word starts with a consonant.

def cap_cons_word(word):
    if type(word) != str:
        return False
    let = word[0]
    if is_consonant(let):
        word = word.capitalize()
    return word


# 5. Define a function named calculate_tip. 
#    It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip (tip, bill_total):
    if  0 < tip < 1:
        total_tip = bill_total * tip
        return total_tip
    else:
        return " The tip must be  betwwen 0 and 1"


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
#    and return the price after the discount is applied.

def apply_discount(price, disc):
    total = price - (price * disc)
    return total



# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input,
#  and return a number as output.

def handle_commas(string):
    string = string.replace(",", "")
    return string


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
 

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

 
def remove_vowels(string):
    new_word=" "
    for letter in string:
        if is_vowel(letter):
            new_word = new_word +letter
    return(new_word)


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#  anything that is not a valid python identifier should be removed
#  leading and trailing whitespace should be removed
#  everything should be lowercase
#  spaces should be replaced with underscores
#  for example:
#  Name will become name
#  First Name will become first_name
#  % Completed will become completed


def normalize_name(string):
    """
    Accept a string and return a valid python identifier
    """
    # remove any leading or trailing spaces replace space with _, and lowercase the string
    string = string.strip().replace(" ", "_").lower()
    #remove all the symbols
    new_string = ""
    for letter in string:
        if letter.isalnum() or letter == "_":
            new_string = new_string + letter
    # remove all the numbers in the beggining of the string
    for letter in range (len(new_string)):
        if not new_string[0].isalpha():
            new_string = new_string[1:]
    if new_string == "":
        return print(" You entered an invalid python identifier")
    else:
        return new_string



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


# def normalize_name(string):
#     output = ""
    
#     # lowercase all the things
#     string = string.lower()

#     # Filter out any non-valid identifiers, keep spaces to turn into _
#     for character in string:
#         if character.isidentifier() or character == " ":
#             output += character
    
#     # remove any leading or trailing spaces
#     output = output.strip()
    
#     # replace " " with "_"
#     output = output.replace(" ", "_")
    
#     return output

# assert normalize_name("First Name") == "first_name"
# assert normalize_name("%99 Compl9eted2") == "completed"
# assert normalize_name(" sum of squares ") == "sum_of_squares"