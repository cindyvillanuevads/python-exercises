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

# How many students prefer light coffee? For each type of coffee roast?

# we need to count when "coffee_preference" ="light",
#that means we need to access every diccionary.
x=0
for student in students:
    if student["coffee_preference"] == 'light':
        x+= 1

print('Students that prefer light coffee: ',x, "students" )


# How many types of each pet are there?


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



# How many grades does each student have? Do they all have the same number of grades?
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

# What is each student's grade average?
# how can we acces to the fist student grades:
print(students[0]["grades"])

# "grades" is  a list. calculate avg = sum of grades / how many grades.
# sum (student["grades"]) / len(student["grades"])

for student in students:
    average =  sum (student["grades"]) / len(student["grades"])
    print(student["student"],' grade average:  ', average)


# How many pets does each student have?

# how can we acces to the fist student "pets": student["pets"]
for student in students:
    no_pets =  len(student["pets"])
    if no_pets == 0:
        print(student["student"], ' has no pets')
    elif no_pets == 1:
        print(student["student"], ' has only 1 pet')
    else:
        print(student["student"], ' has', no_pets,' pets')





# How many students are in web development? data science?
# What is the average number of pets for students in web development?
# What is the average pet age for students in data science?
# What is most frequent coffee preference for data science students?
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?
# What is the average name length?
# What is the highest pet age for light coffee drinkers?