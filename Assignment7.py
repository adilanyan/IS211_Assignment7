#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


class Die(object):
    def __init__(self):
        self.die = 0

    def roll(self):
        self.die = random.randint(1, 6)
        return self.die


class Player(object):
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.total_score = 0
        self.turns_score = 0


class Game(object):
    def __init__(self, first_player, second_player):
        self.first_player = Player(first_player)
        self.second_player = Player(second_player)
        self.die = Die()
        self.turn(self.first_player)

    def turn(self, user):
        user.turn = 1
        print('{} turn'.format(user.name))
        while user.turn == 1 and user.total_score < 100:
            r = self.die.roll()
            print('\nyou rolled a {}\n'.format(r))
            if r == 1:
                user.turns_score = 0
                print('you rolled a 1, next player.\n'.format(
                    user.name, user.total_score))
                print('-' * 60, '\n')
                self.next_player()
            else:
                user.turns_score += r
                print('your total this turn is {}\n'.format(user.turns_score))
                self.player_answer(user)
        print('{} is the winner. His score is {}!'.format(
            user.name, user.total_score))

    def player_answer(self, user):
        answer = input('roll again? r = roll h = hold ').lower()
        if answer == 'h':
            user.total_score += user.turns_score
            print('your turn is now over.')
            if user.total_score >= 100:
                print('{} wins.'.format(user.name, user.total_score))
            else:
                user.turns_score = 0
                print('{} total score is {}.\n\n'.format(
                    user.name, user.total_score))
                print('-' * 60, '\n')
                self.next_player()
        elif answer == 'r':
            self.turn(user)
        else:
            print('Pick correct option, r = roll h = hold ')
            self.player_answer(user)

    def next_player(self):
        if self.first_player.turn == 1:
            self.first_player.turn = 0
            self.turn(self.second_player)
        else:
            self.second_player.turn_status = 0
            self.turn(self.first_player)


def main():
    input('enter key to begin rolling!')


main()
Game('player 1', 'player 2')


# In[ ]:




