luckynum = "7"
guess= []
guesscount = 0
out_of_guesses = False
guess_limit = 5
name = input("Enter name: ")
print("Welcome aboard " + name)
print("Let's play a guessing game!")
print("Choose any number between 1 to 9 ")
while guess != luckynum and not(out_of_guesses) :
    if guesscount < guess_limit:
        guess = (input("Guess my lucky number: " ))
        guesscount += 1
        if guess!=luckynum:
            print("Sorry! Try again.")
    else:
        out_of_guesses= True
        print("Out of guesses. Too bad.")
if guess==luckynum:
    print("Well Done! You have guessed the correct number. You should be a psychic!")