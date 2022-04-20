import random


def my_strategy(decision_history):
    """
    First two rounds starts with Defect, if opponent's last two moves betrays, my strategy betrays too.
    If opponent's last two rounds cooperate, strategy cooperates too. Otherwise it betrays.
    :param decision_history: Opponent's history
    :return: string
    """
    if len(decision_history) < 3:
        return "Defect"
    if decision_history[-1] and decision_history[-2] == "Defect":
        return "Defect"

    return "Cooperate" if decision_history[-1] and decision_history[-2] == "Cooperate" else "Defect"


def tit_for_tat(decision_history):
    """
    Starts cooperate and then copy opponent's previous move.
    :param decision_history: Opponent's history
    :return: string
    """
    if not decision_history:
        return "Cooperate"
    return "Cooperate" if decision_history[-1] == "Cooperate" else "Defect"


def tit_for_2tat(decision_history):
    """
    First two round is cooperating and then betrays if opponent betrayed twice in a row.
    :param decision_history: Opponent's history
    :return: string
    """
    if len(decision_history) < 3:
        return "Cooperate"

    return "Defect" if decision_history[-2] and decision_history[-1] == "Defect" else "Cooperate"


def second_by_champion(decision_history):
    """
    First ten rounds cooperates, after that uses TitForTat strategy until round 25.
    Then cooperates for the rest of the game.
    :param decision_history: Opponent's history
    :return: string
    """

    if len(decision_history) < 10:
        return "Cooperate"
    return tit_for_tat(decision_history) if len(decision_history) < 25 else "Cooperate"


def random_decision():
    """
    Cooperates and betrays randomly.
    :return: string
    """
    randomize_decision = random.randint(0, 1)
    return "Cooperate" if randomize_decision == 1 else "Defect"


def trigger(decision_history):
    """
    Trigger is cooperating until his opponent betrays, then betrays for the rest of the game.
    :param decision_history: Opponent's history
    :return: string
    """

    if "Defect" in decision_history:
        return "Defect"
    return "Cooperate"


def prober(decision_history):
    """
    Starts with Defect, Cooperate, Cooperate. If 2nd and 3rd round opponent cooperates,
    strategy betrays for the rest of the game. Else uses TitForTat strategy.
    :param decision_history: Opponent's history
    :return: string
    """

    if len(decision_history) < 1:
        return "Defect"
    if len(decision_history) < 4:
        return "Cooperate"

    return "Defect" if decision_history[1] and decision_history[2] == "Cooperate" else tit_for_tat(decision_history)
