'''#increment

i=1
while i<=5:
    print(i)
    i+=1
i=1
while i<5:
    print(i)
    i+=1

#decrement
i=5
while i>=1:
    print(i)
    i-=1

#infinity

while true:
    print("Hii")
#even numbers
i=2
while i<=20:
    print(i)
    i+=2

#odd numbers

i=1
while i<=20:
    print(i)
    i+=2

#multiplication table

n=int(input("enter n:"))
f=1
for i in range (1,n+1):
    f*+i
print ("factorial:",f)


#palindrome

a=121
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
    print(b)
    if a==b:
        print("palindrome")
    else:
        print("not a palindrome")

#spy number

a=1124
b=0
c=1
t=a
while t>0:
    d=t%10
    b=b+d
    c=c*d
    t=t//10
print('c:',c)
print('b:',b)
if b==c:
    print("spy number")
else:
    print("not a spy number")
    
        
#factorial

n=int(input("enter a:"))
a=1
b=1
while i<=n:
    f=f*i
    i+=1
print(f)

#reverse number

i=10
while i>=1:
    print(i)
    i-=1

#sum of number

n=int(input("enter n:"))
i=1
s=0
while i<=n:
    s=s+i
    i=i+i
print(s)

a=131
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
if a==b:
    print ("palindrome")
else:
    print ("not a palindrome")''''
