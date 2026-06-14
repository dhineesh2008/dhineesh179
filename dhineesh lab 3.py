'''#print number from 1 to 10 using for loop

for i in range (1,19):
    print (i)

#print the multiplication table

a = int(input("enter a:"))
for i in range (1,10):
    print (i,'x',a,'=',i*a)

#print all even number from 1 to 27

for i in range (1,27):
    if i%2 == 0:
        print (i)

#print the factorial of a number

n = int(input("enter n:"))
f=1
for i in range(1,n+1):
    f*1
print ("factorial:,f")

#print the alphabet form A to

for letter in range (ord('A'), ord('H')):
    print(chr(letter))

#print a pattern

for i in range (1,10):
    for i in range (i):
        print('*',end =" ")
        print()

#print odd number from 1 to 20

for i in range (0,21):
    if i % 2 !=0:
        print(i)



#hollow square pattern

n = 10
for i in range(n):
    for j in range(n):
        if i  == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#print  the inverted triangle

for i in range (6,-1):
    for j in range(i):
        print ('+',end=" ")
    print()


#floyd's triangle pattern

n = 9
num = 1
for i in range (1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()'''


















    
