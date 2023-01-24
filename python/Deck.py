import enum
import itertools
import Card
import random

class Comparator:
    LESS = -1
    EQUAL = 0
    GREATER = 1

class Deck:
    SUIT_LIST = ['Spade', 'Heart', 'Club', 'Diamond'];
    VALUE_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'K', 'A']
    def __init__(self):
        self.cards = [Card.Card(x[0], x[1]) for x in itertools.product(Deck.SUIT_LIST, Deck.VALUE_LIST)]
        self.discard = []

    def shuffle_all(self):
        self.cards = self.cards + self.discard
        self.discard = []
        random.shuffle(self.cards)

    def shuffle_current(self):
        random.shuffle(self.cards)

    def draw_and_discard(self):
        card = self.cards.pop()
        self.discard.append(card)
        return card # Beware, this is a reference

    def draw_and_replace(self):
        self.cards.insert(0, self.cards.pop())
        return self.cards[0]

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle_all()
    print(deck.draw_and_replace().Display())
    print('Size of deck:', len(deck.cards))
    print(deck.draw_and_discard().Display())
    print('Size of deck:', len(deck.cards))
    print('Size of discard:', len(deck.discard))
    deck.shuffle_current()
    print('Size of deck:', len(deck.cards))
    print('Size of discard:', len(deck.discard))
    deck.shuffle_all()
    print('Size of deck:', len(deck.cards))
    print('Size of discard:', len(deck.discard))