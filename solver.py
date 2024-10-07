import json

wordDict = {}

# open wordlist
with open('words_dictionary.json') as json_file:
	wordDict = json.load(json_file)

print("\nWelcome to the NYT Spelling Bee solver! \n\nNote that the puzzle creators at the NYT remove words that they think are too obscure, so some words generated by this program may not be considered solutions to the puzzle.\n\n")

# gather input, could be improved with input validation for user facing application
print("Please enter the required letter (the yellow letter in the middle)")
requiredLetter = input().lower()

print("Please enter the rest of the letters")
okLetters = input().lower() + requiredLetter

# a word in spelling bee must be longer than 4 characters,
# include the required letter, and be constructed only of the
# given letters
minLen = 4

# test word for spelling bee criteria
for testWord in wordDict:
	if requiredLetter in testWord and len(testWord) >= minLen:
		okWord = True
		for letter in testWord:
			if letter not in okLetters:
				okWord = False
		if okWord: 
			print(testWord)