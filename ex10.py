tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

height = "I am 6'2\" tall."  # escape double-quote inside string
height2 = 'I am 6\'2" tall.'  # escape single-quote inside string
height3 = """
I am 6'2" tall
I am 6'2" tall
"""

print(f"{height} \n{height2} {height3}")