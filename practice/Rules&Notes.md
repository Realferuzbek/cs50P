Output differences:
    return value
    side effects
    

# Rules:

1. Don't make function and variables name same!
2. 


Scope:

✅ A variable created inside a function only exists inside that function.

# Example (WRONG)

def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello", name)        # name is located inside of the main function!

main()

---------------

Core Python buckets (so far)

Keywords
Language commands (not functions).
Examples: def, return

Functions
Callable actions.
Examples: print(), input(), round()

Methods (string methods)
Functions that belong to a value like a string.
Examples: "hi".strip(), "hi".title()

Types / Classes
What a value is.
Examples: str, int, float

Values (literals)
Actual data.
Examples: "hello", 10, 3.14

Variables
Names pointing to values.
Examples: name, x, y

Parameters
Variables inside a function definition (input “slots”).
Example: def hello(to): → to is a parameter

Arguments
The real values you pass into a call.
Example: hello(name) → name (its value) is the argument

Return value (you’ve met this now)
What a function gives back with return.
Example: return n * n

Operators (you’ve used these too)
Symbols like math/combining.
Examples: +, -, *, /, %, =

Outside Python (tooling)

Terminal commands / shortcuts
Examples: python, deactivate, Ctrl+L

------------------

# String methods

capitilize() 
.title()
.split(" ")
.strip()
.append
.join()
.replace()
sep=
f" {} "

# Functions:

input()
print()
int()
float()
round()
pow()
def smth ():

# IF Else function
    if variable == 50:
        print("smth")
    else:
        print("smth else")

------

def greet(input):
    if "hello" in input:            # in means inside literally!
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = greet("hello, there")

-----------

SHOWS = ["smth" , "smth else"]
def main():
    for show in SHOWS:
        print(show)

# Means show variable is equal to each arguments in the SHOWS list.

# Keywords:
    # Tiny rule: Keywords dont take parenthesis

global variable     #global makes variables modifiable, which has side effects.
return
def 
if ~ in , variable
else


for
while
try
except
class
import
from
pass
break
continue
True
False
None

# Operators

+ 
- 
* 
** -> power operator #Ex: n ** 2 -> n^2
* is the operator for unpacking lists of arguments
    # print(*input().split(), sep="...") # Output: "smth , "smth" smth"   # THEN sep works! #smth...smth
So, with * it sees as an each words as arguments!
   
   # print(input().split(), sep="...") # Output: [smth, smth, smth]

# Terminal Functions:
1. python
2. deactivate
3. Ctrl + L
4. Ctrl + Z + Enter
5. Ctrl + Z
6. Ctrl + F -> search/type the word 
7. clear AND/OR (Ctrl+L) = clears the terminal(not remove)
8. ls = List of all files and folders with the bytes(1,000,000 bytes=1mb)
9. cp "existing file" "new file" = copy the whole file with its all code into new file/folder i want
10. mv "existing file" "newfile" = rename the existing file to "newfile"
11. rm "existing file" = delete the existing file
12. mv "insideofthefolder's filename" .. = moving this file from inside of the folder while my terminal indeed being in that folder(cd) to the outside like just file itself but not belong to any other folder's inside!
13. cd .. = fully come back(show/focus) to the main project's folder
14. rmdir "existingfolder" = delete the folder 

# Editor Functions:
Editor Hacks/functions:
Ctrl + F -> search/type the word -> for that opened file inside
Ctrl + shift + F -> search/type the word -> for searching the whole project's words
Ctrl + ,  -> Open settings
Ctrl + Z -> Undo
Ctrl + X -> Redo
- Select the lines, and Ctrl + / it will add # to each lines of codes u selected
Pseudocode(syudokod) -> same as the comment, it is just to-do-list to express myself algorithmitically, methodically, succinticately

# Git
U = Untracked (new file, not added to git yet)
M = Modified (tracked file that I changed)
