import random

def random_word():
    with open('SOWPODS.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) != 0:
            random_line = random.randint(0,len(lines)-1)
            word = str(lines[random_line])
            return word

def main():
    word = str(random_word()).upper()
    guessed = (len(word)-1) * '_' 
    letter_guessed = []
    attempts = 0
    
    print ('Welcome to Hangman')
    print (guessed)
    letter = str(input('Guess a letter: ')).upper()
    
    word = list(word)
    guessed = list(guessed)
    
    while attempts <= 10:
        if letter in letter_guessed:
            print ('Letter already asked')
            print (''.join(guessed))
            letter = str(input('Guess a letter: ')).upper()
        elif letter in word:
            letter_guessed.append(letter)
            for i in range(0, len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print (''.join(guessed))
            if '_' not in guessed:
                break;
            letter = str(input('Guess a letter: ')).upper()
        else:
            print ('Incorrect')
            letter_guessed.append(letter)
            print (''.join(guessed))
            attempts += 1
            letter = str(input('Guess a letter: ')).upper()
    if attempts > 10:
        print ('Failed')
    elif '_' not in guessed:
        print ('Congratulations!')
main()