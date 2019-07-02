# language_study
A set of Python scripts for handling lists of words.

These were created to automatically handle the lists of words made  during studying. Namely, words whose definitions were looked up.
The file dictionary_sample.txt is a sample of the proper formatting. One word per line.


An explanation of the files:

checker.py: A Python script that checks an inputted word against the word list, and prints out whether or not the inputted word is already in the list. It also keeps track of the checked word, and if it was in the list or not, in checked.txt.

dictionary.txt: A blank file for word lists.

dictionary_inserter.py: A Python script that adds a word to the end of dictionary.txt, for the option to add words manually one at a time.

dictionary_sample.txt: A example for proper formatting. One word per line.

duplicate_words.py: A Python script that takes the word list, only keeps the duplicates, and outputs it to duplicates.txt.

random_word.py: A Python script that prints out a random word from the list of unique words.

unique_words.py: A Python script that takes the word list, removes the duplicates, and outputs it to unique.txt.

vocabulary.py: A Python script that converts dictionary.txt for use in the other scripts.
