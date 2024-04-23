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



