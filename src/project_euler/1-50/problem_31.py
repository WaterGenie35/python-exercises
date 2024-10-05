from typing import List

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def solution():
    """
    Solution to Project Euler problem 31
    https://projecteuler.net/problem=31

    Find the number of ways 2 GBP can be made using any number of coins.
    The coins are:
      1p, 2p, 5p, 10p, 20p, 50p, 1 GBP, and 2 GBP
      where 100p = 1 GBP
    """
    print(num_ways_to_coin(pence=200))


def test_solution():
    assert num_ways_to_coin(pence=5) == 4
    assert num_ways_to_coin(pence=200) == 73_682

    assert num_ways_to_coin(pence=2, coins=[3, 4, 5]) == 0
    assert num_ways_to_coin(pence=6, coins=[1, 2, 5]) == 5
    assert num_ways_to_coin(pence=6, coins=[1, 2, 5, 10]) == 5


def num_ways_to_coin(pence: int, coins: List[int] = COINS) -> int:
    if coins[0] > pence:
        return 0

    # Count up in coin-ary and carry when the value exceeds the target amount
    num_ways = 0
    num_coins = len(coins)
    coin_freq = [0] * num_coins
    carry_head = 0
    while carry_head < num_coins:
        amount = amount_from_freq(coins, coin_freq)

        # Count up
        if amount < pence:
            # Skip ahead
            coin_freq[0] += (pence - amount) // coins[0]
            carry_head = 0
            continue

        # Carry
        if amount == pence:
            num_ways += 1
        if carry_head == num_coins - 1:
            break
        coin_freq[carry_head] = 0
        coin_freq[carry_head + 1] += 1
        carry_head += 1

    return num_ways


def amount_from_freq(coins: List[int], frequencies: List[int]) -> int:
    return sum([coin * freq for coin, freq in zip(coins, frequencies)])
