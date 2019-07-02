from vocabulary import vocab

print("Input word to check against dictionary")
print("Input 'quit' or 'q' to quit")

while True:
    checkedWord = input("Please input word: ")

    if checkedWord.lower() == "q" or checkedWord.lower() == "quit":
        break
    elif checkedWord in vocab:
        with open("checked.txt", "a") as the_file:
            the_file.write(checkedWord + " O\n")
        print("Word in dictionary")
    elif checkedWord not in vocab:
        with open("checked.txt", "a") as the_file:
            the_file.write(checkedWord + " X\n")
        print("Word not found.")
