import random
import prompt
from brain_games.my_mod import simile


def progression():
    i = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    while i < 4:
        one = random.randint(0, 30)             # первый элемент
        step = random.randint(1, 15)
        quantity = random.randint(5, 15)        # длинна последовательности
        rnd_ind = random.randint(0, quantity - 1)  # индекс пропущенного элемента
        str_question = ''                       # строка вывода прогрессии
        for j in range(quantity):
            if j == rnd_ind:
                x = one + j * step
                str_question = str_question + '..' + ' '
            else:
                str_question = str_question + str(one + j * step) + ' '

        ansver = prompt.integer(f'Question: {str_question} \nYour answer: ')

        simile(name, ansver, x)

        i += 1
    print(f'Congratulations, {name}!')


def main():
    progression()


if __name__ == '__main__':
    main()
