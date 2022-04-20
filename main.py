from strategies import *

strategies = ["TitForTat", "AlwaysDefect", "AlwaysCooperate", "Trigger", "Random", "SecondByChampion",
              "Prober", "TitFor2Tat", "MyStrategy"]


def choose_strategy(shortcut, history):
    """
    Chooses strategy and assigns the opponent's history
    :param shortcut: Shortcut for strategy
    :param history: History of player1 or player2
    :return: string
    """
    return {
        "TitForTat": tit_for_tat(history),
        "AlwaysDefect": "Defect",
        "AlwaysCooperate": "Cooperate",
        "Trigger": trigger(history),
        "Random": random_decision(),
        "SecondByChampion": second_by_champion(history),
        "TitFor2Tat": tit_for_2tat(history),
        "Prober": prober(history),
        "MyStrategy": my_strategy(history)
    }[shortcut]


def calculate_points(first_strategy_decision, second_strategy_decision):
    """
    Returns points according to the rules of Prisoner's dilemma
    :param first_strategy_decision: Result of first strategy
    :param second_strategy_decision: Result of second strategy
    :return: int
    """

    if first_strategy_decision == "Cooperate" and second_strategy_decision == "Defect":
        return 0, 5
    elif first_strategy_decision == "Defect" and second_strategy_decision == "Cooperate":
        return 5, 0
    elif first_strategy_decision == "Defect" and second_strategy_decision == "Defect":
        return 1, 1
    return 3, 3


if __name__ == '__main__':

    strategy_points = dict.fromkeys(strategies, 0)  # using dictionary for saving the points

    player1_history = []
    player2_history = []
    rounds = 200

    for player1 in strategies:
        for player2 in strategies:
            # history resets every round
            player1_history = []
            player2_history = []
            for iterations in range(rounds):
                player1_points, player2_points = calculate_points(choose_strategy(player1, player2_history),
                                                                  choose_strategy(player2, player1_history))
                player1_history.append(choose_strategy(player1, player2_history))
                player2_history.append(choose_strategy(player2, player1_history))

                strategy_points[player1] += player1_points

    for key in strategy_points:
        print(key, "strategy has average of", strategy_points[key]/rounds, "points.")
