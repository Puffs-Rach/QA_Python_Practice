# if 

age = int(input("Enter your age: "))

if age >= 18:
    print("You are in category A")

if age >= 16:
    print("You are in category B")

if age <= 16:
    print("You are in category C")

# Using a elif

age = int(input("Enter your age: "))

if age >= 18:
    print("You are in category A")
elif age >= 16:
    print("You are in category B")
else:
    print("You are in category C")

# Calculator

print("1 Add +")
print("2. Subtract -")

operator = input("Please choose which you would like to do and what numbers): ")

if operator in ('1', '2'):
    number = int(input("Enter First Number: "))
    second_number = int(input("Enter Second Number: "))

    if operator =='1':
        print(number, "+", second_number, "=", number + second_number)

    elif operator == '2':
        print(number, "-", second_number, "=", number + second_number)

# Calculate exam grades

student_grade = int(input("Please enter student score: "))

# Pythagoras's Theorem

print("1. Find length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

Option_of_Operation = input("Enter which you want: ")

A = int()
B = int()
C = int()

A = 2 * (length + width)
print("Perimeter of the rectangle:", perimeter)

B = length * width
print("Area of the rectangle", area)

C = 2 ** (A + B)
print("The length of sides")