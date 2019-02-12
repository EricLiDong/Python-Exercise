#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

#Extras:

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.



num = int(input("What the is target number?: "))
check = int(input("What is the number to check?: "))
if num%check == 0:
    print("%d is divisible by %d!" % (num, check))
else:
    print("%d is NOT divisible by %d!" % (num, check))

