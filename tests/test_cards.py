import unittest

from cards import Card, Deck, Hand, Rank, Suit


class TestDeck(unittest.TestCase):
    def test_print_card(self):
        card = Card(Rank.TWO, Suit.SPADES)
        self.assertEqual(
            str(card),
            "2 of Spades",
        )

    def test_print_deck(self):
        deck = Deck(
            [
                Card(Rank.TWO, Suit.SPADES),
                Card(Rank.SIX, Suit.HEARTS),
                Card(Rank.JACK, Suit.DIAMONDS),
                Card(Rank.ACE, Suit.CLUBS),
            ]
        )
        str_deck = "2 of Spades, 6 of Hearts, Jack of Diamonds, Ace of Clubs"
        self.assertEqual(str(deck), str_deck)

    def test_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle()
        self.assertNotEqual(deck1, deck2)


class TestHand(unittest.TestCase):
    def test_4_cards(self):
        hand = Hand(
            [
                Card(Rank.TWO, Suit.SPADES),
                Card(Rank.SIX, Suit.HEARTS),
                Card(Rank.JACK, Suit.DIAMONDS),
                Card(Rank.ACE, Suit.CLUBS),
            ]
        )
        self.assertEqual(hand.score(), 2 + 6 + 10 + 1)

    def test_print_deck(self):
        hand = Hand(
            [
                Card(Rank.TWO, Suit.SPADES),
                Card(Rank.ACE, Suit.CLUBS),
            ]
        )
        self.assertEqual(hand.score(), 2 + 11)


if __name__ == "__main__":
    unittest.main()
