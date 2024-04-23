
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

