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
    suits = ('hearts', 'clubs', 'diamonds', 'spades')
    values = {'ace': 'ace',
              '2': 'two',
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

    def short_name(self):
        return '{0}{1}'.format(self.value[0].upper(),
                               self.suit[0].upper())

    def long_name(self):
        return '{0} of {1}'.format(self.values[self.value].capitalize(),
                                   self.suit.capitalize())

class Deck():
    def __init__(self):
        self.cards = []
        for suit in PlayingCard.suits:
            for value in PlayingCard.values:
                self.cards.append(PlayingCard(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def deal_one(self):
        return self.cards.pop()

# card = PlayingCard('5', 'spades')
# print(type(card))
#
# test_deck = [PlayingCard('2', 'clubs'), PlayingCard('7', 'hearts')]
# print(test_deck[0].value)
deck = Deck()
# for card in range(0, 52):
#     print(deck.cards[card].longName())
deck.shuffle()
playerHand = []
playerHand.append(deck.deal_one())
print(len(playerHand))
print(len(deck.cards))
print(playerHand[0].long_name())
playerHand.append(deck.deal_one())
print(playerHand[1].long_name())

# print(deck.deal_one().long_name())
# print(len(deck.cards))


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
