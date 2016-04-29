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
    def num_val(self):
        if self.value in ('jack', 'queen', 'king'):
            return 10
        elif self.value == 'ace':
            return 11
        else:
            return int(self.value)


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


class Hand():
    def __init__(self):
        self.cards = []

    def dealt_a_card(self, aCard):
        return self.cards.append(aCard)

    def get_hand(self):
        for num in range(0, len(self.cards)-1):
            print(self.cards[num].long_name())

    def get_last_card(self):
        return(self.cards[len(self.cards)-1].long_name())

    def sum_of_hand(self):
        score = 0
        for num in range(0, len(self.cards)-1):
            score += self.cards[num].num_val()
        return score

    def get_results(self):
        self.get_hand()
        print('Score: {0}'.format(self.sum_of_hand()))



playAgain = "y"

print("""\n         ------ Let's Play Blackjack! ------
You will be playing against a computer generated dealer. Your goal is to have
more points than the dealer without exeeding 21 points. You win if you have
more points than dealer, but less than 21 points. Have fun!\n""")

while "y" in playAgain.lower():

    deck = Deck()
    deck.shuffle()
    playerHand = Hand()
    computerHand = Hand()
    exit = 1

    while len(computerHand.cards) < 3:
        playerHand.dealt_a_card(deck.deal_one())
        computerHand.dealt_a_card(deck.deal_one())

    while exit:
        if playerHand.sum_of_hand() == 21:
            print("Blackjack, you win!")
            break
        elif playerHand.sum_of_hand() > 21:
            print("Sorry, you busted. You loose")
            break
        elif computerHand.sum_of_hand() == 21:
            print("You loose! The dealer hit Blackjack")
            break
        elif computerHand.sum_of_hand() > 21:
            print("The dealer busted. You win!")
            break

        print('\nYour hand: ')
        playerHand.get_results()
        print('\nDealer hand: ')
        computerHand.get_results()

        while True:
            playerChoice = input("\nWould you like to hit(h) or stand(s)? ")
            if 'h' in playerChoice.lower():
                print("You hit....{0}".format(playerHand.get_last_card()))
                playerHand.dealt_a_card(deck.deal_one())
                if computerHand.sum_of_hand() < 17:
                    print("Dealer hits....{0}".format(computerHand.get_last_card()))
                    computerHand.dealt_a_card(deck.deal_one())
                    break
                else:
                    print("Dealer stands.")
                    break
            elif 's' in playerChoice.lower():
                print("You stand.")
                if computerHand.sum_of_hand() < 17:
                    print("Dealer hits....{0}".format(computerHand.get_last_card()))
                    computerHand.dealt_a_card(deck.deal_one())
                    break
                elif computerHand.sum_of_hand() < playerHand.sum_of_hand():
                    print("Dealer stands. You win!")
                    exit = 0
                    break
                elif computerHand.sum_of_hand() > playerHand.sum_of_hand():
                    print("Dealer stands. You loose!")
                    exit = 0
                    break
                else:
                    print("Dealer stands.")
                    print("It's a draw!")
                    exit = 0
                    break
            else:
                print("I didn't catch that?")
                continue

    playAgain = input("\nDeal again (y/n)?")
