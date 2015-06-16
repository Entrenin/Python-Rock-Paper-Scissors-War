import random

class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.num = number

    def getNumber(self):
        return self.num

    def getSuit(self):
        return self.suit

    def name(self):
        cardNum = self.num

        try:
            cardNum = {
                1: "Ace",
                11: "Jack",
                12: "Queen",
                13: "King"
                }[cardNum]
        except KeyError:
            cardNum = cardNum
        
        return "The {0} of {1}s".format(cardNum, self.suit)

class Deck:

    def __init__(self):

        self.cards = []

        for suit in range(1, 4+1):
            for num in range(1, 13+1):
                {
                    1:self.cards.append(Card("Spade", num)),
                    2:self.cards.append(Card("Heart", num)),
                    3:self.cards.append(Card("Diamond", num)),
                    4:self.cards.append(Card("Club", num))
                }[suit]

    def drawCard(self):
        return random.choice(self.cards)
                
                

def main():
    p = Deck()
    print p.drawCard().name()

main()
