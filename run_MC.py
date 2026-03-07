import csv
import math

from cards import Card, Deck, Hand, Rank, Suit
from run_game import run_game
from strategies import BasicStrategy, DealerStrategy, HomeMadeStrategy


def MonteCarlo(n, strategy=DealerStrategy()):
    total_gain = 0
    total_sq = 0
    total_bet = 0
    for i in range(0, n):
        result = run_game(strategy)
        total_gain += result[0]
        total_bet += result[1]
        total_sq += result[0] ** 2
    mean_gain = total_gain / n
    mean_bet = total_bet / n
    std_dev = math.sqrt((total_sq / n - mean_gain**2) / n)
    return mean_gain / mean_bet, std_dev / mean_bet


def main():
    n = 10000
    with open("MC_data_homemade_strategy.csv", "w", newline="") as csvfile:
        datawriter = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        datawriter.writerow(
            [
                "Strategy",
                "opponent_value_threshold",
                "player_score_threshold",
                "mu",
                "sigma",
                "N",
            ]
        )
        for i in range(2, 12):
            for j in range(5, 21):
                mc = MonteCarlo(n, HomeMadeStrategy(None, i, j))
                datawriter.writerow(["HomeMade", i, j, mc[0], mc[1], n])


main()
