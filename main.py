import random
import os

max_attempts = 11
words_directory = 'francais.txt'

attempts = 0
attempted_letters = []

def getWord():
    words = []    
    with open(words_directory, 'r') as file:
        for word in file:
            words.append(word.rstrip("\n"))
    return words[random.randint(0, len(words))]

def find_char_indices(s, char):
    return [i for i, c in enumerate(s) if c == char]

def replace_char_at_index(string, index, new_char):
    string_list = list(string)
    string_list[index] = new_char
    return ''.join(string_list)

def menu(word):
    os.system('cls')
    print('')
    match attempts:
        case 0:
            print(f'                     Attempts: {attempts}/{max_attempts}')
            print(f'                     Attempted Letters: ')
            print('                      ', end='')
            print(*attempted_letters, sep=", ")
            print('                      ')
            print('                      ', end='')
            print(*word)
            print('                      ')
        case 1:
            print(f'                     Attempts: {attempts}/{max_attempts}')
            print(f'                     Attempted Letters: ')
            print('                      ', end='')
            print(*attempted_letters, sep=", ")
            print('                      ')
            print('                      ', end='')
            print(*word)
            print('                      ')
            print('  ────────────        ')
        case 2:
            print(f'  |                  Attempts: {attempts}/{max_attempts}')
            print(f'  |                  Attempted Letters: ')
            print('  |                   ', end='')
            print(*attempted_letters, sep=", ")
            print('  |                   ')
            print('  |                   ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 3:
            print(f'  ┌──────────        Attempts: {attempts}/{max_attempts}')
            print(f'  |                  Attempted Letters: ')
            print('  |                   ', end='')
            print(*attempted_letters, sep=", ")
            print('  |                   ')
            print('  |                   ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 4:
            print(f'  ┌──────────        Attempts: {attempts}/{max_attempts}')
            print(f'  |/                 Attempted Letters: ')
            print('  |                   ', end='')
            print(*attempted_letters, sep=", ")
            print('  |                   ')
            print('  |                   ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 5:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |                   ', end='')
            print(*attempted_letters, sep=", ")
            print('  |                   ')
            print('  |                   ', end='')
            print(*word)
            print('  |')
            print('  └───────────        ')
        case 6:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |         O         ', end='')
            print(*attempted_letters, sep=", ")
            print('  |                   ')
            print('  |                   ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 7:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |         O         ', end='')
            print(*attempted_letters, sep=", ")
            print('  |         |         ')
            print('  |         |         ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 8:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |         O         ', end='')
            print(*attempted_letters, sep=", ")
            print('  |         |         ')
            print('  |        /|         ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 9:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |         O         ', end='')
            print(*attempted_letters, sep=", ")
            print('  |         |         ')
            print('  |        /|\\       ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 10:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |         O         ', end='')
            print(*attempted_letters, sep=", ")
            print('  |        /|         ')
            print('  |        /|\\       ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
        case 11:
            print(f'  ┌─────────┐        Attempts: {attempts}/{max_attempts}')
            print(f'  |/        |        Attempted Letters: ')
            print('  |         O         ', end='')
            print(*attempted_letters, sep=", ")
            print('  |        /|\\       ')
            print('  |        /|\\       ', end='')
            print(*word)
            print('  |                   ')
            print('  └───────────        ')
    print()
    
def main():
    global attempts
    global attempted_letters
    
    word = getWord()
    hiddenWord = ""
    
    for _ in word:
        hiddenWord += '_'
    
    while True:        
        menu(hiddenWord)
        
        if word == hiddenWord or attempts >= max_attempts:
            print(f'The word was {word}')
            break
        
        letter = input('Guess a letter: ').lower()
        if len(letter) == 1 and letter.upper() not in attempted_letters:            
            letterIndexes = find_char_indices(word, letter)
            attempted_letters.append(letter.upper())
            
            if len(letterIndexes) > 0:
                for letterIndex in letterIndexes:
                    hiddenWord = replace_char_at_index(hiddenWord, letterIndex, letter)
            else:
                attempts += 1
main()