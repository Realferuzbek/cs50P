def main():
    name=input("What's your name? ")  # noqa: F841
    main(main)
    

def hello(to="world"):
    print ("hello,", to)
    
name=input("What's your name? ")
hello(name)