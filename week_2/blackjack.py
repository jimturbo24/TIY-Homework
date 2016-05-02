import unittest
import random
import time
import sys

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
        for num in Deck.deckNumber:
            for suit in PlayingCard.suits:
                for value in PlayingCard.values:
                    self.cards.append(PlayingCard(value, suit))

    deckNumber = [1, 2, 3, 4]

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def deal_one(self):
        return self.cards.pop()

    def deck_length(self):
        return len(self.cards)


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

class TestPlayingCard(unittest.TestCase):
    def testSuits(self):
        self.assertEqual(4, len(PlayingCard.suits))
        self.assertTrue('hearts' in PlayingCard.suits)
        self.assertFalse('weasels' in PlayingCard.suits)

    def testValues(self):
        self.assertEqual(13, len(PlayingCard.values))
        self.assertTrue('9' in PlayingCard.values)
        self.assertTrue('21' not in PlayingCard.values)

    def testInit(self):
        pc1 = PlayingCard('ace', 'hearts')
        self.assertEqual('ace', pc1.value)
        self.assertEqual('hearts', pc1.suit)
        with self.assertRaises(TypeError):
            pc2 = PlayingCard()

        with self.assertRaises(AttributeError):
            pc3 = PlayingCard('duke', 'earl')

    def testShortName(self):
        pc1 = PlayingCard('9', 'clubs')
        self.assertEqual('9C', pc1.short_name())
        self.assertNotEqual('AH', pc1.short_name())

    def testLongName(self):
        pc = PlayingCard('10', 'hearts')
        self.assertEqual('Ten of Hearts', pc.long_name())
        self.assertNotEqual('ten of hearts', pc.long_name())

    def testGetValue(self):
        pc = PlayingCard('10', 'hearts')
        self.assertEqual('10', pc.get_value())
        self.assertNotEqual(10, pc.get_value())

    def testNumVal(self):
        pc1 = PlayingCard('ace', 'hearts')
        self.assertEqual(11, pc1.num_val())
        pc2 = PlayingCard('3', 'clubs')
        self.assertEqual(3, pc2.num_val())
        pc3 = PlayingCard('queen', 'spades')
        self.assertEqual(10, pc3.num_val())

class TestDeck(unittest.TestCase):
    def testInit(self):
        deck = Deck()
        self.assertEqual(208, len(deck.cards))

    def testShuffle(self):
        deck = Deck()
        copy_of_cards = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(copy_of_cards, deck.cards)

    def testDealOne(self):
        deck = Deck()
        self.assertTrue(deck.deal_one() not in deck.cards)

    def testDeckLength(self):
        deck = Deck()
        self.assertEqual(208, deck.deck_length())
        self.assertNotEqual(52, deck.deck_length())

class TestHand(unittest.TestCase):
    def testInit(self):
        aHand = Hand()
        self.assertEqual(0, len(aHand.cards))

    def testDealtACard(self):
        aHand = Hand()
        aHand.dealt_a_card('something')
        self.assertEqual(1, len(aHand.cards))
        self.assertTrue('something' in aHand.cards)
        self.assertFalse('nothing' in aHand.cards)

    def testGetLastCard(self):
        aHand = Hand()
        aHand.dealt_a_card(PlayingCard('ace', 'spades'))
        self.assertEqual('Ace of Spades', aHand.get_last_card())
        self.assertNotEqual('Three of Spades', aHand.get_last_card())

    def testSumOfHand(self):
        aHand = Hand()
        aHand.dealt_a_card(PlayingCard('ace', 'spades'))
        aHand.dealt_a_card(PlayingCard('jack', 'hearts'))
        self.assertEqual(21, aHand.sum_of_hand())
        self.assertNotEqual(11, aHand.sum_of_hand())


    def testGetResults(self):
        pass # not sure how to write a test for this.



def slow_dots(dots):
    for char in dots:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.5)

# if __name__ == '__main__':
#     unittest.main()

playAgain = "y"
bet = 10
wallet = 100
deck = Deck()
deck.shuffle()
sixDots = "...."


print("""\n                 ------ Let's Play Blackjack! ------
You will be playing against a computer generated dealer. Your goal is to have
more points than the dealer without exeeding 21 points. You will start with $100
and each bet costs $10. You win the hand if you have more points than dealer
after you both stand or if you have exactly 21 points. The game ends when you
have no more money, if you win $1000, or if you choose to no longer play.\n""")

while "y" in playAgain.lower():
    playerHand = Hand()
    computerHand = Hand()
    exit = 1

    if deck.deck_length() < 26:
        print("\nOne moment the dealer is reshuffling", end='')
        slow_dots(sixDots)
        deck = Deck()
        deck.shuffle()

    while len(computerHand.cards) < 2:
        playerHand.dealt_a_card(deck.deal_one())
        computerHand.dealt_a_card(deck.deal_one())

    if wallet <= 0:
        print("\nOoops, you have no money left.\nThanks for your contribution!")
        break
    elif wallet >= 1000:
        print("\nOoops, I didn't realize you had won so much!")
        print("These gentlemen will help you find another place to gamble.")
        break

    while exit:
        print("\nYour bet: ${0}".format((bet)))
        print('\nYour hand: ')
        playerHand.get_results()
        print('\nDealer hand: ')
        computerHand.get_results()

        if playerHand.sum_of_hand() == 21:
            print("\nBlackjack, you win!")
            wallet += bet
            print("You have ${0} in your wallet.".format((wallet)))
            break
        elif playerHand.sum_of_hand() > 21:
            print("\nSorry, you busted. You loose")
            wallet -= bet
            print("You have ${0} in your wallet.".format((wallet)))
            break
        elif computerHand.sum_of_hand() == 21:
            print("\nYou loose! The dealer hit Blackjack")
            wallet -= bet
            print("You have ${0} in your wallet.".format((wallet)))
            break
        elif computerHand.sum_of_hand() > 21:
            print("\nThe dealer busted. You win!")
            wallet += bet
            print("You have ${0} in your wallet.".format((wallet)))
            break

        while True:
            playerChoice = input("\nYou can Hit(h), Stand(s), Double(d), or Surrender(x)? ")
            if 'h' in playerChoice.lower():
                playerHand.dealt_a_card(deck.deal_one())
                print("You hit", end='')
                slow_dots(sixDots)
                print(playerHand.get_last_card())
                if playerHand.sum_of_hand() == 21:
                    print("\nBlackjack, you win!")
                    wallet += bet
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                elif playerHand.sum_of_hand() > 21:
                    print("\nSorry, you busted. You loose")
                    wallet -= bet
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                if computerHand.sum_of_hand() < 17:
                    computerHand.dealt_a_card(deck.deal_one())
                    print("Dealer hits", end='')
                    slow_dots(sixDots)
                    print(computerHand.get_last_card())
                    if computerHand.sum_of_hand() == 21:
                        print("\nYou loose! The dealer hit Blackjack")
                        wallet -= bet
                        print("You have ${0} in your wallet.".format((wallet)))
                        exit = 0
                        break
                    elif computerHand.sum_of_hand() > 21:
                        print("\nThe dealer busted. You win!")
                        wallet += bet
                        print("You have ${0} in your wallet.".format((wallet)))
                        exit = 0
                        break
                    else:
                        break
                else:
                    print("Dealer stands.")
                    time.sleep(1)
                    break
            elif 's' in playerChoice.lower():
                print("You stand.")
                time.sleep(1)
                if computerHand.sum_of_hand() < 17:
                    computerHand.dealt_a_card(deck.deal_one())
                    print("Dealer hits", end='')
                    slow_dots(sixDots)
                    print(computerHand.get_last_card())
                    if computerHand.sum_of_hand() == 21:
                        print("\nYou loose! The dealer hit Blackjack")
                        wallet -= bet
                        print("You have ${0} in your wallet.".format((wallet)))
                        exit = 0
                        break
                    elif computerHand.sum_of_hand() > 21:
                        print("\nThe dealer busted. You win!")
                        wallet += bet
                        print("You have ${0} in your wallet.".format((wallet)))
                        exit = 0
                        break
                    else:
                        break
                elif computerHand.sum_of_hand() < playerHand.sum_of_hand():
                    print("Dealer stands.\nYou win!")
                    wallet += bet
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                elif computerHand.sum_of_hand() > playerHand.sum_of_hand():
                    print("Dealer stands.\nYou loose!")
                    wallet -= bet
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                else:
                    print("Dealer stands.\nIt's a draw!")
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
            elif 'd' in playerChoice.lower():
                print("\nYour bet: ${0}".format((bet*2)))
                playerHand.dealt_a_card(deck.deal_one())
                print("Your last card is", end='')
                slow_dots(sixDots)
                print(playerHand.get_last_card())
                if playerHand.sum_of_hand() == 21:
                    print("\nBlackjack, you win!")
                    wallet += bet * 2
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                elif playerHand.sum_of_hand() > 21:
                    print("\nSorry, you busted. You loose")
                    wallet -= bet * 2
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break

                while computerHand.sum_of_hand() < 17:
                    computerHand.dealt_a_card(deck.deal_one())
                    print("Dealer hits", end='')
                    slow_dots(sixDots)
                    print(computerHand.get_last_card())
                if computerHand.sum_of_hand() == 21:
                    print("\nYou loose! The dealer hit Blackjack")
                    wallet -= bet * 2
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                elif computerHand.sum_of_hand() > 21:
                    print("\nThe dealer busted. You win!")
                    wallet += bet * 2
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break

                if computerHand.sum_of_hand() < playerHand.sum_of_hand():
                    print("Dealer stands\nYou have the high score\nYou loose!")
                    wallet += bet * 2
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                elif computerHand.sum_of_hand() > playerHand.sum_of_hand():
                    print("Dealer stands\nDealer has the high score\nYou loose!")
                    wallet -= bet * 2
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
                else:
                    print("Dealer stands.\nIt's a draw!")
                    print("You have ${0} in your wallet.".format((wallet)))
                    exit = 0
                    break
            elif 'x' in playerChoice.lower():
                print("If you can't stand the heat...")
                wallet -= 5
                print("You have ${0} in your wallet.".format((wallet)))
                exit = 0
                break
            else:
                print("I didn't catch that?")
                continue

    playAgain = input("\nDeal again (y/n)?")
