#Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#new_list = [num for num in a if num < 5]

thresh = int(input("Please input fib threshold: "))

a = 1
b = 1
new_list = [a, b]

while a <= thresh:
    new_list.append(a)
    a, b = b, a + b
print(new_list)

