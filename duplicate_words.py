from vocabulary import vocab
file = open("duplicates.txt", "w")

uniqueList = []
duplicateList = []
duplicatesTemp = []

for elem in vocab:
    if elem not in uniqueList:
        uniqueList.append(elem)
    else:
        duplicatesTemp.append(elem)

for elem in duplicatesTemp:
    if elem not in duplicateList:
        duplicateList.append(elem)
#    else:
#        elem = elem + " +1"

with open("duplicates.txt", "a") as the_file:
    for elem in duplicateList:
        the_file.write(elem + "\n")

file.close()

# print(duplicateList)
