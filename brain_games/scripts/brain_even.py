import random
import prompt
from brain_games.my_mod import simile


def even():
    i = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    while i < 4:
        random_number = random.randint(1, 50)
        ansver = prompt.string(f'Question: {random_number} \nYour answer: ')
        if random_number % 2 == 0:
            simile(name, ansver, 'yes')
        else:
            simile(name, ansver, 'no')
        i += 1
    print(f'Congratulations, {name}!')


def main():
    even()


if __name__ == '__main__':
    main()
