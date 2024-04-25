print("hello world")

print("person 1: \tHey how are you?\nPerson 2 : \tGood thanks! \U0001F604")

length = "50"
length = int(length)

width = "40"
width =int(width)

perimeter = 2 * (length + width)
print("Perimeter of the rectangle:", perimeter)

area = length * width
print("Area of the rectangle", area)

name = "root"

if name not in ("root", "admin", "user"):
    print("accepted")
else:
    print("invalid")

x = int(input(70))

weigt = float(input)


# Iteration is another word for loops, repeating blocks of code over and over
# 2 types of loop - while and for
# if a condition is never true the while loop will never start
# adding 1 to the value of x. x is now 1. keeps going until x is 101 and stops because its reached the limit

x = 0
while x < 101:
    print(x)
    x += 1

# Break

i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i +=1

# continue, skipping the current iteration.jumps on to the main iteration.

j = 0
while j < 6:
    j += 1
    if j == 3:
        continue
    print(j)

# while true- must have a clearly defined way of existing/breaking

while True:
    name = input("enter your name: ")
    if name == "quit":
        break
    else:
        print(f"hello {name}")

# for loops
# a for loop will iterate over an collection - lists/strings/dictionaries any iterable. useful for when we want to use the data in a collecton.

# iterating through a list:
# x represents the tiems in the iterable 
# for item in iterable

my_fruits = ["apple", "orange", "kiwi"]
    #item    #iterable
for fruit in my_fruits:
    print(fruit)

numbers = [ 1, 2, 3, 4, 5]
    
for number in numbers:
        print(number)

1 = 0 


#while loop for above

while l < len(numbers)
    print(numbers[l])
    l += 1

# infinite use while
# forloop is for a iterable collection

# Range for loop
# up to but not including the last number
# They are only hitting the first 4 numbers

for a in range(5):
    print(a)

for a in range(1, 5):
    print(a)

# high number not included, this example goes up in steps of 2. starts at 1, up to 10, skips ever 2
for a in range(1, 10, 2):
    print(a)

# strings
#would use each letter as a seperate thing. so H E L L O

for letter in "hello":
    print(letter)

# splits the word

for word in "hello world".split():
    print(word)

# List Comprehension
        #expression item  iterable 

result = [x**2 for x in range(5)]
print(result)

#expression is what we awant to do to the item in the iterable. going to be square rooting. x to the power of 2 for what in each item in. up to range of 5. answer is [0,1,4,9,16]

result = []

for x in range (5):
    result.append(x**2)
print(result)

# wanting to grab all the even numbers and square them

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        #expression   item  from     iterable  using what condition
even_numbers_squared = [number**2 for number in numbers if number % 2 == 0]
print(even_numbers_squared)

# if the data type is different and we need to tell it its an integer from a string.

numbers = ["1", "2", "3", "4"]
even_numbers_squared = [int(number**2) for number in numbers if number % 2 == 0]
print(even_numbers_squared)

# Dictionary. prints vale
          # key    value
for i in {"drink": "wine"}:
    print(i)

# invoking the dictionary menthod, pulling out the value
for i in {"drink": "wine"}.values():
    print(i)

# iterate through dictionaries
for i in {"drink" : "wine"}.items():
    print(i)

# Break

for i in range(10):
    if i == 5:
        break
    print(i)

# Nested loop. for i (1) in 1 - 3, and then for 1 in 1 to 4 print 1 times 1 rthis is the 

for i in range(1,3):
    for j in range(1,4):
        print(i, "x", j, "=", i*j)

# write a loop that asks for 5 names (as user input)
# for each name prints it out + "is great".

# while loop

# functions - a block of code - either preforms a task or returns a value.
# repeatability. 

def greet(name): #parameters that in arguments
    print(f"hi {name}")
greet("chris")


def greet_1(first_name, second_name, age):
    print(f"{first_name} {second_name} is {age}")

greet_1("chris", "reeves", 30)
# on the command line cant use print and cant use input. better to use return as we can store the value.

def greeter(name):
    return f"hello {name}"

    # not going to be doing anything conditional, no printing required. Can store this in a data type variable.

x = greeter("chris")
print(x)

# default is def values
# parameters in python

def greet3(name, age=10 =):
    return f"{name} is {age}"

print(greet3("chris")) # chris is 10
print(greet3("chris, 20")) # chris is 20

def make_Pizza(size, *toppings):
    print(f"order for {size}- inch pizza, with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_Pizza(12, "mushrooms","Green peppers")

# key word arguments- kwargs
# send args as key:value pairs.

def fruit_list(fruit1, fruit2, fruit3):
    print(f"fav fruit is {fruit1}")
    print(f)

#** is a kwarg

def fav_food(**food):
    print(f"fav food is", food["dessert"], "not", food["fruit"])

    fave_food(dessert="Ice-cream", fruit="apple", dairy="milk")
    # fave food is dessert not apple

# / - a marker dividig positional-only parameters from the rest
# before / the params must be in order.

def example(a, b, c, )


setting up parameters, wat do I want to be passed through. 

print("my name is {}, iam {}, my height is {}".format(name, age, height))

x = "my name is {}, i am {}, my height is {}"
print(x.format(name))


# list comprehension
- previous labs 5 and 6, extra functions challeges if time. rock paper scissors app (if time but tomorrow as well)

# While loop

count = 0
while count < 5:
    name = input("Enter a name: ")
    print(name + " is great")
    count += 1

# for loop

for count in range(5):
    name = input("Enter a name: ")
    print(name + " is great")

# list comprehension

# Collect names using list comprehension
names = [input("Enter a name: ") for count in range (5)]

# Print each name followed by "is great" on separate lines
for name in names:
    print(name + " is great")

# list comprehension 1 line of code only

[print(input("Enter a name: ") + " is great") for count in range(5)]

[print(f"{name} is great!") for name in [input("enter a name") for x in range(5)]]

rewrite without any if statemetns
or any inbuilf function like max()

# If number is bigger than other number then print larger number
num = 10
num1 = 20

if num > num1:
    print(num)
else:
    print(num1)

result (num - num1) * (num1 > num) + num1

# number is greater than num1 so that is false. so now is 0. now we add num1 is greater than 1 times num1.
largest = num * (num > num1) + num1 * (num1 > num)

print(largest)


budget = input
shakes = {"1": (flavour, 3),}

while True:
    

length = 50

width = 40

perimeter = 2 * (length + width)
print("Perimeter of the rectangle:", perimeter)

area = length * width
print("Area of the rectangle", area)

books = {"author1": ["book1", "book2"], "author2": ["book3", "book 4"]}


books = {"JK Rowling": ["Goblet of Fire", "Deathly Hallows"], "CS Lewis": ["Lion, Witch, Wardrobe", "Prince Caspian"]}

print(books["JK Rowling"])
print(books.get("JK Rowlinggg", "not-found"))

x = int(input("70"))
if x >= 85:
    print("distinction")
elif x >= 65:
    print("pass")
else:
    print("Fail")
    


deposit = 100
password = "password"

if 0 < deposit <=100 or password == "password":
    print(f"thankyou for deposit of £{deposit}.")
else:
    print("failed to deposit")

if not 0 < deposit <=100 or password != "password":
    print("failed to deposit")
else:
    print("ok")
    
# in and not in
# () is a tuple

name = "root"
if name in ("root", "admin", "user"):
    print("invalid username")
else:
    print("accepted")
    
if name not in ("root", "admin", "user"):
    print("accepted")

# conversion is a new variable
# f is an f string, stands for format, format then calls the variable in the string. used instead of ending a string and adding a plus.

weight = float(input("Enter weight: "))
unit = input("KGS or LBS: ")

if unit.upper() == "KGS":
    conversion = weight / 0.45
    print(f'your weight in pounds is {conversion}')

elif unit.upper() == "LBS":
    conversion = weight * 0.45
    print(f"your weight in Kilo is {conversion}")
    KGS = float(input("Enter weight: "))
else:
    print("invalid unit entered")
    

try:
    weight = float(input("enter weight: "))
except ValueError:
    print("invalid input. Please enter a numeric value.")


# Dictionaries vs Lists
# This is a list inside a function. This function check_password, contains a list of common_assword which stores some common passwords as strings.

def check_password():
    common_passwords = [
        "password"
        "password123"
        "1234556789"
    ]

user_password = input("What is your password? ")
if user_password in common_passwords:
    print(f"Use a stronger password '{user_password} is not safe enough.")
else:
    print("Password is strong.")
