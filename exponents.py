# exponents.py
# Ask the user for a number, then raise it to powers using ** (exponent operator).

# input() gives back text, so int() turns it into a number
number = int(input("Enter a number: "))

# ** is the exponent operator
squared = number ** 2
cubed = number ** 3

# Commas let print() show text and numbers together
print(number, "squared is", squared)
print(number, "cubed is", cubed)
