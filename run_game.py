from cards import Deck, Hand
from strategies import BasicStrategy, DealerStrategy

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
def run_game(strategy=DealerStrategy()):
    deck = Deck()
    deck.shuffle()

    player, dealer = Hand(), Hand()

    # each player starts with 2 cards
    player.draw_card(deck, 2)
    dealer.draw_card(deck, 2)

    # player's turn
    if hasattr(strategy, "opponent_card"):
        strategy.opponent_card = dealer.cards[0]
    strategy(player, deck)
    if player.score() > 21:
        return (-player.bet, player.bet)  # player busts

    # dealer's turn
    DealerStrategy()(dealer, deck)
    if dealer.score() > 21:
        return (player.bet, player.bet)  # dealer busts

    # outcome if no bust
    if player.score() > dealer.score():
        return (player.bet, player.bet)
    if player.score() < dealer.score():
        return (-player.bet, player.bet)
    return (0, player.bet)
