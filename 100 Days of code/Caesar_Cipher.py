alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dict = {letter: num for num, letter in enumerate(alphabet)}
alphabet_dict_reverse = {num: letter for num, letter in enumerate(alphabet)}

direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    enc = []
    for let in text:
        num = alphabet_dict.get(let)
        enc.append(alphabet_dict_reverse.get(shift + num))
    return ''.join(enc)


def decode(text, shift):
    dec = []
    for let in text:
        num = alphabet_dict.get(let)
        dec.append(alphabet_dict_reverse.get(num - shift))
    return ''.join(dec)


def main():
    if direction == 'encode':
        print(encrypt(text, shift))
    elif direction == 'decode':
        print(decode(text, shift))
    else:
        print('I don`t know this direction')


if __name__ == '__main__':
    main()
