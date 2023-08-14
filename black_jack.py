import random

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if self.number in ['Jack', 'Queen', 'King']:
            self.value = 10
        elif self.number == 'Ace':
            self.value = 11
        else:
            self.value = int(self.number)

class Deck:
    def __init__(self):
        self.cards = []
        self.cards = [Card(suit, number) for suit in suits for number in numbers]
        random.shuffle(self.cards)

    def show_deck(self):
        for card in self.cards:
            print(card.number, "of", card.suit, card.value)

    def topcard(self):
        return self.cards.pop(0)

deck1 = Deck()

deck1.show_deck()