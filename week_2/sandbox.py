class Hand():
    def __init__(self):
        self.cards = []

    def append_five(self, value):
        return self.cards.append(value)

    def initial_hand(self, aCard):
        count = 2
        while count:
            return self.dealt_a_card(aCard)

# playerHand = Hand()
# playerHand.append_five(5)
# playerHand.append_five(6)
# playerHand.append_five(7)
#
# print(playerHand.cards[0])
# print(playerHand.cards[1])
# print(playerHand.cards[2])


count = 2
while count:
    print(count)
    count -= 1


# card = PlayingCard('5', 'spades')
# print(card)
#
# test_deck = [PlayingCard('2', 'clubs'), PlayingCard('7', 'hearts')]
# print(test_deck)
