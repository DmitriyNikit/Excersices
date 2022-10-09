import sys
from classes import Qty, Category, ClientIsPremium, FoodPurchases
from logger import logs


def main():
    logs.debug('Start of our program')
    if len(sys.argv) == 2:
        check_date = sys.argv[1]
        Qty(check_date).checker()
        Category(check_date).checker()
        ClientIsPremium(check_date).checker()
        FoodPurchases(check_date).checker()
    else:
        logs.error('If you want starting check, use this template - "python3 *.py "2022-01-01""')


if __name__ == '__main__':
    main()
