# aux function that checks if word matches info
# ex:
# word="deer", info:"-ee-"
def wordMatch(word, info):
	if len(word) != len(info):
		return False
	for i in range(len(info)):
		if info[i] != "-":
			if info[i] != word[i]:
				return False
	return True

# creates dict as a dictionary of english words
doc = open("/usr/share/dict/words", "r")
dict = {}
for line in doc: # fill dictionary
    dict[line.strip()] = True

# prompts user
info1 = raw_input("first word: ")
info2 = raw_input("second word: ")

# basic mistake check
if len(info1) != len(info2):
	print("length mismatch")

# meat of the code:
for word1 in dict:
	if wordMatch(word1, info1): # found word1 that fits info1
		# building word2 candidate from info 2
		word2 = ""
		for i in range(len(info2)):
			if info2[i] != "-":
				word2 = word2+info2[i]
			else:
				word2 = word2+word1[i]
		if (word2 in dict):
			# success!
			print("word 1: "+word1)
			print("word 2: "+word2)

