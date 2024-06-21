import random
import prompt
from brain_games.my_mod import simile


def calc():
    i = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    symbols = '+-*'
    while i < 4:
        a = random.randint(1, 40)
        b = random.randint(1, 20)
        symb_ind = random.randint(0, 2)
        qest = str(a) + ' ' + symbols[symb_ind] + ' ' + str(b)
        ansver = prompt.integer(f'Question: {qest} \nYour answer: ')

        if symb_ind == 0:
            result = a + b
        elif symb_ind == 1:
            result = a - b
        elif symb_ind == 2:
            result = a * b
        else:
            print('symb error')
            return

        simile(name, ansver, result)

        i += 1
    print(f'Congratulations, {name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
