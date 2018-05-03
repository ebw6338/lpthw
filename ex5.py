# ex5.py
# more variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"let's talk about {name}.")
print(f"he's {height} inches tall")
print(f"he's {weight} pounds heavy")
print("actually that's not too heavy")
print(f"he's got {eyes} eyes and {hair} hair")
print(f"his teeth are usually {teeth} depending on coffee")

total = age + height + weight
print(f"if I add {age}, {height}, and {weight} I get {total}")

# study drills
# 1 change the variables to remove ''
# 2 write variables that convert to metric

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
cm = height * 2.54
kg = weight / 2.2
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"let's talk about {name}.")
print(f"he's {height} inches tall")
print(f"he's {weight} pounds heavy")
print(f"in metric that's {cm} centimeters and {kg} kilograms")
print("actually that's not too heavy")
print(f"he's got {eyes} eyes and {hair} hair")
print(f"his teeth are usually {teeth} depending on coffee")

total = age + height + weight
print(f"if I add {age}, {height}, and {weight} I get {total}")
