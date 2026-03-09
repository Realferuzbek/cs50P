# Simple way of saying hello
# print("hello, world")

# Bit beginner friendly
# input("What's your name? ")
# print("hello, world")

# #When you want your name to be printed
# name = input("What's your name? ")
# print("hello, " + name)

# When you want your name to be printed (beginner)
# name = input("What's your name? ")
# print("Hello, ")
# print(name)


# When you want your name to be printed (annoying version)
# name = input("What's your name? ")
# print("hello, " + name)

#When you want your name to be printed(recomended)
# name = input("What's your name? ")
# print("hello,",name)

#trying new parameter called end"/n"
# name = input("What's your name? ")
# print("Hello, " , end=name)

#
# name = input("What's your name? ")
# print("Hello" , name , sep="Wow")

#Default version
# name = input("What's your name? ")
# print("Hello" , name , sep="")

# # What if want to print the quotation mark (wrong) 
# print("Hello, "friend"") 

# What if want to print the quotation mark (correct and the best way) 
# print('Hello, "friend"') 

# What if want to print the quotation mark (hard way)
# print("Hello, \"friend\"") 

# Modern way of saying user's name (I am not done yet as it is wrong, I thought that curly makes that as special as it prints the user's name, but it wont)
# name = input("What's your name? ")
# print("hello, {name}")

# Modern way of saying user's name (correct) just add f which is format at the beginning of arg witht he curly braket
# name = input("What's your name? ")
# print(f"hello, {name}")

# Now we explore and solve the problem of as the users make the unconcsious mistakes of writing their names in lowercase, or spacing double times

# Get the user's name
# name = input("What's your name? ")

# # Remove whitespace bar from str
# name = name.strip()

# # Capitalize user's name
# name = name.capitalize()

# # Give/print user's name
# print(f"hello, {name}")


# # What if I want to capitalize my surname, capitilize every single title written behaviour

# # Get the user's name
# name = input("What's your name? ")

# # Remove whitespace bar from str
# name = name.strip()

# # Capitalize user's name
# name = name.title()

# # Give/print user's name
# print(f"hello, {name}")

# # How about making it less line of codes 

# # Get the user's name
# name = input("What's your name? ")

# # Remove whitespace bar and capitilize
# name = name.strip().title()

# # Give/print user's name
# print(f"hello, {name}")

# # How about even fewer
# name = input("What's your name? ").strip().title()
# print(f"Hello, {name}")

# How to greet users with their first or surnames only

name = input("What's your name? ").title().strip()
first, last = name.split(" ")
print(f"Hello, {first}")