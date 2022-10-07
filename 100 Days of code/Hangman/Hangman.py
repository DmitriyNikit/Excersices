import random
import words
import arts

LIVES = 5

chosen = random.choice(words.word_list)
chosen_word = chosen[0]
word_length = len(chosen_word)
display = ['_'] * word_length
end_of_game = f'Word is "{chosen_word}". \nMeaning is {chosen[1]}. \nUsage - {chosen[2]}'

while LIVES > 0:
    print(display)
    guess = input('Guess a letter please: ').lower()
    if guess in chosen_word:
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
        if '_' not in display:
            print('You`re win. \n' + end_of_game)
            break
    else:
        LIVES -= 1
        if LIVES == 0:
            print(arts.ICONS[-1])
            print('You`re loose. \n' + end_of_game)
            break
        else:
            print(f'Sorry, we haven`t this letter in our word. You lives is {LIVES}')
            print(arts.ICONS[-LIVES])
