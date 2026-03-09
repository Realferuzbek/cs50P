emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?") #In here, the argument will go and match as like phrase = "Is anyone there"
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):
    print (phrase, emoticon)

main()