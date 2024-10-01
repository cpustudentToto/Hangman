answer = "frbjhbdhbddcd"  #set the answer as anything you like
noOfGuessesLeft = 10
blanks = ""
digitsRight = 0
length = len(answer)
for i in range(length):
    blanks = "_r____________"
finalDigit = 0
slotedLetters = []
lettersInBlanks = 0


#initialization of counting how many digits were right
for i in range(length):
    if blanks[i] != "_":
        digitsRight += 1

#begining of guessing
guess = input(blanks + "guess a character:")
if guess in blanks:
    noOfGuessesLeft -= 1
    print("You guessed that before, you have", noOfGuessesLeft, "left")
else:


    #detection of if and where a correctly guessed letter is
    lettersInBlanks = 0
    newSlots = []
    finalDigit = -1
    digitsRightNow = digitsRight
    for i in range(length):
        if blanks[i] != "_":
            lettersInBlanks += 1
            newSlots += str(i)
    for i in range(length - 1, -1, -1):
        if blanks[i] != "_":
            newSlots += str(i)
            finalDigit = i
            slotedLetters[finalDigit] = {newSlots[newSlots[lettersInBlanks]]: blanks[i]}
            lettersInBlanks += 1
        elif answer[i] == guess:
            newSlots += str(i)
            finalDigit = i
            slotedLetters[finalDigit] += {newSlots[i]: blanks[i]}
            lettersInBlanks += 1
            digitsRightNow = digitsRightNow + 1
    print("slotedLetters:", slotedLetters)
    print("newSlots:", newSlots)
    print("finalDigit:", finalDigit)
    print("digitsRight:", digitsRight)
    print("digitsRightNow:", digitsRightNow)




    print("blanks:", blanks)

