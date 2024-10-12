answer = "frbjhbdhbddcd"  #set the answer as anything you like
noOfGuessesLeft = 10
correct = False
blanks = ""
length = len(answer)
for i in range(length):
    blanks += "_"
finalDigit = 0
listOfCorrectDigits = []




def makeBlanks():
    global listOfCorrectDigits
    for i in range(length):
        if guess == answer[i]:
            listOfCorrectDigits += "i"
    









    blanksList = []
    for i in range(length):
        blanksList += blanks[i]
    blanksList[] = ""
    blanks = ""
    for i in range(length):
        blanks += blanksList[i]
    print(blanksList)
    print(blanks)







while blanks != answer and noOfGuessesLeft > 0:
    guess = input(blanks + "guess a character:")
    makeBlanks()
    if blanks == answer:
        print(answer + "You won")
    else:
        print(answer, "You lost")



text = "hi I am almost insane"
textList = []
for i in range(len(text)):
    textList += text[i]
textList[6] = "d"
text = ""
for i in range(len(textList)):
    text += textList[i]
print(textList)
print(text)