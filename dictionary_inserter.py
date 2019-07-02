print("Input word add to index")
print("Input 'quit' or 'q' to quit")

while True:
    indexed = input("Please input word: ")

    if indexed.lower() == "q" or indexed.lower() == "quit":
        break
    else:
        with open("index.txt", "a") as the_file:
            the_file.write(indexed + "\n")
        print(indexed + " added to index")
