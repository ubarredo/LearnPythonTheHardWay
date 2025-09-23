print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# Below is the output where I gave input as string and number. 
# input() take as string and then we have to convert it to integer but here we are not converting.

# jas@jasmeen-E490:~$ /usr/bin/python3 /home/jas/Downloads/ex1.py
# How old are you? two
# How tall are you? two
# How much do you weight? two
# So, you're two old, two tall and two heavy.

# jas@jasmeen-E490:~$ /usr/bin/python3 /home/jas/Downloads/ex1.py
# How old are you? 33
# How tall are you? 5.5
# How much do you weight? 65
# So, you're 33 old, 5.5 tall and 65 heavy.