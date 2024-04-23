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