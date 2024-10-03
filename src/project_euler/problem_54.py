import os
from typing import List, Tuple


def solution():
    """
    Solution to Project Euler problem 54
    https://projecteuler.net/problem=54
    """
    print(num_player_1_wins(parse_hands("problem_54_hands.txt")))


def test_solution():
    assert (
        num_player_1_wins(
            [
                (('5H', '5C', '6S', '7S', 'KD'), ('2C', '3S', '8S', '8D', 'TD')),
                (('5D', '8C', '9S', 'JS', 'AC'), ('2C', '5C', '7D', '8S', 'QH')),
                (('2D', '9C', 'AS', 'AH', 'AC'), ('3D', '6D', '7D', 'TD', 'QD')),
                (('4D', '6S', '9H', 'QH', 'QC'), ('3D', '6D', '7H', 'QD', 'QS')),
                (('2H', '2D', '4C', '4D', '4S'), ('3C', '3D', '3S', '9S', '9D')),
            ]
        )
        == 3
    )
    assert num_player_1_wins(parse_hands("problem_54_hands.txt")) == 376


type Hand = Tuple[str, str, str, str, str]


def parse_hands(filename: str) -> List[Tuple[Hand, Hand]]:
    hands = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            cards = line.strip().split(" ")
            player_1_hand = tuple(cards[:5])
            player_2_hand = tuple(cards[5:])
            hands.append((player_1_hand, player_2_hand))
    return hands


def num_player_1_wins(hands: List[Tuple[Hand, Hand]]) -> int:
    num_wins = 0
    for players_hand in hands:
        if winner_of(players_hand) == 1:
            num_wins += 1
    return num_wins


def winner_of(players_hand: Tuple[Hand, Hand]) -> int:
    player_1_evaluation = evaluation_of(players_hand[0])
    player_2_evaluation = evaluation_of(players_hand[1])
    for i in range(5):
        if player_1_evaluation[i] > player_2_evaluation[i]:
            return 1
        if player_2_evaluation[i] > player_1_evaluation[i]:
            return 2
    if player_1_evaluation[5] >= player_2_evaluation[5]:
        return 1
    return 2


def evaluation_of(hand: Hand) -> Tuple[int, int, int, int, int, int]:
    values = sorted([value_of(card[0]) for card in hand], reverse=True)
    highest_value = values[0]
    value_diff = [values[i] - values[i + 1] for i in range(4)]
    is_consecutive = value_diff.count(1) == 4

    suits = [card[1] for card in hand]
    is_same_suit = suits.count(suits[0]) == 5

    # 9: Royal flush
    if is_same_suit and is_consecutive and highest_value == 14:
        return (9, 0, 0, 0, 0, 0)
    # 8: Straight flush
    if is_same_suit and is_consecutive:
        return (8, highest_value, 0, 0, 0, 0)

    freq = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    for card in hand:
        freq[card[0]] += 1

    # 7: Four of a kind
    four_group = [value_of(card) for card, count in freq.items() if count == 4]
    if len(four_group) == 1:
        one_group = [value_of(card) for card, count in freq.items() if count == 1]
        return (7, four_group[0], one_group[0], 0, 0, 0)

    # 6: Full house
    three_group = [value_of(card) for card, count in freq.items() if count == 3]
    two_group = [value_of(card) for card, count in freq.items() if count == 2]
    if len(three_group) == 1 and len(two_group) == 1:
        return (6, three_group[0], two_group[0], 0, 0, 0)

    # 5: Flush
    if is_same_suit:
        return (5, *values)

    # 4: Straight
    if is_consecutive:
        return (4, *values)

    # 3: Three of a kind
    if len(three_group) == 1:
        remaining_values = [value for value in values if value != three_group[0]]
        return (3, three_group[0], *remaining_values, 0, 0)

    # 2: Two pairs
    if len(two_group) == 2:
        remaining_values = [value for value in values if value not in two_group]
        return (2, max(two_group), min(two_group), remaining_values[0], 0, 0)

    # 1: One pair
    if len(two_group) == 1:
        remaining_values = [value for value in values if value != two_group[0]]
        return (1, two_group[0], *remaining_values, 0)

    # 0: High card
    return (0, *values)


def value_of(card: str) -> int:
    if card == 'T':
        return 10
    if card == 'J':
        return 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14
    return int(card)
