NEW_LINE = '\n'


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1 - n2


def multiple(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiple,
    '/': divide
}


def next_operation(previous_answer):
    operation_symbol = input('Pick another operation: ')
    num = float(input('What`s the next number?: '))
    result = operations[operation_symbol](previous_answer, num)
    print(f'{previous_answer} {operation_symbol} {num} = {result}')
    return result


def main():
    should_continue = True
    number = float(input('What`s the first number?: '))
    print(f'{NEW_LINE.join([oper for oper in operations])}')
    while should_continue:
        operation_symbol = input('Pick an operation: ')
        second_number = float(input('What`s the next number?: '))
        result = operations[operation_symbol](number, second_number)
        print(f'{number} {operation_symbol} {second_number} = {result}')
        condition = input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation: ")
        if condition == 'n':
            should_continue = False
        elif condition == 'y':
            number = result
        else:
            raise('Incorrect symbol')
    print(f'Your answer is {result}')


if __name__ == '__main__':
    main()


