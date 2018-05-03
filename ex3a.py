# exercise 3a, find something you need calculated and write a new .py file that does it.

# calculator cost per round of ammo!

print("how many rounds?")
try:
    rounds=float(input(":"))
except ValueError:
    print("Not a number!")

print("price?")
try:
    price=float(input(":"))
except ValueError:
    print("Not a number!")

print("shipping costs?")
try:
    shipping=float(input(":"))
except ValueError:
    print("Not a number!")


print("cost per round is:", (price+shipping)/rounds)
