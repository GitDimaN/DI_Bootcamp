hangman = [[' ','o',' '],["/","|","\\"],["/"," ","\\"]]
progress_hangman = [[' ',' ',' '],[" "," "," "],[" "," "," "]]

row_count = len(hangman)
col_count = len(hangman[0])
hangman_size = 6
hangman_index = 6
fail_vector = [2,4,5,6,7,9]

import string
alphabet = list(string.ascii_lowercase)
alphabet.append(' ')
print(*alphabet, sep=' ')
alphabet_remain = list(alphabet)
alphabet_remain.append(' ')

import random

def gen_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    return random.choice(wordslist)

word = list(gen_word())
word_len = len(word)
word_hidden = list("*" * len(word))
word_remain = word.copy()
# print(*word, sep='')
print(*word_hidden, sep='')
# print(*word_remain, sep='')

def display_figure(figure):
    for i in figure:
        print(*i, sep="")

# def update_hangman():
#     for i in range(row_count):
#         for j in range(col_count):
#             progress_hangman[i][j] = hangman[i][j]
#             # display_figure(progress_hangman)

def update_hangman(fail_cell):
    global progress_hangman, hangman_index
    r = fail_cell // col_count
    c = fail_cell % col_count

    if c == 0:
        c = col_count # for last column in that row, correct index for range that excludes last
    else:
        r += 1 # for correct index of this row

    #progress_hangman[r][c] = hangman[r][c]

    for i in range(r):
        for j in range(c):
             progress_hangman[i][j] = hangman[i][j]
#             # display_figure(progress_hangman)


# update_hangman()

def player_input():
    global alphabet_remain
    letter_guess = input("Please choose a letter incl. space: ").lower()

    while letter_guess not in alphabet_remain:
        if letter_guess not in alphabet:
            letter_guess = input("This is not a letter, please choose a letter from the alphabet incl. space: ").lower()
        else:
            letter_guess = input("You've already used this letter, please choose one from the remaining available letters: ").lower()        

    alphabet_remain = [l for l in alphabet_remain if l!=letter_guess]

    return letter_guess

def open_letter(letter):
    global word_hidden,word_remain
    # go through
    # for i in range(word_len):
    #    if word[i] == letter:
    #        word_hidden[i] = letter
    indices = [i for i,l in enumerate(word) if l == letter]
    word_hidden = [letter if i in indices else val for i,val in enumerate(word_hidden)]
    word_remain = [l for l in word_remain if l != letter]
    print(*word_hidden,sep='')

def play():
    global word_hidden, word_remain, alphabet_remain, progress_hangman
    # reset failed attempts:
    fail_count = 0

    # play until hangman full (max attempts)
    while fail_count < hangman_size:
        guess = player_input()
        if guess in word_remain:
            print(f"There is such a letter in the word. Please open letter {guess}!")
            open_letter(guess)
            if "*" not in word_hidden:
                print("You've won! The word is: ", end='')
                print(*word_hidden,sep='')
                return
        else:
            fail_cell = fail_vector[fail_count]
            update_hangman(fail_cell)
            display_figure(progress_hangman)
            fail_count += 1
    print("You have lost. The correct word is :", end='')
    print(*word, sep='')
    
play()

