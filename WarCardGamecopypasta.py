"""
Implement the card game war. Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins. Winner takes both cards.
3. If players tie, then each player puts down three cards, and the third card competes.
   If a player has less than 3 cards, then they put down all of their cards and their
   final card competes against the other player's third card.
   Continue doing this until tie is broken.
   Winner takes all cards.
4. Game is over when a player doesn't have any cards. The player with cards remaining
   is the winner.
"""
import random

class Card():

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def getNum(self):
        return self.num

    def getSuit(self):
        return self.suit

    def __cmp__(self, other):
        if self.getNum() < other.getNum():
            return -1
        elif self.getNum() == other.getNum():
            return 0
        else: return 1

    def __str__(self):
        return str(self.num) + " of " + str(self.suit) + "s"

def generate_deck(suites=4, type_cards=13):
    "Generate a randomized deck of cards."
    cards = []
    for suite in range(suites):
        for type_card in range(1, type_cards+1):
            cards.append({
                0: Card("Spade", type_card),
                1: Card("Diamond", type_card),
                2: Card("Club", type_card),
                3: Card("Heart", type_card)
                }[suite])
    random.shuffle(cards)
    return cards

def play_warAI(deck):
    a_cards = deck[:len(deck)/2]
    b_cards = deck[len(deck)/2:]
    a_stash = []
    b_stash = []

    round = 1
    while a_cards and b_cards:
        # by using pop, we're playing from the end forward
        a_card = a_cards.pop()
        b_card = b_cards.pop()

        print "(%s) vs (%s)" % (a_card, b_card)

        if a_card == b_card:
            a_stash.extend([a_card]+a_cards[-3:])
            a_cards = a_cards[:-3]
            a_cards.append(a_stash.pop())

            b_stash.extend([b_card]+b_cards[-3:])
            b_cards = b_cards[:-3]
            b_cards.append(b_stash.pop())
        elif a_card > b_card:
            # ordering of a_stash and b_stash is undefined by game rules
            a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
            a_stash = []
            b_stash = []
        elif b_card > a_card:
            # ordering of a_stash and b_stash is undefined by game rules
            b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
            a_stash = []
            b_stash = []

        print "round %s: a_cards: %s, a_stash %s, b_cards %s, b_stash %s" % (round, len(a_cards), len(a_stash), len(b_cards), len(b_stash))
        round += 1

def play_warVSAI(deck):
    a_cards = deck[:len(deck)/2]
    b_cards = deck[len(deck)/2:]
    a_stash = []
    b_stash = []

    round = 1
    while a_cards and b_cards:
        # by using pop, we're playing from the end forward
        a_card = a_cards.pop()

        print "Number then Suit (13 Spade)"
        b_input = raw_input("Card: ")
        b_input_list = b_input.split()
        
        b_card = Card(b_input_list[1], int(b_input_list[0]))

        print "(%s) vs (%s)" % (a_card, b_card)

        if a_card == b_card:
            a_stash.extend([a_card]+a_cards[-3:])
            a_cards = a_cards[:-3]
            a_cards.append(a_stash.pop())

            b_stash.extend([b_card]+b_cards[-3:])
            b_cards = b_cards[:-3]
            b_cards.append(b_stash.pop())
        elif a_card > b_card:
            # ordering of a_stash and b_stash is undefined by game rules
            a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
            a_stash = []
            b_stash = []
        elif b_card > a_card:
            # ordering of a_stash and b_stash is undefined by game rules
            b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
            a_stash = []
            b_stash = []

        print "round %s: a_cards: %s, a_stash %s, b_cards %s, b_stash %s" % (round, len(a_cards), len(a_stash), len(b_cards), len(b_stash))
        round += 1


def main():
    deck = generate_deck()
    play_warVSAI(deck)
    deck = generate_deck()
    play_warAI(deck)

main()
