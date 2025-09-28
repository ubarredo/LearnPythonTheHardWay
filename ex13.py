from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# in below script, I dont understand how come ex1.py came in place of script. why not script

# jas@jasmeen-E490:~/Downloads$ python3 ex1.py first second third
# The script is called: ex1.py
# Your first variable is: first
# Your second variable is: second
# Your third variable is: third

#################################################################

# in below script i tried giving argv as input from user but i do not get the expected output

# from sys import argv

# # read the WYSS section for how to run this

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weight? ")


# script, age, height, weight = argv

# print("The script is called:", script)
# print("Your age is:", age)
# print("Your height  is:", height)
# print("Your weight  is:", weight)

# jas@jasmeen-E490:~/Downloads$ python3 ex1.py age height weight
# How old are you? 33
# How tall are you? 5.6
# How much do you weight? 65
# The script is called: ex1.py
# Your age is: age
# Your height  is: height
# Your weight  is: weight