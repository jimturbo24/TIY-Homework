class PlayingCard:
    def __init__(self, suit, value):
        if not suit and not value:
            raise AttributeError("Suit and/or value omitted")
        if suit not in self.suits: #['spades', 'clubs', 'hearts', 'diamonds']:
            raise AttributeError("The card suit entered is invalid")
        if value not in self.values: #['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
            raise AttributeError("The card value entered is invalid")
        self.suit = suit
        self.value = value

    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

    def shortName(self):
        pass

    def longName(self):
        pass


AS = PlayingCard('spades', 'ace')
AS.suits

print(AS.suit, AS.value)
print(PlayingCard.suits)
