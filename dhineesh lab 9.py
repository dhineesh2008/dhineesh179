                                            #Math Module Tasks

       #Task 1

#Find Square root of 144
import math

num = 144
a = math.sqrt(num)

print("Square root:", a)

#find Power of 5³
import math

b= math.pow(5, 3)

print("5³ =", b)

# find Factorial of 6
import math

c = math.factorial(6)

        #Task 2
#Calculate:ceil(5.2)
import math

print("Ceil of 5.2 =", math.ceil(5.2))

#Calculate:floor(5.8)
import math

print("Floor of 5.8 =", math.floor(5.8))

#Calculate:gcd(24, 36)
import math

print("GCD of 24 and 36 =", math.gcd(24, 36))

            #Task 3
Create calculator using the math module.

import math

d = float(input("Enter first number: "))
e = float(input("Enter second number: "))

print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Power ")
choice = int(input("Enter choice: "))

if choice == 1:
    print(d + e)
elif choice == 2:
    print(d - e)
elif choice == 3:
    print(d * e)
elif choice == 4:
    print(d / e)
elif choice == 5:
    print(math.pow(d, e))
else:
    print("Invalid choice")
                                    #2. Datetime Module Tasks
          #Task 1                                    
#Display:Current date
from datetime import datetime

now = datetime.now()

print("Current Date:", now.date())

#Display:Current time
print("Current Time:", now.time())

#Display:Current year
print("Current Year:", now.year)

           #Task 2
#Find your age using date of birth.

from datetime import datetime

f = input("Enter DOB (DD-MM-YYYY): ")
birth = datetime.strptime(f, "%d-%m-%Y")

age = datetime.now().year - birth.year

print("Age:", age)

          #Task 3
          
#Print today's date in Python DD-MM-YYYY format

from datetime import datetime

today = datetime.today()

print(today.strftime("%d-%m-%Y"))

                                                  # 3. Date Module Tasks
           #Task 1

#Create a date object for your birthday.

from datetime import date

birthday = date(2008, 10, 7)

print("My Birthday:", birthday)

              #Task 2

#Find the difference between: Today's date and Your birthday
from datetime import date

bday = date(2005, 8, 15)  

print("Difference:", tday - bday)

               #Task 3
#Display:Day, month and Year separately
 from datetime import date

today = date.today()

print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

                                  #4. Calendar Module Tasks
                                  
                #Task 1
# Print calendar for current month.
import calendar
from datetime import date

today = date.today()

print(calendar.month(today.year, today.month))

               #Task 2
#Print calendar for the year 2026.
import calendar

print(calendar.calendar(2026))

                #task 3
Check whether:2024, 2025 and 2026 are leap years.

import calendar

print("2024:", calendar.isleap(2024))
print("2025:", calendar.isleap(2025))
print("2026:", calendar.isleap(2026))

                 #Task 4
Find the weekday of your birthday.
import calendar

year = 2005
month = 8
day = 15

print(calendar.day_name[calendar.weekday(year, month, day)])

                                    #5. PyWhatKit Tasks
                     #Task 1

#Send a WhatsApp message automatically.
import pywhatkit

phone = "+944017829"   
message = "Hello! This is a test message."

pywhatkit.sendwhatmsg_instantly(phone, message)

                      #Task 2
    #Search "Python Programming" on Google using PyWhatKit.

import pywhatkit

pywhatkit.search("Python Programming")

                      #Task 3
#Play a YouTube video automatically.

import pywhatkit

pywhatkit.playonyt("Python Tutorial")

              #Task 4
Convert text into handwritten style.

import pywhatkit

pywhatkit.text_to_handwriting("Hello, Welcome to Python!")

                                        #6. Random Module Tasks
             #Task 1
#Generate a random number between 1 and 100.
import random

number = random.randint(1, 100)

print("Random number is:", number)

              #Task 2
#Generate a random OTP of 6 digits.
import random

otp = random.randint(100000, 999999)

print("Your 6-digit OTP is:", otp)

                #Task 3
Create a dice simulator.Example: Python 1 to 6
import random

print("Dice Simulator")
print("Rolling the dice...")

dice = random.randint(1, 6)

print("You got:", dice)

               # Task 4
Create a Rock-Paper-Scissors game using rand
import random

choices = ["rock", "paper", "scissors"]

print("Rock-Paper-Scissors Game")
user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or 
     (user_choice == "paper" and computer_choice == "rock") or 
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")

                                       # 7. NumPy Module Tasks
                 #Task 1
Create a NumPy array:Python [10,20,30,40,50]   
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:", arr)

                #Task 2
#Find: Sum, Mean, Maximum, Minimum.
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
