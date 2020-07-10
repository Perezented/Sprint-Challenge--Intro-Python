# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
# going to look at the names and attempt to split their letters of their names to get the first letter
# if the first item is 'D', return it
a = []
for n in humans:
    if n.name[0] == "D":
        a.append(n.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# check the last letter of their name using a negative index to see if it matches the letter e
b = []
for e in humans:
    if e.name[-1] == 'e':
        b.append(e.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# if the letters are between c and g, append it to c
# looks like i'll be bringing in a string dependency
import string
c = []
for letter in (string.ascii_uppercase[2:7]):
    for name in humans:
        if name.name[0] == letter:
            c.append(name.name)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# get each human and return the ages plus 10
d = [hu.age + 10 for hu in humans]

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# get the persons and concat a '-' in between
e = [person.name + '-' + str(person.age) for person in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for p in humans:
    if 27 < p.age > 32:
        f.append((p.name, p.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
# for each human in humans, I want to return human.name uppercased
# and add 5 to their age. Making uppercased names ages you.
g = [hum.name.upper() + ', ' + str(hum.age + 5) for hum in humans]

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(t.age) for t in humans]
print(h)
