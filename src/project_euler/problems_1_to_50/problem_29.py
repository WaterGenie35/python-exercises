def solution():
    """
    Solution to Project Euler problem 29
    https://projecteuler.net/problem=29

    Find the number of distinct terms in the sequence generated by a^b for
    2 <= a <= 100 and 2 <= b <= 100.
    """
    print(num_distinct_power_terms(2, 100, 2, 100))


def test_solution():
    assert num_distinct_power_terms(2, 5, 2, 5) == 15
    assert num_distinct_power_terms(2, 100, 2, 100) == 9_183


def num_distinct_power_terms(base_min: int, base_max: int, power_min: int, power_max: int) -> int:
    terms = set()
    for base in range(base_min, base_max + 1):
        for power in range(power_min, power_max + 1):
            terms.add(base**power)
    return len(terms)
