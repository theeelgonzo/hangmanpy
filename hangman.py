count = 6
alreadyGuessed = []

def playGame(secretWord):
    secretWord = list(secretWord)
    encWord = list(len(secretWord) * '*') 
    # print(encWord)
    while (count > 0) & (encWord != secretWord):
        #print('The game is afoot!')
        print(str(encWord))
        nextGuess = input('Guess a letter... \n')
        for char in range(len(secretWord)):
            if nextGuess == secretWord[char]:
                encWord[char] = secretWord[char]
                continue
            else:
                break

    if (count > 0 ) & (encWord == secretWord):
        print('You win!')
        
    else:
        print('You lose!')
    





playGame('poodle')
