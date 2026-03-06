from cards import Deck, Hand


def basic_strategy(player, deck):
    while player.score() < 17:
        player.draw_card(deck)
