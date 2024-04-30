# modules
# modules are just files that we can use to extend our functionality. can pip install loads of bits. we can import existing modules and install other modules
# Many modules are build in
# Install using pip.
# Dev to test to environment
# app.py,main.py
# keep them in a reqirements.txt, copy in what the requirements are
# q to quit
# added into the metadata by using a doc string """"


import math #imports entire module

number = 10

answer = math.sqrt(number) # modulename.method(args)

print(answer)

import math
import random

def random_pi():
    """
    Function to times pi by a random number between 1 and 10
    """
    return math.ceil(random.randint(1,10) * math.pi)

for i in range(5):
    print(random_pi)

print(dir(random))
help(math)



import boss

boss.good_boss("john")

# Files
# importance of file handling:
# storing and rtrieving data
# Configuring systems
# Sharing data between apps/software
# logs 
# dont store logs locally on production envronment due to space issues and virutal machine. storage in an s3 bucket is a good place to out
# reda, write, edit files
# most file types are supported, some will need to import modules
# focus on txt files
# read mode ("r"): defialt mode - "w" and "a"

file = open("file.txt", "mode")
...
file.close() # must remember to close a file. most recent file will close.


# Reading
x = file.read() - reads the entire file sll conttent could be in x. 

file = open("lines.txt", "r")
lines = file.readlines()
print(lines)

for n in range(1,11)
    newline = "this is a new line" + " " + str(n) + "\n"
    file.write(newline)

file.close()


open a new text file (w mode) - called teams.txt - add the names of 5 sports teams
list of team names with a for loop to put it in the file. 
read and display the names of the 1st and 4th team using (.strip())
edit the file so that the top line is replaced with "this is a new line"
print out the edited file line by line

list =[man city, real madrid....]

file = open("teams.txt", "w")
    teams = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5"]
    for team in teams:
    file.write(team + "\n")
# Close the file
    file.close()

with open("teams.txt", "w") as file:
    teams = ["Man City", "Arsenal", "Tottenham", "Sunderland", "Wrexham"]
    for team in teams:
        file.write(team + "\n")

with open("teams.txt", "r") as file:
    team_name = file.readlines()
    print

file.close()

open file r

read
print 1 and 4 line

close


open file r

read as list
update line 1 (index 0)

reopen in w

for loop to write to file

close

open in r

for loop to print each line.