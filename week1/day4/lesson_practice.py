#RECAP from before:
expressions = {
    'booleans': [
        bool(None),        
        'a' > '?',
        str(5) in '5',
        float(0.99) == int(0.99),
        not bool('A')
    ],
    'numbers': [
        (' ' in 'Hello World') * 3.5,        
        True + 5,
        'Magical'.count('a') - 6.5,
        sum(x for x in range(11)),
        sum(x for x in range(3, 13, 3) if x % 3 < 2)
    ]
}
print(sum(expressions['booleans']))


print([x for x in expressions['numbers'] if x > 0])
print(sum([x for x in expressions['numbers'] if x > 0])/len([x for x in expressions['numbers'] if x > 0]))

# NEW DAY 4 TOPICS:

#def say_hello (username, language):
def say_hello(username, message, language="en"): # default value "en" for parameter language
    if language =='en':
        print(f"Hello {username} {message}")
    elif language =='fr':
        print(f"Bonjour {username} {message}")
    else:
        print("I'm sorry, I don't speak your language")


#say_hello()
say_hello("Dima", 'en')
say_hello("Mary", "fr")
say_hello("ABC", "he")
say_hello("ABC", message="Nice to meet you!") # will use default parameter value "en"

def my_sum(*args): # for tuple inputs
    print(args)
    sum = 0
    for i in args:
        sum += i
    return sum

print(my_sum(1,2,3,4,5)) # passes a tuple to arg

def my_fct(**kwargs): 
    # key-word values, i.e. keyword and value, 
    # accepts it as a dicitionary inside the function body
    print(f"My args look like {kwargs}")
    print(kwargs['username'])

print(my_fct(username="Mary", age=18, language="e"))


def my_fct(username,*args,**kwargs): 
    # key-word values, i.e. keyword and value, 
    # accepts it as a dicitionary inside the function body
    print(f"username: {username}")
    print(f"My args look like {args}")
    print(f"My kwargs look like {kwargs}")
    print(kwargs['language'])

print(my_fct("Mary", 5, 8, age=18, language="he"))

# def calculator(*args, operation='+'):
#     sum = 0
#     print(f"my args are: {args}")
#     for k in args:
#         if operation == '-':
#             sum -= k
#         else:
#             sum += k
#     return sum

# print(calculator(1,2,3,4,'+'))

def calculator1(*args, operation = "+"):
    result = 0
    print(f"my args are: {args}")
    if len(args) <= 1:
        print("be aware that your input contains less that two numbers")
    if operation == '-':
        for k in args:
            result -= k
    else:
        result = sum(args)
    return result

print(calculator1(1,2,3.5,4))

# MAP
fruit = ["apple","banana","pear","apricot"]

def make_uppercased(item):
    return item.upper()
def make_lowercased(item):
    return item.lower()
def make_organic(item):
    return item + ' organic'

print(list(map(make_uppercased, fruit)))
print(list(map(make_lowercased, fruit)))
print(list(map(make_organic, fruit)))

print(list(map(lambda i: i.upper(), fruit)))
print(list(map(lambda i: i.lower(), fruit)))
print(list(map(lambda i: i + " organic", fruit)))

print(list(filter(lambda i: i[0] =='a', fruit)))

from functools import reduce

numbers = [1,2,3,4]
print(reduce(lambda a, b: a + b, numbers))


def calc (*args, operation = "+"):
    if len(args)<2:
        return "We need at least two numbers"
    if operation == '+':
        return sum(args)
    if operation != '-':
        return "The operation is incorrect"
    #args2 = -args[0] + args[1:]
    return reduce(lambda a, b: a - b, args)

print(calc(1,2,3,4,'-'))