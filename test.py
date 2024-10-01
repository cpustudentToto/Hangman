name = input("pls enter your name: ")
print("Hello,", name, "Time to play hangman.")


answer = "frbjhbdhbddcd"  #set the answer as anything you like
noOfGuessesLeft = 10
blanks = ""
length = len(answer)
for i in range(length):
    blanks += "_"
finalDigit = 0


def makeBlanks():
    global blanks, finalDigit, answer, length
    newSlots = []
    finalDigit = -1
    for i in range(length):
        if blanks[i] != "_" or answer[i] == guess:
            newSlots += str(i)
            finalDigit = i

    blanks = ""
    
    if finalDigit != -1:
        for i in range(int(newSlots[0]) - 1):
           blanks += "_"
        for i in range(len(newSlots)):
            for a in range(int(newSlots[i - 1]) - 1, int(newSlots[i])):
                blanks += "_"
        blanks += answer[int(newSlots[i])]
        for i in range(length - finalDigit):
           blanks += "_"
    else:
        noOfGuessesLeft -= 1
        print("Wrong" + "\n" + "You have", noOfGuessesLeft, "more guesses")






while blanks != answer and noOfGuessesLeft > 0:
    guess = input(blanks + "guess a character:")
    makeBlanks()
if blanks == answer:
    print(answer + "You won")
else:
    print(answer, "You lost")
    
        