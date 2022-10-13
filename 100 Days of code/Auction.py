from replit import clear


def add_participant():
    name = input('What is your name?\n')
    bid = int(input('What is your bid?\n'))
    return name, bid


def main():
    participants = {}
    name, bid = add_participant()
    participants[name] = bid
    high_price_name = name
    bidding_finished = False
    while not bidding_finished:
        decision = input('Are there any bidders? Type "yes" or "no" \n')
        if decision == 'yes':
            clear()
            name, bid = add_participant()
            participants[name] = bid
            if participants[high_price_name] < bid:
                high_price_name = name
        else:
            print(f'The winner is {high_price_name} with a bid of ${participants[high_price_name]}')
            bidding_finished = True


if __name__ == '__main__':
    main()
