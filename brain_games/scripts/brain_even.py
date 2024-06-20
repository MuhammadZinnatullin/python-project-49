import random
import prompt

def even():
    i = 1
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    while i < 4:
        random_number = random.randint(1, 20)
        ansver = prompt.string(f'Question: {random_number} \nYour answer: ')
        if random_number % 2 == 0:
            if ansver == 'yes':
                print('Correct!')
            else: 
                print(f'\"{ansver}\" is wrong answer ;(. Correct answer was \"yes\".')
                print(f'Let\"s try again, {name}!')
                return
        else:
            if ansver == 'no':
                print('Correct!')
            else: 
                print(f'\"{ansver}\" is wrong answer ;(. Correct answer was \"no\".')
                print(f'Let\"s try again, {name}!')
                return
        i += 1
    print(f'Congratulations, {name}!')


def main():
    even()


if __name__ == '__main__':
    main()
