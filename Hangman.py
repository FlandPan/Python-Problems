import random

#return random word
def random_word():
    #uses http://norvig.com/ngrams/sowpods.txt as database for words to choose from
    with open('sowpods.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) != 0:
            random_line = random.randint(0,len(lines)-1)
            word = str(lines[random_line])
            return word

def main():
    word = str(random_word()).upper()
    guessed = (len(word)-1) * '_' 
    letter_guessed = []
    attempts = 1
    max_attempts = 10

    print ('Welcome to Hangman')
    print (guessed)
    
    word = list(word)
    guessed = list(guessed)
    
    while attempts < max_attempts:
        letter = str(input('Guess a letter: ')).upper()
        if letter in letter_guessed:
            print ('Letter already asked')
            print (''.join(guessed))
        elif letter in word:
            letter_guessed.append(letter)
            for i in range(0, len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print (''.join(guessed))
            if '_' not in guessed:
                break;
        else:
            print ('Incorrect')
            letter_guessed.append(letter)
            print (''.join(guessed))
            attempts += 1
            print ("Attempts left: ", 10-attempts)
    if attempts >= max_attempts:
        print ('Failed')
        print (''.join(word))
    elif '_' not in guessed:
        print ('Congratulations!')
main()