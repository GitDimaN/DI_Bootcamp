my_dict = {
    'first_name': 'Dima',
    'last_name': 'Negin',
    'courses': [
        {
            'title': 'Python Fundamentals',
            'hours': 100
        },
        {
            'title': 'AI Fundamentals',
            'hours': 50
        }
    ]
}
print(my_dict['courses'][1]['hours'])

print(my_dict.items())

for item in my_dict.items():
    (my_key, my_value) = item
    print(f"The key is: {my_key} and the value is: {my_value}")

my_dict['last_name'] = 'Neginsky'
print(my_dict['last_name'])

my_dict['age'] = 38
del my_dict['last_name']
print(my_dict.items())

print(my_dict.keys())
print(my_dict.values())

my_dict2 = {
    'city': 'Tel Aviv',
    'country': 'Israel'
}

my_dict.update(my_dict2)
print(my_dict)

# Exercise - removing certain keys from a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]
print(sample_dict.items())
# print(type(sample_dict.items()))
# unpack/drop the dict_items[] from the print
print(*sample_dict.items(), sep=",")

# check if a key exists in a dictionary
print('name' in sample_dict)

# For keys:
for e in sample_dict:
    print(e)

# For a key-value pair:
for a,b in sample_dict.items():
    print(str(a) + ": " + str(b))

my_str = list(range(1,10,3))
for i in range(len(my_str)):
    print(i)

# iterate through an object to get index-position and the value:
for i in enumerate(my_str):
    print(i)


# List Methods
# Map
# print("Map method:")
# my_list=[1,2,3]
# def mult2(x):
#     return x*2
# print(list(map(mult2, my_list)))

# Filter
print("filter method:")
my_list=[1,2,3]
def is_odd(x):
    return x % 2 != 0
print(list(filter(is_odd, my_list)))

my_list = list(range(5))
my_list2 = "Hello World".split()
my_list3 = [1.2, 1.5, 3.1]

print(my_list2)

for i in zip(my_list, my_list2, my_list3):
    print(i)


for i in zip(my_list, my_list2, my_list3):
    print(i)
    if i[0] == 0:
        break
else: # gets here if the whole loop iterated through the full list
    print("that's all!")

a = 0
while a < 5:
    a += 1
    print(f"a is {a} now")

    #if a > 3:
    #    break -> doesn't get to else oart

    if a > 3:
        continue # continue goes into next iteration without completing the current one
    print("I'm here")
else:
    print(f"in the else statement a is {a}")

if 10 > 5:
    pass # does nothing and also doesn't raise an error
print("we did nothing, but kept the structure for future modification instead of 'pass'")

# Comprehensions:

my_str = '12345'
my_list = []
for c in my_str:
    my_list.append(int(c))
print(my_list)
my_list2 = [int(c) for c in my_str]
print(my_list2)

my_new_list = []
for i in range(5):
    my_new_list.append(i*2)
print(my_new_list)

my_new_list2 = [i*2 for i in range(5)]
print(my_new_list2)
# comprehension with a loop and a condition
my_new_list3 = [i*2 for i in range(5) if i % 2 == 0]
print(my_new_list3)

my_str = "Hello World"
vowels_chars = ['a','e','i','o','u']
mod_str = [a.upper() for a in my_str if a in vowels_chars]
print("".join(mod_str))

# nested loop:
my_list = []
for i in range(5):
    for j in [10, 100, 1000]:
        my_list.append(i * j)
print(my_list)
# via comprehension
my_list2 = [i*j for i in range(5) for j in [10, 100, 1000]]
print(my_list2)

# comprehension applied to construct a dictionary
family_age = {
    'Lea': 12,
    'Mark': 25,
    'George': 50
}
new_year = 1
new_family_age = {name: age + new_year for (name, age) in family_age.items()}
print(new_family_age.items())

my_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    #'age': 30
}

new_name = ["New Name", "New Last Name"]
my_new_dict = {key: value for (key, value) in zip(my_dict.keys(), new_name)}
#my_new_dict = {a: new_name[i] for (a,b) in my_dict.items() for i in range(len(new_name))}
print(my_new_dict)

