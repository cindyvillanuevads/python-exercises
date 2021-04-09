#Python String, List, Dictionary Warmup Exercises
""""
Write the code that operates on a single string containing the make and model of a vehicle. The first part of the string before the space is the make The last part of the string after the space is the model We can assume that the strings will only have one space. Assume the input string is completely lower-cased.

Example inputs:
"""
truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lambourgini diablo"


"""
Exercise #1
Write the code to take a string and produce a dictionary out of that string such that the output looks like the following: 
Some thoughts:

You'll need a way to get the first part of the string and a way to get the second part of the string
Feel free to make new variables/data types in between the string and the output dictionary
Input truck = "toyota tacoma"

Output

truck = {
    "make": "toyota",
    "model": "tacoma"
}
"""


truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lambourgini diablo"



# separete make and model for each car
truc_list = truck.split()

sedan_list= sedan.split()

sports_car_list = sports_car.split()

# Create a dicctionary
print ("Truck")
truck_dic = dict( make = truc_list[0] , model = truc_list[1])
print(truck_dic)
print ("Sedan")
sedan_dic = dict ( make = sedan_list[0] , model = sedan_list[1])
print (sedan_dic)
print ("Sedan")
sports_car_list_dicc = dict ( make = sports_car_list[0] , model = sports_car_list[1])
print(sports_car_list_dicc)



"""
Exercise #2
Write the code that takes a dictionary containing make/model for a vehicle and capitalizes the first character of the make and the model:

Input

truck = {
    "make": "toyota",
    "model": "tacoma"
}
Output

truck = {
    "make": "Toyota",
    "model": "Tacoma"
}
"""
# how to get a key from a dicctionary
sedan_dic["make"]
print(sedan_dic["make"])

# using capitalize() 
cap = sedan_dic["make"].capitalize()
print(cap)

# Truck
for key in truck_dic:
    truck_dic[key] = truck_dic[key].capitalize()
print("Truck")
print (truck_dic)
len(truck_dic)
"""
Create a list of 3 dictionaries where each dictionary represents a vehicle, 
as above Write the code that operates on that list of dictionaries in order to uppercase the entire make and model values.

Input

truck = {
    "make": "Toyota",
    "model": "Tacoma"
}
Output

truck = {
    "make": "TOYOTA",
    "model": "TACOMA"
}
"""
# createa  a list of dictionaries
list_dicc = [truck_dic,sedan_dic, sports_car_list_dicc]
print(list_dicc)

"""
list_dicc=[
    {'make': 'Toyota', 'model': 'Tacoma'},
    {'make': 'hyundai', 'model': 'sonata'},
    {'make': 'hyundai', 'model': 'sonata'}]
"""
# how to get a key from a list of dicctionaries
list_dicc[0]['make']


# using capitalize() 
new_upper_make = list_dicc[0]['make'].upper()
new_upper_mod =  list_dicc[0]['model'].upper()


# now we can do it for each dicctionary ussing a loop
for  x in range(len(list_dicc)):
    new_upper_make = list_dicc[x]['make'].upper()
    new_upper_mod =  list_dicc[x]['model'].upper()
    list_dicc[x]['make']=  new_upper_make
    list_dicc[x]['model'] = new_upper_mod 

print (list_dicc)
