import sys


def simile(name, ansv, correct_ans):
    if ansv == correct_ans:
        print('Correct!')
    else:
        mess = '\" is wrong answer ;(. Correct answer was \"'
        print(f'\"{ansv}{mess}{correct_ans}\".')
        print(f'Let\"s try again, {name}!')
        sys.exit()


def main():
    simile()


if __name__ == '__main__':
    main()
