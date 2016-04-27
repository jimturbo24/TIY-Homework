import unittest
import random

class PlayingCard:
    def __init__(self, value, suit):
        if suit not in self.suits:
            raise AttributeError("suit not valid")
        if value not in self.values:
            raise AttributeError("value not valid")

        self.value = value
        self.suit = suit
        self.long_name = value + " " + suit
    suits = ('hearts', 'clubs', 'diamonds', 'spades')
    values = {'ace': 'ace',
              '2': 'duece',
              '3': 'three',
              '4': 'four',
              '5': 'five',
              '6': 'six',
              '7': 'seven',
              '8': 'eight',
              '9': 'nine',
              '10': 'ten',
              'queen': 'queen',
              'king': 'king',
              'jack': 'jack'}

    def shortName(self):
        return '{0}{1}'.format(self.value[0].upper(),
                               self.suit[0].upper())

    def longName(self):
        return '{0} of {1}'.format(self.values[self.value].capitalize(),
                                   self.suit.capitalize())

class Deck(PlayingCard):
    def __init__(self):
        self.cards = []
        for suit in PlayingCard.suits:
            for value in PlayingCard.values:
                self.cards.append(PlayingCard(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return


deck = Deck()
print(deck.cards[0].longName())
# deck.shuffle()
playercards = []
playercards.append(deck.pop())

# playAgain = "y"
#
# print("""\n         ------ Let's Play Blackjack! ------
# You will be playing against a computer generated dealer. Your goal is to have
# more points than the dealer without exeeding 21 points. You win if you have
# more points than dealer, but less than 21 points. Have fun!\n""")
#
# while "y" in playAgain.lower():
#
#
#     playAgain = input("Wanna play again (y/n)?")
