import csv

import matplotlib.pyplot as plt
import pandas as pd


def plot_data():
    df = pd.read_csv("MC_data_homemade_strategy.csv")
    results_basic = df[df["Strategy"] == "HomeMade"].pivot(
        index="opponent_value_threshold", columns="player_score_threshold", values="mu"
    )

    matrix = results_basic.values

    fig, ax = plt.subplots()
    im = ax.imshow(results_basic)
    ax.set_title("Gain expectation value at BlackJack")

    ax.set_xlabel("player threshold")
    ax.set_xticks(range(len(results_basic.columns)))
    ax.set_xticklabels(results_basic.columns.astype(int))

    ax.set_ylabel("dealer threshold")
    ax.set_yticks(range(len(results_basic.index)))
    ax.set_yticklabels(results_basic.index.astype(int))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ax.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center", fontsize=8)

    # plt.colorbar(im)

    plt.savefig("heatmap.png")
    plt.show()


plot_data()
