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