from typing import List


def solution():
    """
    Solution to Project Euler problem 76
    https://projecteuler.net/problem=76

    Find the number of ways 100 can be written as a sum of at least 2 positive
    integers.
    """
    print(num_ways_to_sum(5))
    print(num_ways_to_sum(100))


def test_solution():
    assert num_ways_to_sum(5) == 6
    # assert num_ways_to_sum(100) == 190_569_291


# TODO: find a different approach wth better time complexity
def num_ways_to_sum(target: int) -> int:
    # Based on solution from problem 31
    num_ways = 0

    # Count up and carry when the value exceeds the target amount
    num_terms = target - 1
    term_freq = [0] * num_terms
    carry_head = 0
    while carry_head < num_terms:
        current_sum = sum_from_freq(term_freq)

        # Count up
        if current_sum < target:
            # Skip ahead
            term_freq[0] += target - current_sum
            carry_head = 0
            continue

        # Carry
        if current_sum == target:
            num_ways += 1
        if carry_head == num_terms - 1:
            break
        term_freq[carry_head] = 0
        term_freq[carry_head + 1] += 1
        carry_head += 1

    return num_ways


def sum_from_freq(frequencies: List[int]) -> int:
    return sum([(i + 1) * freq for i, freq in enumerate(frequencies)])
