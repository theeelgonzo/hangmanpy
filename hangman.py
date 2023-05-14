def playGame(secretWord):
    secretWord = list(secretWord)
    encWord = list(len(secretWord) * '*')
    count = 0
    alreadyGuessed = []
    
    print(secretWord)
    while (count < 6):
        print(encWord)
        print(f'You have {6 - count} guesses remaining')
        nextGuess = input('Guess a letter...')
        if nextGuess in secretWord:
            for i,v in enumerate(secretWord):
                if secretWord[i] == nextGuess:
                    v = secretWord[i]
                    encWord[i] = v
            return encWord
            alreadyGuessed.append(nextGuess)
            continue
        elif nextGuess not in secretWord:
            print(f'{nextGuess} is incorrect, try again!')
            guesses -= 1
            alreadyGuessed.append(nextGuess)
        else:
            print(f'You have already tried {nextGuess}, try something else!')
        
    





playGame('poodle')
