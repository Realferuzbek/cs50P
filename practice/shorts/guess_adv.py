def main():
    guess = user_guess()
    return guess        # In here it returns the output

def user_guess():
    guess = int(input("Enter a guess: "))
    if guess == 50:
        print("Correct! ")
    else:
        print("Incorrect! ")
    
main()
