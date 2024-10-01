answer = "frbjhbdhbddcd"  #set the answer as anything you like
noOfGuessesLeft = 10
blanks = ""
digitsRight = 0
length = len(answer)
for i in range(length):
    blanks = "f_____________"
correctDigitsThisRound = []
blanksList = []

guess = input(blanks + "guess a character:")

for i in range(length):
    blanksList += blanks[i]
    print(correctDigitsThisRound)

for i in range(length):
    if guess == answer[i]:
        correctDigitsThisRound += "Y"
    else:
        correctDigitsThisRound += "N"
    print(correctDigitsThisRound)







blanksList = []
for i in range(length):
    blanksList += blanks[i]
for i in range(len(correctDigitsThisRound)):
    if correctDigitsThisRound[i] == "Y":
        blanksList[i] = guess
blanks = ""
for i in range(len(blanksList)):
    blanks += blanksList[i]
print(blanksList)
print(blanks)


correctDigitsThisRound = []

print("blanks:", blanks)

