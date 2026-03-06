from cards import Card, Deck, Hand, Rank, Suit


def main():
    deck = Deck(
        [
            Card(Rank.TWO, Suit.SPADES),
            Card(Rank.SIX, Suit.HEARTS),
            Card(Rank.JACK, Suit.DIAMONDS),
            Card(Rank.ACE, Suit.CLUBS),
        ]
    )
    hand = Hand()
    print(hand)
    while len(deck.cards) > 0:
        hand.draw_card(deck)
        print(hand)


main()
