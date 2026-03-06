import random
from enum import Enum


class Suit(Enum):
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"


class Rank(Enum):
    ACE = "Ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit


class Deck:
    def __init__(self, cards):
        # cards should be a stack (a list) of Card
        self.cards = cards

    # Fisher-Yates shuffle
    def shuffle(self):
        shuffled_cards = []
        while len(self.cards) > 0:
            n_cards = len(self.cards)
            k = random.randint(0, n_cards - 1)
            shuffled_cards.append(self.cards.pop(k))
        self.cards = shuffled_cards

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck += str(card) + ", "
        return deck[:-2]

    def __eq__(self, other):
        if not isinstance(other, Deck):
            return NotImplemented
        return self.cards == other.cards


class Hand:
    def __init__(self, cards=[], score=0):
        self.cards = cards
        self.score = score

    def draw_card(self, deck):
        if len(deck.cards) > 0:
            self.cards.append(deck.cards.pop())
        else:
            raise Exception("deck is empty !")

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck += str(card) + ", "
        return deck[:-2]
