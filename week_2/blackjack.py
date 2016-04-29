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

    def get_value(self):
        return self.value

    def num_val(self):
        if self.value in ('jack', 'queen', 'king'):
            return 10
        elif self.value == 'ace':
            return 11
        else:
            return int(self.value)


class Deck:
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


class Hand:
    def __init__(self):
        self.cards = []

    def dealt_a_card(self, aCard):
        return self.cards.append(aCard)

    def get_last_card(self):
        return(self.cards[len(self.cards)-1].long_name())

    def sum_of_hand(self):
        score = 0
        for num in range(0, len(self.cards)):
            score += self.cards[num].num_val()
        for num in range(0, len(self.cards)):
            if self.cards[num].get_value() == 'ace':
                if score > 21:
                    score -= 10
        return score

    def get_results(self):
        for num in range(0, len(self.cards)):
            print(self.cards[num].long_name())
        print('Score: {0}'.format(self.sum_of_hand()))


class Cash:
    def __init__(self, pot):
        self.pot = pot


playAgain = "y"
wallet = 100
bet = 10

print("""\n                 ------ Let's Play Blackjack! ------
You will be playing against a computer generated dealer. Your goal is to have
more points than the dealer without exeeding 21 points. You win if you have
more points than dealer, or exactly 21 points. Have fun!\n""")

while "y" in playAgain.lower():

    deck = Deck()
    deck.shuffle()
    playerHand = Hand()
    computerHand = Hand()
    exit = 1

    while len(computerHand.cards) < 2:
        playerHand.dealt_a_card(deck.deal_one())
        computerHand.dealt_a_card(deck.deal_one())

    while exit:
        print('\nYour hand: ')
        playerHand.get_results()
        print("You have ${0} in your wallet.".format((wallet-bet)))
        print('\nDealer hand: ')
        computerHand.get_results()

        if playerHand.sum_of_hand() == 21:
            print("\nBlackjack, you win!")
            wallet += bet
            break
        elif playerHand.sum_of_hand() > 21:
            print("\nSorry, you busted. You loose")
            wallet -= bet
            break
        elif computerHand.sum_of_hand() == 21:
            print("\nYou loose! The dealer hit Blackjack")
            wallet -= bet
            break
        elif computerHand.sum_of_hand() > 21:
            print("\nThe dealer busted. You win!")
            wallet += bet
            break

        while True:
            playerChoice = input("\nWould you like to hit(h) or stand(s)? ")
            if 'h' in playerChoice.lower():
                playerHand.dealt_a_card(deck.deal_one())
                print("You hit....{0}".format(playerHand.get_last_card()))
                if computerHand.sum_of_hand() < 17:
                    computerHand.dealt_a_card(deck.deal_one())
                    print("Dealer hits....{0}".format(computerHand.get_last_card()))
                    break
                else:
                    print("Dealer stands.")
                    break
            elif 's' in playerChoice.lower():
                print("You stand.")
                if computerHand.sum_of_hand() < 17:
                    computerHand.dealt_a_card(deck.deal_one())
                    print("Dealer hits....{0}".format(computerHand.get_last_card()))
                    break
                elif computerHand.sum_of_hand() < playerHand.sum_of_hand():
                    print("Dealer stands.\nYou win!")
                    wallet += bet
                    exit = 0
                    break
                elif computerHand.sum_of_hand() > playerHand.sum_of_hand():
                    print("Dealer stands.\nYou loose!")
                    wallet -= bet
                    exit = 0
                    break
                else:
                    print("Dealer stands.\nIt's a draw!")
                    exit = 0
                    break
            else:
                print("I didn't catch that?")
                continue

    playAgain = input("\nDeal again (y/n)?")
