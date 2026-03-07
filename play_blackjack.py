from cards import Deck, Hand


def play():
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    # each player starts with 2 cards
    player.draw_card(deck, 2)
    print(
        "Player's initial hand : " + str(player) + " and score : " + str(player.score())
    )
    dealer.draw_card(deck, 2)
    dealer_card = dealer.cards[-1]
    print(
        "dealer's card : "
        + str(dealer_card)
        + " with score : "
        + str(dealer_card.get_value())
    )

    # player's turn
    #
    players_turn = True

    print("Player's turn...")

    while players_turn:
        action = input("Hit (H), Stand (S), or Double (D)? ")
        if action.lower() in ["h", "hit"]:
            player.draw_card(deck)
            print("You draw : " + str(player.cards[-1]))
        elif action.lower() in ["d", "double"]:
            if len(player.cards) < 3:
                player.double(deck)
                print("You draw : " + str(player.cards[-1]))
                players_turn = False
            else:
                print("you can not double with more than two cards !")
                continue
        elif action.lower() in ["s", "stand"]:
            players_turn = False
        else:
            print("Please enter a correct input !")
            continue

        print("current hand : " + str(player) + " and score : " + str(player.score()))

        if player.score() > 21:
            print("player busts ! You loose.")
            return -1
    print("player's hand : " + str(player) + " and score : " + str(player.score()))

    print("Dealer's turn...")
    # dealer's turn
    while dealer.score() < 17:
        print("dealer draws")
        dealer.draw_card(deck)

        if dealer.score() > 21:
            print(
                "Dealer's final hand : "
                + str(dealer)
                + " and score : "
                + str(dealer.score())
            )
            print("dealer busts ! You win.")
            return 1  # dealer busts

    print(
        "Player's final hand : " + str(player) + " and score : " + str(player.score())
    )
    print(
        "Dealer's final hand : " + str(dealer) + " and score : " + str(dealer.score())
    )

    # outcome if no bust
    if player.score() > dealer.score():
        print("You win.")
        return 1
    if player.score() < dealer.score():
        print("You loose.")
        return -1
    print("draw !")
    return 0


play()
