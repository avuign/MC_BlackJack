class Strategy:
    def __call__(self, player, deck):
        raise NotImplementedError


class DealerStrategy(Strategy):
    def __call__(self, player, deck):
        while player.score() < 17:
            player.draw_card(deck)


class HomeMadeStrategy(Strategy):
    def __init__(self, opponent_card=None, dealer_card=2, player_score=5):
        self.opponent_card = opponent_card
        self.dealer_card_threshold = dealer_card
        self.player_score_threshold = player_score

    def __call__(self, player, deck):
        while (
            player.score() < self.player_score_threshold
            and self.opponent_card.get_value() > self.dealer_card_threshold
        ):
            player.draw_card(deck)


class BasicStrategy(Strategy):
    def __init__(self, opponent_card=None):
        self.opponent_card = opponent_card

    def __call__(self, player, deck):
        dealer = self.opponent_card.get_value()
        while player.score() < 9:
            player.draw_card(deck)
        if player.score() == 9:
            if 3 <= dealer <= 6:
                if len(player.cards) < 2:
                    player.double(deck)
                else:
                    player.draw_card(deck)
            else:
                player.draw_card(deck)
        if player.score() == 10:
            if dealer <= 9:
                if len(player.cards) < 2:
                    player.double(deck)
                else:
                    player.draw_card(deck)
            else:
                player.draw_card(deck)
        if player.score() == 11:
            player.draw_card(deck)
        if player.score() == 12 and (dealer < 4 or dealer > 6):
            player.draw_card(deck)
        while 13 <= player.score() <= 16 and dealer > 6:
            player.draw_card(deck)
