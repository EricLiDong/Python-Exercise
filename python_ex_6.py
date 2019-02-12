#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

str = input("Please input a string to test: ")

str_rev = str[::-1]

if str == str_rev:
    print("This is a palindrome!")
else:
    print("Not a palindrome!")
