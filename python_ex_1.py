#Ask the user for name and age and return the year that he will turn to 100

import datetime

name = input("Give me your name: ")
age = int(input("Give me your age: "))
repeats = int(input("How many times to do you want to see this?: "))
now = datetime.datetime.now()
answer = now.year + 100 - age
for i in range(repeats):
    print("%s you will turn to 100 in the year of %d" %(name, answer))