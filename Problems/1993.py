string = input().lower()
array = string.split(", ")
newWord = ["", "", ""]
result = ""
for wordArray in array:
    justWord = ""
    while wordArray != "":
        word = ""
        if wordArray[0] in ("{", "(", "["):
            if wordArray[0] == "{":
                while wordArray[0] != "}":
                    word += wordArray[0]
                    wordArray = wordArray[1:]
                newWord[0] = word[1:]
                wordArray = wordArray[1:]
            elif wordArray[0] == "(":
                while wordArray[0] != ")":
                    word += wordArray[0]
                    wordArray = wordArray[1:]
                newWord[1] = word[1:]
                wordArray = wordArray[1:]
            elif wordArray[0] == "[":
                while wordArray[0] != "]":
                    word += wordArray[0]
                    wordArray = wordArray[1:]
                newWord[2] = word[1:]
                wordArray = wordArray[1:]
        else:
            while wordArray[0] != " ":
                justWord += wordArray[0]
                wordArray = wordArray[1:]
            wordArray = wordArray[1:]
    if justWord != "":
        result += justWord + " " + newWord[0] + " " + newWord[1] + " " + newWord[2] + "  "
    else:
        result += justWord + newWord[0] + " " + newWord[1] + " " + newWord[2] + ", "
print(result[0].upper()+result[1:-2])
