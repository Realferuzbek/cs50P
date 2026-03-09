-------- Quick NOTE ----------

Def = create/remember the function. 
Call = run the function.

----------------

def function_name ():
   # everything indented below belongs to this invented function

-----------------

# Difference: DEFINING vs CALLING
1) Defining 
    • Python reads the file top → bottom.

    • When Python reaches def function_name():, it registers/creates the function.

    • But it does NOT execute the indented lines inside the function yet untill we CALL it.

2) Calling
    • Calling is what triggers execution of the function body.

    • When you call it, Python jumps into the function and runs the indented lines.

# How to call
function_name()
    • function_name() means calling the defined function

------------------------

          Parameters in my own functions

Definition:
     • Parameter = the “slot” inside def (example: to)
     • When calling, I must fill that slot with an argument/variables (example: name)


Matching rule:

        • def hello(to): → must call like hello(something)

        • def hello(): → must call like hello()

Why parameters matter (greeting example)

# If my function has no parameter:

def hello():
    print("hello")

name = input("What's your name? ")
hello()

It can only say generic hello (no greeting).

# If my function has a parameter:

def hello(to):
    print("hello", to)

name = input("What's your name? ")
hello(name)

It can say hello + name, because it received the name when I called it.  

# u cant use "to"  when calling moment from inside of the defined function's parameter
# user's name = to  <- I mean will behave like this

----------------------------

    Giving a default value to a parameter in a def function
# Default = backup value used only when no argument is provided.

# Example

def hello(to="world"):
    print("hello,", to)

hello()                       # Uses default "world"
name = input("What's your name? ")
hello (name)                  # Uses the value in name

# Explanation

    • Writing to="world" means: to has a default value "world".

    • After = you can put a default value like:

        • numbers: 0, 10, 3.14
        • text (strings): "world" (quotes needed)
        • special values: True, False, None

    • If you call hello() with no argument, Python uses the default → to = "world".

    • If you call hello(name) with an argument, that argument replaces the default → to = name.

✅ Conclusion: With a default value, the function can be called with or without an argument.


----------------

# Rule: 
Python reads def first (registers functions). Function bodies run only when called.
So a function can call another function even if the other function’s def is written later, as long as the program calls main() after both are defined.

# Example 

def main():
    hello()

def hello():
    print("hello")

main( )

------------------

Scope:

✅ A variable created inside a function only exists inside that function.

# Example (WRONG)

def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello", name)        # name is located inside of the main function!

main()
