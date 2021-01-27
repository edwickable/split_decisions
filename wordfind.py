def createEnglishWordsDict():
  doc = open("/usr/share/dict/words", "r")
  words = {}
  for line in doc:
    words[line.strip()] = True

  return words

def promptUserInput():
  shape1 = raw_input("first word: ")
  shape2 = raw_input("second word: ")

  if len(shape1) != len(shape2):
    print("length mismatch")

  return (shape1, shape2)

def runSearch(shape1, shape2, words):
  for word1 in words:
    if doesWordFitShape(word1, shape1):
      word2 = constructComplimentaryWord(word1, shape2)

      if (word2 in words):
        printSuccessMessage(word1, word2)

# ex:
# word="deer", shape:"-ee-"
def doesWordFitShape(word, shape):
  if len(word) != len(shape):
    return False

  for i in range(len(shape)):
    blank = shape[i] == "-"

    if not blank and shape[i] != word[i]:
      return False

  return True

def constructComplimentaryWord(word, shape):
  compliment = ""

  for i in range(len(shape)):
    if shape[i] == "-":
      compliment += word[i]
    else:
      compliment += shape[i]
	
  return compliment

def printSuccessMessage(word1, word2):
  print("word 1: " + word1)
  print("word 2: " + word2)
  print("-----")

words = createEnglishWordsDict()
shape1, shape2 = promptUserInput()

runSearch(shape1, shape2, words)
