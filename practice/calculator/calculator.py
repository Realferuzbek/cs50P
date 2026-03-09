# Simple calculation
# x= 5
# y = 10

# print(x+y)

# Lil bit more advanced
# x = input("What's x? ")
# y = input("What's y? ")

# z = (x+y) # Wrong because + is str, not int!
# print(z)

# Lil bit more advanced P.2
# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)
# print(z)

# Lez make it a bit less lines 
# x = int(input("What's x? "))  # python start reading the codes first from the inside parenthesis!
# y = int(input("What's y? "))
# print(x+y)

# Programming Golden Rule: Make it simple, Make it readeable
# print(int(input("What's x? ")) + int(input("What's y? ")))

# New type of data, float, which supports decimal point
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# print(x+y)

# Let's round to the near integers
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x+y)
# print(z)

# Let's round to the near integers
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# print(round(x+y))

# Let's now put commas for each thousand numbers inside
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x+y)
# print(f"{z:,}")

# Let's now learn some dividents
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x/y, 2)  # The way it rounds like with changing the value. (1.2277 -> 1.23)
# print(f"{z}")      # The way it displays/formats without changing the value. (1.2222 -> 1.22)

# Let's now learn some dividents
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x/y)      # The way it rounds like with changing the value. (1.2222 -> 1)
print(f"{z:.2f}")   # The way it displays/formats without changing the value. (1.2222 -> 1.22 <- if not rounded!)