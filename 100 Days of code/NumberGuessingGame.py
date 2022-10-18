import random

EASY = 10
HARD = 5


def get_number():
    num = int(input('Make a guess: '))
    return num


def check_answer(number, answer):
    if answer > number:
        print('Too low')
    elif answer < number:
        print('Too high')
    else:
        print('You win')
        return True
    return False


def main():
    win = False
    print('Welcome to the Number Guessing Game!\n I`m thinking of a number between 1 and 100.')
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    cnt = EASY if level == 'easy' else HARD
    answer = random.randint(1, 100)
    while cnt > 0:
        print(f'You have {cnt} attempts to remaining to guess the number.')
        new_number = get_number()
        win = check_answer(new_number, answer)
        if win:
            break
        cnt -= 1
    if not win:
        print('You`ve run out of guess, you lose.')


if __name__ == '__main__':
    main()
