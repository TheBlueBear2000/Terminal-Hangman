'''
Question 1: Create a function called is_letter_in_word which take in a letter and a word, and returns True if the letter is in the word
'''

def is_letter_in_word(word, letter):
  if letter in word:
    return True
  else:
    return False
'''
Question 2: Create a function called print_word which takes in a word and an array of letters, and returns an array of length of the word with _ if the letter is not in the array, and the actual letter if it is. For example, if the "found letters" are ["o", "u"] and the word is "found", the output should be the array ["_", "o", "u", "_", "_"]. You can use the function find which returns the index of a letter in a word. For example, "word".find("o") will return 1.
Also, if you do ["_"] * 3, you will get ["_", "_", "_"]
'''

def print_word(word, letters):
    out = []
    
    for letter in list(word):
        if letter == " ":
            out.append(" ")
        elif letter in letters:
            out.append(letter)
        else:
            out.append("_")
    
    return out

'''
Question 3: Use the above functions to have a small hangman game. Choose a word and ask the user to input a letter. Check if the letter is in the word (you can use the previously defined functions), and if it is keep track of it and print the word with the found letters. Keep going until the user finds all of the letters.
'''

attemptStages = [
    "                   \n"+
    "                   \n"+
    "                   \n"+
    "                   \n"+
    "                   \n"+
    " ___________       \n",
    
    "                  \n"+
    " |                 \n"+
    " |                 \n"+
    " |                 \n"+
    " |                 \n"+
    " |__________       \n",
    
    "  _________        \n"+
    " |/                \n"+
    " |                 \n"+
    " |                 \n"+
    " |                 \n"+
    " |__________       \n",
    
    "  _________        \n"+
    " |/   |            \n"+
    " |    |            \n"+
    " |                 \n"+
    " |                 \n"+
    " |__________       \n",
    
    "  _________        \n"+
    " |/   |            \n"+
    " |    o            \n"+
    " |   /|\           \n"+
    " |   / \           \n"+
    " |__________       \n",
]



letters = []
word = "test word"
MAX_ATTEMPTS = 5
attempts = MAX_ATTEMPTS
won = False

while True:
    newletter = input("Please pick a letter:    ")
    if len(newletter) != 1:
        print("Please only choose 1 letter")
        continue
    elif newletter in letters:
        print("You have already tried that letter")
        continue
    
    letters.append(newletter)
    
    wordInList = print_word(word, letters)
    
    print("\n" + attemptStages[min(MAX_ATTEMPTS - attempts, len(attemptStages)-1)] + "\n")
    
    
    toPrint = ""
    for letter in wordInList:
        toPrint += letter 
    print(f"Progress: {toPrint}")
    if toPrint == word:
        won = True
    
    toPrint = ""
    for letter in letters:
        toPrint += letter + ", "
    toPrint = toPrint[:-2]
    print(f"Used letters: {toPrint}")
    
    if not is_letter_in_word(word, newletter):
        attempts -= 1
    
    if won:
        print(f"\nYou won! The word was: {word}")
    elif attempts < 0:
        print(f"\nYou ran out of attempts, the word was: {word}")
    else:
        currentAttempt = MAX_ATTEMPTS - attempts
        print(f"Failed attempts {currentAttempt}/{MAX_ATTEMPTS}\n")
    
    

'''
Question 4: Try your game with the word "choice". Does it work correctly? What happens when you have a letter occurs more than once. Try to fix this.
'''

# It works perfectly did you ever doubt me

'''
Question 5: Make this work with compound words or sentences
'''
# Already did  