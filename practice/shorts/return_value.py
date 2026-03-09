# Printing values where variables are usable once
def greet(input):
    if "hello" in input:
        print("hello, there")
    else:
        print ("I'm not sure what you mean")

greeting = greet("hello, computer")

# Returning values where variables are usable unlimited
def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = greet("hello, computer")     # Variables are containers, let's say

print(greeting, "Feruzbek")     # But when I used print function, I couldn't add "Feruzbek"