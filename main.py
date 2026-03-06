import math

from cards import Card, Deck, Hand, Rank, Suit
from run_game import run_game
from strategies import basic_strategy


def MonteCarlo(n, strategy=basic_strategy):
    total = 0
    total_sq = 0
    for i in range(0, n):
        result = run_game(strategy)
        total += result
        total_sq += result * result
    mean = total / n
    std_dev = math.sqrt((total_sq / n - mean**2) / n)
    return mean, std_dev


def main():
    print(MonteCarlo(1000)[1])


main()
