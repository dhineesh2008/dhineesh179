'''# dictionaries

#1
students = {
    "dhineesh" : 92,
    "raghav" : 99,
    "nagul":85,
    "vipul":87,
    "jai":96,
}

print(students)

#2
students = {
    "dhineesh":88,
    "raghav":97,
    "vishal":94,
    "jai":78,
    "'vipul":98,
}

print(students["vipul"] )

#3

students = {
    "dhineesh": 91,
    "jai": 85,
    "vipul": 94,
    "raghav": 78,
    "jayasurya": 89
}

students["Kavin"] = 87

print(students)

#4
students = {
    "dhneesh": 91,
    "raghav": 85,
    "vipul": 94,
    "raghav": 78,
    "jayasurya": 89
}

top_student = max(students, key=students.get)

print("Student with the highest marks:", top_student)
print("Marks:", students[top_student])

#5

students1 = {
   "dhineesh": 91,
    "kavin": 85,
    "vipul": 94,
}

students2 = {
    "surya": 78,
    "raghav": 89
}

students1.update(students2)

print(students1)

#6
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequencies:")
for char, count in frequency.items():
    print(char, ":", count)

#Functions:
#1

def find_length(text):
    return len(text)

string = input("Enter a string: ")
print("Length of the string is:", find_length(string))

#2

def find_max(numbers):
    return max(numbers)

numbers = [10, 25, 8, 45, 32]

print("Maximum value is:", find_max(numbers))

#3

def find_min(numbers):
    return min(numbers)

numbers = [10, 25, 8, 45, 32]

print("Minimum value is:", find_min(numbers))

#4

def find_sum(numbers):
    return sum(numbers)

numbers = [10, 20, 30, 40, 50]

print("Sum of the numbers is:", find_sum(numbers))

#5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))

print("Factorial of", num, "is:", factorial(num))


#6

def student_details(name, roll, dept):
    print("Student Name :", name)
    print("Roll Number  :", roll)
    print("Department   :", dept)

student_details("Kavin", 101, "Computer Science")

#7

def calculate_total(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    print("Total Marks:", total)

calculate_total(85, 90, 88)

#8

def rectangle_area(length, width):
    area = length * width
    print("Area of the rectangle:", area)

rectangle_area(10, 5)

#9

def greet_user(name, message="Good Morning"):
    print(message + ", " + name + "!")
greet_user("Keerthi")
greet_user("Keerthi", "Welcome")

#10

def add_numbers(*args):
    return sum(args)

total = add_numbers(10, 20, 30, 40, 50)
print("Sum:", total)

#11

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

product = multiply_all(2, 3, 4, 5)
print("Product:", product)'''
