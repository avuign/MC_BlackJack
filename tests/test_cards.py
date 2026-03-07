import unittest

from cards import Card, Deck, Hand, Rank, Suit


class TestDeck(unittest.TestCase):
    def test_print_card(self):
        card = Card(Rank.TWO, Suit.SPADES)
        self.assertEqual(
            str(card),
            "Two of Spades",
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
        str_deck = "Two of Spades, Six of Hearts, Jack of Diamonds, Ace of Clubs"
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

    def test_card_value(self):
        two_of_spades = Card(Rank.TWO, Suit.SPADES)
        six_of_hearts = Card(Rank.SIX, Suit.HEARTS)
        jack_of_diamonds = Card(Rank.JACK, Suit.DIAMONDS)
        ace_of_clubs = Card(Rank.ACE, Suit.CLUBS)

        values = [
            two_of_spades.get_value(),
            six_of_hearts.get_value(),
            jack_of_diamonds.get_value(),
            ace_of_clubs.get_value(),
        ]

        self.assertListEqual(values, [2, 6, 10, 11])


if __name__ == "__main__":
    unittest.main()
