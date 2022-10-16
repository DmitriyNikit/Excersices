import random
my_deck = []
dillers_deck = []


def get_random_card(card_list):
    index = random.randint(0, len(card_list) - 1)
    card = card_list[index]
    card_list[index], card_list[-1] = card_list[-1], card
    return card_list


def message(all=False):
    print(f'Your cards: {my_deck}, current score is {sum(my_deck)}')
    if all:
        print(f'Diler`s deck is {dillers_deck}, score is {sum(dillers_deck)}')
    else:
        print(f'Diler`s first card is {dillers_deck[0]}')


def start_game(cards):
    for _ in range(2):
        my_deck.append(get_random_card(cards).pop())
    for _ in range(2):
        dillers_deck.append(get_random_card(cards).pop())
    message()
    if sum(my_deck) == 21:
        return 0
    return cards


def my_game(cards):
    is_over = False
    while not is_over:
        if input(f'Type "y" to get another card, "n" to pass: ') == 'y':
            cards = get_random_card(cards)
            my_deck.append(cards.pop())
            if sum(my_deck) == 21 or sum(my_deck) > 21:
                is_over = True
            else:
                message()
        else:
            is_over = True
            print(f'Ok, your score is {sum(my_deck)}, lets see to dillers deck')


def diller_game(cards):
    while sum(dillers_deck) < 17:
        cards = get_random_card(cards)
        dillers_deck.append(cards.pop())


def result():
    message(True)
    if sum(my_deck) > 21:
        print('You`re lose')
    elif sum(dillers_deck) > 21:
        print('Diller has more then 21, you`re win.')
    elif sum(my_deck) == 21:
        print('You`re win with BlackJack')
    elif sum(dillers_deck) == 21:
        print('Diller win with BlackJack')
    elif sum(dillers_deck) == sum(my_deck):
        print('The same result')
    elif sum(my_deck) > sum(dillers_deck):
        print('You`re win')
    else:
        print('Dillers win')


def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if input('Do you want to play a game of BlackJack? Type "y" or "n" ') == 'y':
        cards = start_game(cards)
        if cards == 0:
            print('You`re win!')
        else:
            my_game(cards)
            diller_game(cards)
            result()
    else:
        print('Okey, we are waiting you later.')


if __name__ == '__main__':
    main()
