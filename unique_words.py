from vocabulary import vocab
file = open("unique.txt", "w")

uniqueList = []

for elem in vocab:
    if elem not in uniqueList:
        uniqueList.append(elem)

with open("unique.txt", "a") as the_file:
    for elem in uniqueList:
        the_file.write(elem + "\n")

file.close()

# print(uniqueList)
