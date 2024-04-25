# classes is a part of the object orientated programming
# key concepts:
# class - a blueprint - of attrubes (vars/args) and methods (functions) object.method 
# use class against an object
# object is an instance of the class
# allows us to easily make multiple objects of the same type.

class Dog: # class name start with a capitol. 
    energy = "high" # setting an attribute to the class

    def speak(self):# refers to the object we build
        print("bark")

fide = Dog() # makes an object called fido of the dog class

fido.speak()

fido.energy

class Students:
    pass

student1 = Students()
student2 = Students()

student1.first = "john"
student1.last = "smith"
student1.age = "10"

print(student1.age, student1.first)

class Student: 
    def __init__(x, first, last, age):
        x.first = first #the x parameter (self) referes to the object self.
        x.last = last # x maps the class data to the object
        x.age = age
    
    #__init__ method is called a dunder backgrond task and python is doing something for us. x can be anything. init method initialises the object (x) with the attributes

student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age, student2.age)


class Student: 
    def __init__(x, first, last, age):
        x.first = first
        x.last = last
        x.age = age
        x.full = first + " " + last

student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.full, student2.full)

class Student: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # self.full = first + " " + last

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.fullname())
print(Student.fullname(student2))#this is an argument

# change an attribute with a method

class Student: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # self.full = first + " " + last

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

    def change_age (self) #change age function
        self.age + int(self.age + 1)


student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age, student2.age)
# this is the object 
student1.change_age()
Student.change_age(student2)

# making a self class variable

class Student: 

    age_increase_amount = 25 #put variables at the top in a class. This means 

    def __init__(self, first, last, age): #functions
        self.first = first
        self.last = last
        self.age = age
       

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

    def change_age (self) #change age function
        self.age + int(self.age + self.age_increase_amount)


student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age)
student1.change_age
print(student1.age)

print(student1.age_increase_amount)
print(student2.age_increase_amount)

# __dict___

print(student1.__dict__)
print(Student.__dict__) # will return first, hohn, last, smith, age, 35. 

#change to variable

student1.age_increase_amount = 20
print(student1.__dict__) # this then prints back ge increase amount into variable but doesnt for student 2, has to be outside of hte functions


# non-self class variable



# creating a counter 

class Student: 

    age_increase_amount = 25 #put variables at the top in a class.
    num_of_students = 0 

    def __init__(self, first, last, age): #functions
        self.first = first
        self.last = last
        self.age = age
       

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

    def change_age (self) #change age function
        self.age + int(self.age + self.age_increase_amount)


student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age)
student1.change_age
print(student1.age)

print(student1.age_increase_amount)
print(student2.age_increase_amount)

# __dict___

print(student1.__dict__)
print(Student.__dict__) # will return first, hohn, last, smith, age, 35. 

#change to variable

student1.age_increase_amount = 20
print(student1.__dict__) # this then prints back ge increase amount into variable but doesnt for student 2, has to be outside of hte functions


# non-self class variable

