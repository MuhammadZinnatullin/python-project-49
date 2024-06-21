import random
import prompt
from brain_games.my_mod import simile


def gcd():
    i = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    while i < 4:
        a = random.randint(40, 80)
        b = random.randint(2, 20)
        ansver = prompt.integer(f'Question: {a} {b} \nYour answer: ')

        while b != 0:           # алгоритм Эвклида, в а - НОД
            a, b = b, a % b
        result = a

        simile(name, ansver, result)

        i += 1
    print(f'Congratulations, {name}!')


def main():
    gcd()


if __name__ == '__main__':
    main()
