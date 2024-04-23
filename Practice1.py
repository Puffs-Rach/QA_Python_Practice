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
if unit


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

