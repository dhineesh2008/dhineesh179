'''#addition

a=int(input("enter a:"))
b=int(input("enter b:"))
print(a+b)

#subraction
a=int(input("enter a:"))
b=int(input("emter b:"))
print(a-b)

#multipcation

a=int(input("enter a:"))
b=int(input("enter b:"))
print(a*b)

#division

a=int(input("enter a:"))
b=int(input("enter b:"))
print(a/b)

#modulus

a=int(input("enter a:"))
b=int(input("enter b:"))
print(a%b)


#floor division

a=int(input("enter a:"))
b=int(input("enter b:"))
print(a**b)


#exponentiation

a=int(input("enter a:"))
b=int(input("enter b:"))
print(a//b)

#rectangle

lenth=float(input("enter the length of the rectangle:"))
width=float(input("enter the width of the rectangle:"))

rect_area=lenth*width
rect_perimeter=2*(lenth*width)

print("rectangle area=",rect_area)
print("rectangle perimeter=",rect_perimeter)

#square

side=float(input("\nEnter the side of the square:"))

square_area=side*side
square_perimeter=4*side

print("square area=",square_area)
print("square perimeter",square_perimeter

     
#circle

radius=float(input("\nEnter the radiusof the circle:"))

circle_area=3.13*radius*radius
circle_perimeter=2*3.14*radius

print("circle area=",circle_area)
print("circle circumference=",circle_perimeter)


#3
a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter third number:"))

average=(a+b+c)/3
print("average=",average)


#4)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# i) If two numbers are equal
if a == b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# ii) If one number is greater than the other
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")

# iii) If a number is less than or equal to another
if a <= b:
    print(f"{a} is less than or equal to {b}")
else:
    print(f"{a} is greater than {b}")
#5)
num = float(input("Enter a number: "))
square_root = num ** 0.5
print(f"The square root of {num} is {square_root}")
#6)
p = float(input("Enter Principal amount: "))
r = float(input("Enter Annual Rate of interest (%): "))
t = float(input("Enter Time (years): "))

# Simple Interest calculation
si = (p * r * t) / 100

# Compound Interest calculation
ci = p * ((1 + r / 100) ** t) - p

print(f"Simple Interest: {si}")
print(f"Compound Interest: {ci}")
#7)
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x /= 4   # x = 6.0
x %= 2   # x = 0.0
x **= 3  # x = 0.0

print(f"Final value of x: {x}")
#8)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Swapping without temporary variable
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
#9)
num = float(input("Enter a number: "))
cube_root = num ** (1/3)
print(f"The cube root of {num} is {cube_root}")
#10)
num = 8523
# Using modulo 100 extracts the last two digits
last_two_digits = num % 100
print(f"The last 2 digits of {num} are {last_two_digits}")
#11)
num = 8523
# Using integer division (//) removes the last two digits
remaining_digits = num // 100
print(f"After removing the last 2 digits, we get: {remaining_digits}")'''

