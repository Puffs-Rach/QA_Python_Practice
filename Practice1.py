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