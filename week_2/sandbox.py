class Cash:
    def __init__(self, bet, wallet):
        self.bet = bet
        self.wallet = wallet

    # def win(self):
    #     return self.wallet += self.bet * 2
    #
    # def loose(self):
    #     return self.wallet -= self.bet * 2



playerCash = Cash(10, 100)

# playerCash.win()

print(type(playerCash.bet))
print(playerCash.wallet)

# # deck = Deck()
# # deck.shuffle()
# hand_1 = Hand()
# # hand_2 = Hand()
#
# hand_1.dealt_a_card(PlayingCard('ace', 'spades'))
# hand_1.dealt_a_card(PlayingCard('ace', 'hearts'))
# # hand_1.dealt_a_card(PlayingCard('jack', 'hearts'))
# hand_1.dealt_a_card(PlayingCard('ace', 'hearts'))
#
# print(hand_1.cards)
# print(len(hand_1.cards))
# # print(hand_1.cards[0].value)
# # print(hand_1.cards[1].value)
# hand_1.get_results()
