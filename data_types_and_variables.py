"""
***********************************************************************************************************
Write some Python code, that is, variables and operators, to describe the following scenarios. 
Do not worry about the real operations to get the values, the goal of these exercises is to understand 
how real world conditions can be represented with code.
***********************************************************************************************************
"""

"""
1. You have rented some movies for your kids: 
The little mermaid (for 3 days),
Brother Bear (for 5 days, they love it),
and Hercules (1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, how much will you have to pay? 27 dollars
"""
# variables
movie_cost = 3
# days of rented movie
little_mer = 3
bro_bear = 5
her =  1


#result
total = (little_mer + bro_bear + her) * movie_cost
total


"""
2.Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour.
Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
total $7,420
"""
#  dollars per hour
google = 400
amazon = 380
facebook = 350

# worked hours
goog_hrs = 6
amaz_hrs = 4
faceb_hrs = 10

# (first calculate the total for each company  and the sum all)
payment = (google * goog_hrs) + (amazon * amaz_hrs) + (facebook * faceb_hrs)
payment



"""
3. A student can be enrolled to a class only if the class is not full and 
the class schedule does not conflict with her current schedule.
"""
#variables
is_class_full = False
is_conflict = False

#result
is_enrrolled = not (is_class_full or is_conflict)
is_enrrolled 


"""
4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired.
Premium members do not need to buy a specific amount of products.
"""
#variables
is_premium_member = True
is_current_offer = False
no_items = 2
offer ="20%  off"

# you can get offer if:
#  is_current_offer = true
# no_items  > 2  
# or is_premium_member = True.


get_offer = is_current_offer and (no_items >2 or is_premium_member)
get_offer

"""
5. Use the following code to follow the instructions below:
"""
username = 'codeup'
password = 'notastrongpassword'

"""
Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
"""
#variables
pass_charac = len(password) >= 5
pass_charac
user_charac = len(username) < 20
user_charac
is_pass_user_same = username == password
is_pass_user_same

#validation
is_valid_registation = pass_charac and user_charac and not is_pass_user_same
is_valid_registation

#bonus
pass_space = password[0] == ' ' or  password[-1] == ' '
user_space = username[0] == ' ' or  username[-1] == ' '
pass_space
user_space

#validation 
is_valid_registation = pass_charac and user_charac and not is_pass_user_same and not (pass_space or user_space)
is_valid_registation

