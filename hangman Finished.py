
#Start of game
name = input("pls enter your name: ")
print("Hello,", name, "Time to play hangman.")

#preparing all variables and lists
answer = "frbjhbdhbddcd"  #set the answer as anything you like
noOfGuessesLeft = 10
correct = False
blanks = ""
length = len(answer)
for i in range(length):
    blanks += "_"
blanksList = []
correctDigitsThisRound = []
UsedLetters = []
dupelicate = False
UsedLettersStr = ""
count = 0


#main gmae loop
while blanks != answer and noOfGuessesLeft > 0:
    #making input prompt
    for i in range(len(UsedLetters)):
        UsedLettersStr += UsedLetters[i] 
    guess = input(blanks + " you've already guessed the letters \"" + UsedLettersStr + "\" " + "guess a character:")

    #emptying lists and variables
    blanksList = []
    correctDigitsThisRound = []
    correct = False
    dupelicate = False
    UsedLettersStr = ""
    count = 0

    #checking if more than one letters were guessed
    for i in range(len(guess)):
        count += 1
    if count != 1:
        print("please only guess one letter")
        noOfGuessesLeft -= 1
        print("Wrong", "\n", "You have", noOfGuessesLeft, "more guesses")

    else:
        #Checking if the current guess has been used before
        for i in range(len(UsedLetters)):
            if UsedLetters[i] == guess:
                dupelicate = True
                noOfGuessesLeft -= 1
                print("Wrong", "\n", "You have", noOfGuessesLeft, "more guesses")

        #stopping if the guess is a dupelicate
        if dupelicate == True:
            print("you've guessed that already, guess something else")

        #Executing guessing if the guess is not a dupelicate
        else:
            #converting blanks into a list
            for i in range(length):
                blanksList += blanks[i]
                correctDigitsThisRound += "_"
            
            #checking for correct guesses
            for i in range(length):
                if guess == answer[i]:
                    correctDigitsThisRound[i] = "1"
                    correct = True
                else:
                    correctDigitsThisRound[i] = "0"

            #putting the correct guesses into the list
            for i in range(len(correctDigitsThisRound)):
                if correctDigitsThisRound[i] == "1":
                    blanksList[i] = guess

            #Changing the list back into a string
            blanks = ""
            for i in range(len(blanksList)):
                blanks += blanksList[i]

            #correct and incorrect responses
            if correct == False:
                noOfGuessesLeft -= 1
                print("Wrong", "\n", "You have", noOfGuessesLeft, "more guesses")
        UsedLetters += guess + " "

#game end responses
if blanks == answer:
    print(answer + "You won")
else:
    print(answer, "You lost")
    
        