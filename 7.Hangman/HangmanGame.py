import random

python_words = [
    "python", "variable", "function", "loop", "for", "while", "if", "else", "elif", "true",
    "false", "none", "list", "tuple", "dictionary", "set", "string", "integer", "float", "boolean",
    "class", "object", "method", "attribute", "self", "init", "inheritance", "encapsulation", "polymorphism", "abstraction",
    "lambda", "map", "filter", "reduce", "comprehension", "generator", "iterator", "yield", "break", "continue",
    "pass", "def", "return", "import", "from", "as", "with", "try", "except", "finally",
    "raise", "assert", "global", "nonlocal", "del", "is", "in", "not", "and", "or",
    "module", "package", "pip", "virtualenv", "venv", "interpreter", "compiler", "script", "syntax", "error",
    "exception", "traceback", "debug", "comment", "indentation", "pep8", "format", "fstring", "input", "print",
    "open", "read", "write", "file", "os", "sys", "math", "random", "datetime", "json",
    "re", "threading", "multiprocessing", "async", "await", "sqlite3", "flask", "django", "pandas", "numpy"
]
six =   '''
     +---+
     |   |
         |
         |
         |
         |
    ========='''

five =   '''
     +---+
     |   |
     O   |
         |
         |
         |
    ========='''

four = '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========='''

three = '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========='''

two =  '''
     +---+
     |   |
     O   |
    /|\  |
     |   |
         |
    ========='''

one =  '''
     +---+
     |   |
     O   |
    /|\  |
    /|   |
         |
    ========='''

zero =  '''
     +---+
     |   |
     O   |
    /|\  |
    /|\   |
         |
    ========='''
image = [zero,one,two,three,four,five,six]

hangman = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/          '''
print("Welcome to HANGMAN!!")
print(hangman)

word = random.choice(python_words)
length = len(word)

print("Words to guess - ")
while length>0:
    print("_",end="")
    length-=1

length = len(word)
guessed = 0
lives = 6
ans = ""
for i in range(length):
   ans += "_"

left_word = word
while lives>0:
    letter = input("\nGuess a letter - ").lower()

    if letter in left_word:
        print("Your guess is CORRECT")
        ind = word.index(letter)
        indL = left_word.index(letter)
        temp = ""

        for i in range(length):
            if word[i]==letter:
                temp += letter
                guessed += 1
            else:
                temp += ans[i]
        ans = temp
        print(ans)


        left_word = left_word.replace(letter,"")
        if guessed == length:
            break

    elif word.count(letter)!=0 and word.count(letter) == ans.count(letter):
        print("Already guessed")
        lives -= 1

    else:
        print(f"You guessed it wrong, {letter} does not belong to the word")
        print(ans)
        lives-=1
    print(image[lives])
    print(f"********************** {lives}/6 lives left **********************")



if guessed == length:
    print("\nYOU WON")
else:
    print(f"\nThe word was {word}")
    print("YOU LOSE")
