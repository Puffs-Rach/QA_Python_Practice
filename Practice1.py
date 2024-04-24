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
    

