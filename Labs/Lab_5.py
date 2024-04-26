#Lab 5

from statistics import mean
from statistics import median

grades = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = [int(grade) for grade in grades.split(",")]
average_grade = mean(grades)
median_grade = median(grades)

def minimum_grade(grades):
    return min(grades)

def maximum_grade(grades):
    return max(grades)
    
print("Grades:", grades)
print("Minimum grade is: ", minimum_grade(grades))
print("Maximum grade is: ", maximum_grade(grades))
print("Average grade is: ", round(average_grade, 2))
print("Median grade is: ", median_grade)
