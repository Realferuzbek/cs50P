# Keywords:
   return

# Explanation:
  • return is a keyword.
        • It sends a value back to whoever called the function.

# Example
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):      # n is a parameter
    return n * n

main()

# Other ways to square:
    • return n ** 2
    • return pow(n, 2)