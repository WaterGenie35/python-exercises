from utils.math import choose


def solution():
    """
    Solution to Project Euler problem 53
    https://projecteuler.net/problem=53

    How many of n choose r are greater than 1_000_000 for 1 <= n <= 100 and
    r <= n?
    """
    print(num_n_choose_r_gt(min_n=1, max_n=100, gt=1_000_000))


def test_solution():
    assert num_n_choose_r_gt(min_n=1, max_n=100, gt=1_000_000) == 4_075


def num_n_choose_r_gt(min_n: int, max_n: int, gt: int) -> int:
    num_gt = 0
    for n in range(min_n, max_n + 1):
        for r in range(1, (n // 2) + 1):
            n_choose_r = choose(n, r)
            if n_choose_r > gt:
                num_gt += 2 if r < n - r else 1
    return num_gt
