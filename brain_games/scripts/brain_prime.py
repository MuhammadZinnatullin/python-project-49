import random
import prompt
from brain_games.my_mod import simile


def prime():
    i = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    while i < 4:
        random_number = random.randint(2, 50)
        ansver = prompt.string(f'Question: {random_number} \nYour answer: ')
        flag = 1
        for j in range(2, random_number):           # если есть
            print(random_number % j, ' ', j)
            if random_number % j == 0:
                flag = 0
                break

        if flag:
            simile(name, ansver, 'yes')
        else:
            simile(name, ansver, 'no')
        i += 1
    print(f'Congratulations, {name}!')


def main():
    prime()


if __name__ == '__main__':
    main()
