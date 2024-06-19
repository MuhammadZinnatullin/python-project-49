#!/usr/bin/env python3
from brain_games.cli import welcome_user


def greet(who):
    print(who)


def main():
    greet('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
