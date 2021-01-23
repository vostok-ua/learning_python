import random
list_ = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(list_)
guess_word_set = set(guess_word)
guessed_word_hint = "-" * len(guess_word)
bad_letters = set()
letters = set()
tries = 8

print("H A N G M A N")
while True:
    answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == 'play':
        while tries > 0 and guess_word_set != letters:
            print()
            guessed_word_hint = ''
            for ch in guess_word:
                if ch in letters:
                    guessed_word_hint += ch
                else:
                    guessed_word_hint += "-"
            print(guessed_word_hint)
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter")
            elif letter in letters or letter in bad_letters:
                print("You've already guessed this letter")
            elif letter not in ('a', 'b', 'c', 'd', 'e', 'f', 'g',
                                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                'o', 'p', 'q', 'r', 's',
                                't', 'u', 'v', 'w', 'x', 'y', 'z'):
                print('Please enter a lowercase English letter')
            elif letter not in guess_word_set:
                print("That letter doesn't appear in the word")
                tries -= 1
                bad_letters.add(letter)
            else:
                letters.add(letter)

        if guess_word_set == letters:
            print(f'You guessed the word {guess_word}!')
            print('You survived!')
            print()
        else:
            print('You lost!')
            print()
    elif answer == 'exit':
        break
