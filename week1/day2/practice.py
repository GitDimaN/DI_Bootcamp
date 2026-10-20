# Practice with lists, ranges

a= list(range(1,10))
print(a)
print(a[1])
print(a[::-1])
print(a[0:4])
print(4 in a)

b = ["rose", "tulip", "lily", "iris", "orchid"]
b.append("frog") # to add 1 element
print(b)

c = ["cat","dog"]
b.extend(c) # adds multiple alements to the end
print(b)

b.insert(2,"hamster") # inserst an element to the list in the specified index-position
print(b)

b.remove("hamster") # removes the first  occurence of this element from the list
print(b)

b.pop() # removing last 1 element by default or at specified index
print(b)

# b.clear() # empties the full list
# print(b)

b.sort() # sorts a list in alphabetic or ascending order
print(b)
c = [0,-10,4,5,20,11]
c.sort()
print(c)

c = [0,-10,4,5,20,11]
print(sorted(c, reverse=True)) # reversing the order

d = c # d becomes a pointer to c
d.append(100) # adding smth to d, actually adds it to c to which d points
c.append(111)
print(c)
print(d)
print("\n")

e = c.copy() # creates actual copy, not just a pointer
e.append(101)
print(c)
print(d)
print(e)
print("\n")

f = c[:] # pythonic way to create an actual copy, not just a pointer
f.append(1000000)
print(c)
print(f)
print("\n")

del d[3]
print(d)

print(f + e) 

# Task 1: create a list 'l' with first 5 even numbers, starting from 2
# Task 2: Print a list created using this pattern [a[i], a[i]**2,a[i+1],a[i+1]**2,...]

l=list()
for i in range(1,6): l.append(i*2)
l = list(range(2,11,2)) # last parameter does the step-size in the range
print(l)

l_2=list()
for i in range(len(l)):
    l_2.extend([l[i],l[i]**2])
print(sorted(l_2, reverse=True))

l_3=[]
for elem in l:
    l_3+=([elem,elem**2])
print(sorted(l_3, reverse=True))

print("\n")


# Immutable iterables e.g. tuples, where each element is fixed/assigned once and can't change separately
# the are useful cause also memory allocaiton is known/fixed from the beginning, unlike lists that can grow
my_tuple = (1,2,3)
# my_tuple[0] = 10 # --> TypeError, becase cannot re-assign/change elements, they are set once and for all
print(my_tuple)

my_tuple2 = (0,10,20)
my_tuple = my_tuple2
print(my_tuple)
(a,b,c) = my_tuple # unpacking data
print(c)

my_tuple = (10, 10, 10)
my_list = [10, 10, 10]
my_set = set() # sets have unique objects in it
my_set.add(10);my_set.add(10);my_set.add(10);my_set.add(3)
print(my_set)

my_list = [1, 50, 20, 15]
print(max(my_list), min(my_list))
print(min(my_tuple))
print(f"sum of elements in my list: {sum(my_list)}")
print(min(my_set))

# play with strings
s = "Hello World Hello"
print(s.find("hell"),s.find("Hell")) # find returns only the first occurence
print(s.find("old")) # returns -1 when fails
print(len(s))
print(s.replace("World", "Sky")) 
print(s.replace("Hello", "Morning")) #replaces all occurences with the new sub-string
print(s.split()) #splitting string into list of elements
print(s.count("Hello")) # find number of occurences of a substring
print(s[::-1]) # reverse order of characters in a string
print(s.swapcase()) # swap from lower to upper and vice versa
s += " "
print(s)
print(s.strip()) # removes last space(?)
x = s.split()
print(x)
z=["dima",2]
print(z)
print(str(z)) #??

# While Loop
i=1
while True:
    print("A")
    i += 1
    if i > 5:
        break

i=1
while i < 5:
    print("A")
    i += 1


my_tuple = (1+3, 2.7, 'Thursday')
print(my_tuple)