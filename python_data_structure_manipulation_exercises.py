# The following questions reference the students data structure below. Write the python code to answer the following questions:
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]
# 1.How many students are there?

# we have a list of diccionaries.
# every diccionary represents a student with his/her information.
# we can use len  to get the length of our list
total= len(students)
print('Total of students', total)

#2. How many students prefer light coffee? For each type of coffee roast?

# we need to count when "coffee_preference" ="light",
#that means we need to access every diccionary.
x=0
y=0
z=0
for student in students:
    if student["coffee_preference"] == 'light':
        x+= 1
    if student["coffee_preference"] == 'medium':
        y += 1
    else:
        z += 1


print('Students that prefer light coffee: ',x, "students" )
print('Students that prefer medium coffee: ',y, "students" )
print('Students that prefer dark coffee: ',z, "students" )


# 3.How many types of each pet are there?


# how to acces to asingle  the key that we need. 
(students[0]["pets"][0]['species'])
 
 # pets is  a list of dictionaries
type(students[0]["pets"])
cat=0
dog=0
horse =0
for student in students:
    nlist = student["pets"]
    if len(nlist)> 0:
        for x in range(len(nlist)):
            if nlist[x]['species'] == "cat":
                cat +=1 
            elif nlist[x]['species'] == "dog":
                dog +=1
            else:
                horse +=1
print(' Pet types:')
print('Cat:   ', cat)
print('Dog:   ', dog)
print('Horse: ', horse)



# 4.How many grades does each student have? Do they all have the same number of grades?
# how can we acces to the fist student grades:
print(students[0]["grades"])

# now lets print each grades for each student (this is only yo show how to access)
for student in students:
    print(student['grades'])
   

# grades are a list. so we can use len() to get how many grades a student has
len((student['grades']))

# now lets do it for each student with a loop
for student in students:
    no_grades = len((student['grades']))
    print(student["student"],'  has ', no_grades, ' grades')

# 5.What is each student's grade average?
# how can we acces to the fist student grades:
print(students[0]["grades"])

# "grades" is  a list. calculate avg = sum of grades / how many grades.
# sum (student["grades"]) / len(student["grades"])

for student in students:
    average =  sum (student["grades"]) / len(student["grades"])
    print(student["student"],' grade average:  ', average)


# 6. How many pets does each student have?

# how can we acces to the fist student "pets":
# sutdent= students[0].
# so student["pets"] has the values that we need 
for student in students:
    no_pets =  len(student["pets"])
    if no_pets == 0:
        print(student["student"], ' has no pets')
    elif no_pets == 1:
        print(student["student"], ' has only 1 pet')
    else:
        print(student["student"], ' has', no_pets,' pets')



# 7. How many students are in web development? data science?

#first solve only for first item from the list
# sutdent= students[0].
# so student["course"] has the values that we need 
ds=0
wd=0
other =0
for student in students:
    if student["course"] == 'data science':
        ds+=1
    elif student["course"] == 'web development':
        wd+=1
    else:
        other += 1

print('Students in Data Science: ', ds)
print('Students in Web Development: ',wd)
print('Other: ', other)


# 8. What is the average number of pets for students in web development?
x=0
age_pets = 0
for student in students:
    if student["course"] == 'web development':
        age_pets = age_pets + len(student["pets"])
        x += 1
average = no_pets / x
print("The average number of pets for students in web development is: ", average)

# 9.What is the average pet age for students in data science?

x=0
pets = 0
for student in students:
    if student["course"] == 'data science':
        lon = len(student["pets"])
        if lon > 0:
            for n in range (lon):
                pets = pets + student["pets"][n]["age"]
                x += 1
average = pets / x
print("The average pet age for students in Data Science is: ", average)



# 10.What is most frequent coffee preference for data science students?

# first I calculate how many students prefer each coffe
dark=0
med= 0
light =0
for student in students:
    if student["course"] == 'data science':
        if student["coffee_preference"] == 'light':
            light += 1
        elif student["coffee_preference"] == 'medium':
            med +=1
        else:
            dark +=1
       
##  I create a list of diccionaries  with the information. but this was is long
"""
pref = []  
pref =[
{
    "coffe":"dark",
    "No_students": dark
},
{
    "coffe":"medium",
    "No_students": med
},
{
    "coffe":"light",
    "No_students": light
}
]
f= 0 
freq = {}
  
# with this loop I compare each diccionary and freq has the diccionary with max number
for cof in pref:
    n = int(cof["No_students"])
    if n > f:
        f = n
        freq = cof

print("The most frequent coffee preference for data science students is: ", freq["coffe"])
"""

# better  way
if dark > med > light:
    print("The most frequent coffee preference for data science students is:  Dark")
elif  med > dark > light:
    print("The most frequent coffee preference for data science students is:  Medium")
else:
    print("The most frequent coffee preference for data science students is:  Light")

#print("The average number of pets for students in Data Science is: ", average)

x=0
no_pets = 0
for student in students:
    if student["course"] == 'data science':
        no_pets = no_pets + len(student["pets"])
        x += 1
average = no_pets / x
print("The average number of pets for students in Data Science is: ", average)


# 11. What is the least frequent coffee preference for web development students?

dark=0
med= 0
light =0
for student in students:
    if student["course"] == 'web development':
        if student["coffee_preference"] == 'light':
            light += 1
        elif student["coffee_preference"] == 'medium':
            med +=1
        else:
            dark +=1

if dark < med < light:
    print("The least frequent coffee preference for web development is:  Dark")
elif  med < dark < light:
    print("The least frequent coffee preference for web development is:  Medium")
else:
    print("The least frequent coffee preference for web development is:  Light")


# 12.What is the average grade for students with at least 2 pets?

for student in students:
    no_pets =  len(student["pets"])
    if no_pets >= 2:
        average =  sum (student["grades"]) / len(student["grades"])
        print("Average grade for students with at least 2 pets")
        print(student["student"],' grade average:  ', average)


# 13. How many students have 3 pets?
x=0
for student in students:
    no_pets =  len(student["pets"])
    if no_pets == 3:
        x += 1

print("The total of students that have 3 pets:", x)



# 14. What is the average grade for students with 0 pets?
grades=[]
for student in students:
    no_pets =  len(student["pets"])
    if no_pets == 0:
         grades = grades + student["grades"]       
average = sum(grades) / len(grades)
print("The average grade for students with 0 pets", average)

# 15. What is the average grade for web development students? data science students?

grades_wd =[]
grades_ds=[]
for student in students:
    if student["course"] == 'web development':
        grades_wd = grades_wd + student["grades"]
    else:
        grades_ds = grades_ds +student["grades"]
average_ds = sum(grades_ds) / len(grades_ds)     
average_wd = sum(grades_wd) / len(grades_wd)
print("The average grade for Web Development students is: ", average_wd)
print("The average grade for Data Science students is: ", average_ds)

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# first we know that "grades" is a list, in a list we can use max() for a highest grade and min() for the lowest grade
#we need to create a list that has all the grades for the dark coffee drinkers
grades = []
for student in students:
    if student["coffee_preference"] == "dark":
        grades += student["grades"]
aver_range = max(grades) - min(grades)
print(max(grades))
print(min(grades))
print("The average range for dark coffee drinkers is:", aver_range)

# 17. What is the average number of pets for medium coffee drinkers?
x=0
pets = []

for student in students:
    if student["coffee_preference"] == "medium":
        x = len(student["pets"])
        pets.append(x)
print("************************************")
print("   ")
print("17. The average number of pets for medium coffee drinkers is:", sum(pets) / len(pets))

# 18. What is the most common type of pet for web development students?
"""
Counter(words).most_common(10)

for student in students:
    if student["course"] == "web development":
        Counter(student["pets"])
"""
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?