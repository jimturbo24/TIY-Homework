import unittest

class PlayingCard:
    def __init__(self, suit, value):
        if not suit and not value:
            raise AttributeError("Suit and/or value omitted")
        if suit not in self.suitsList:
            raise AttributeError("The card suit entered is invalid")
        if value not in self.valuesList:
            raise AttributeError("The card value entered is invalid")
        self.suit = suit
        self.value = value

    suitsList = ['spades', 'clubs', 'hearts', 'diamonds']
    valuesList = ['ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'jack', 'queen', 'king']
    valuesDict = {'ace': 'ace', '2': 'two', '3': 'three',
                  '4': 'four', '5': 'five', '6': 'six',
                  '7': 'seven', '8': 'eight', '9': 'nine',
                  '10': 'ten', 'jack': 'jack', 'queen': 'queen',
                  'king': 'king'}

    def shortName(self):
        name = ("{0}{1}".format(self.value[0].capitalize(),
                                self.suit[0].capitalize()))
        return name

    def longName(self):
        name = ("{0} of {1}".format(PlayingCard.valuesDict
                                    [self.value].capitalize(),
                                     self.suit.capitalize()))
        return name


aCard = PlayingCard('clubs', '7')
# print(aCard.suit, aCard.value)
# print(PlayingCard.valuesDict)
# print(aCard.shortName())
# print(aCard.longName())

class TestPlayingCardMethods(unittest.TestCase):

    def test_shortName(self):
        self.assertEqual(aCard.shortName(), '7C')

    def test_longName(self):
        self.assertEqual(aCard.longName(), 'Seven of Clubs')

if __name__ == '__main__':
    unittest.main()
