# Ask user for their name
name=input("Hello, what's your name?").strip().title()
Hello()
print(name)



# Split their name
#first, last= name.split(" ")
#print(f"Hello, {first}") #Adjusting "first" to "name" makes it print both names #print("Hello," , name) is the another way to solve the earlier problem which is "," OR with "+" = means adding arguments

def hello():
    name = input("What's your name? ")
    print(f"hello, {name}").strip().title()
    

hello()

#Creating my own first function
def Hello():
    print("Hello")

# Ask user for their name
name=input("Hello, what's your name?").strip().title()
Hello()
print(name)

# Split their name
first, last= name.split(" ")
print(f"Hello, {first}") #Adjusting "first" to "name" makes it print both names #print("Hello," , name) is the another way to solve the earlier problem which is "," OR with "+" = means adding arguments