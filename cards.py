import random
from enum import Enum


class Suit(Enum):
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"


class Rank(Enum):
    ACE = "Ace"
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
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


# initialize a list of all 52 cards
def init_cards():
    cards = []
    for suit in Suit:
        for rank in Rank:
            cards.append(Card(rank, suit))
    return cards


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = init_cards()
        else:
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
        if len(self.cards) == 0:
            return "deck is empty"
        deck = ""
        for card in self.cards:
            deck += str(card) + ", "
        return deck[:-2]

    def __eq__(self, other):
        if not isinstance(other, Deck):
            return NotImplemented
        return self.cards == other.cards


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def score(self):
        score = 0
        n_aces = 0
        for card in self.cards:
            if (
                card.rank == Rank.JACK
                or card.rank == Rank.QUEEN
                or card.rank == Rank.KING
            ):
                score += 10
            elif card.rank == Rank.ACE:
                score += 11
                n_aces += 1
            else:
                score += card.rank.value
        while score > 21 and n_aces > 0:
            score -= 10
            n_aces -= 1
        return score

    def draw_card(self, deck, n=1):
        while n > 0:
            if len(deck.cards) > 0:
                self.cards.append(deck.cards.pop())
                n -= 1
            else:
                raise Exception("deck is empty !")

    def __str__(self):
        deck = ""
        for card in self.cards:
            deck += str(card) + ", "
        return deck[:-2]
