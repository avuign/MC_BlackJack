from cards import Deck, Hand
from strategies import basic_strategy

"""
RULES :
    One player vs the dealer, both start with 2 cards. One of the dealer's card is hidden.

    Player's turn :
        Player can draw or not draw
        if player exceeds 21 -> bust

    Dealer's turn :
        Dealer reaveals hidden card
        Dealer must draw is score <17 and not draw if score >=17
        If Dealer busts -> player wins

    Outcomes :
        neither busts -> highest score wins
        equal scores -> draw
"""


# -1 : loose, 0 : draw, 1 : win
def run_game(strategy=basic_strategy):
    deck = Deck()
    deck.shuffle()

    player, dealer = Hand(), Hand()

    # each player starts with 2 cards
    player.draw_card(deck, 2)
    dealer.draw_card(deck, 2)

    # player's turn
    strategy(player, deck)
    if player.score() > 21:
        return -1  # player busts

    # dealer's turn
    basic_strategy(dealer, deck)
    if dealer.score() > 21:
        return 1  # dealer busts

    # outcome if no bust
    if player.score() > dealer.score():
        return 1
    if player.score() < dealer.score():
        return -1
    return 0


def run_game_commented():
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    # each player starts with 2 cards
    player.draw_card(deck, 2)
    print(
        "initial player's hand : " + str(player) + " and score : " + str(player.score())
    )
    dealer.draw_card(deck, 2)
    print(
        "initial dealer's hand : " + str(dealer) + " and score : " + str(dealer.score())
    )

    # player's turn
    # hardcode strategy : we copy the dealer's strategy
    while player.score() < 17:
        print("player draws")
        player.draw_card(deck)
        print("player's hand : " + str(player) + " and score : " + str(player.score()))
        if player.score() > 21:
            print("player busts !")
            return -1  # player busts

    # dealer's turn
    while dealer.score() < 17:
        print("dealer draws")
        dealer.draw_card(deck)
        print("dealer's hand : " + str(dealer) + " and score : " + str(dealer.score()))
        if dealer.score() > 21:
            print("dealer busts !")
            return 1  # dealer busts

    # outcome if no bust
    if player.score() > dealer.score():
        print("player wins !")
        return 1
    if player.score() < dealer.score():
        print("player looses !")
        return -1
    print("draw !")
    return 0
