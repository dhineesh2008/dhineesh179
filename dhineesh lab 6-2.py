'''#List Tasks
#Create a list of 5 student names and display it.
a=['dhineesh','raghav','sai','vipul']
for ch in a:
    print(ch)

#Add a new element to the list using append().
b = [7,11,16,5]
b.add(37)
print(b)

# Insert an element at the 2nd position.
c=[6,9,7,4]
print(c[2])

#Remove an element from the list.
d=[1,2,3,4,5,6]
d.remove(5)
print(d)

#Find the length of the list.
e=[8,7,6,5,4,3]
e.len()
print(e)

#Reverse the list
f=[9,6,5,3]
f.reverse()
print(f)

#Find the largest number in a list.
g=[4,5,6,7,70,90]
g.max()
print(g)

#Count the occurrence of an element.
h=[7,8,9,3,5,1,6]
h.count(4)
print(h)

#Tuple Tasks
#Create a tuple of 5 numbers and display it.
i=(1,2,3,4,5)
print(i)

#Find the length of a tuple.
j=(5,7,8,9)
print(len(j))

#Count how many times an element occurs in a tuple.
k=(1,2,3,4,5,6,7,8,9)
print(k.index(9))

#Find the index of a given element.
l=(8,5,7,4,9)
print(l.index(2))


#Create a tuple containing different data types.
m=(2,4,6,8,10,12,14,16,18)
print(max(m))
print(min(m))

# Set Tasks
#Create a set of 5 numbers and display it.
n=(2,4,6,8,10)
print(n)

#Add a new element to the set
o=(1,4,7,6,9,3)
o.add(10)
print(o)

#Remove an element using remove().
p=(1,3,5,7,9)
p.remove(7)
print(p)

#Remove an element using discard().
q=(2,4,6,8,10)
q.discare(6)
print(q)'''

#Find the union of two sets.
r=(1,3,5,7,9)
s=(2,4,6,8,10)
print(r.union(s))

#Find the intersection of two sets.
u={1,7,4,9}
v={2,4,7,8}
print{u.intersection(v)}

#Find the difference between two sets.
w={1,2,6,7,9}
x={3,4,7,9}
print(w.difference(x))
#Check whether one set is a subset of another set.
z={1,2,3,45}
a={4,5,67,8,9}
print(z.issubset(a))


#Check whether one set is a superset of another set.
b={1,3,5,7}
c={2,4,6,8}
print(b.issupperset(C))


#Find common elements between two sets.
d={2,4,7,8,10}
e={1,3,5,8,7,9}
print(d.intersection(e))

#Store student names in a list, tuple, and set and compare the outputs.

# list
f=[dhakshithaa,sara,mica,bharathi]
print(f)

#tuple
i=(dhakshithaa,sara,mica,bharathi)
print(i)

#set
j={dhakshithaa,sara,mica,bharathi}
print(j)
