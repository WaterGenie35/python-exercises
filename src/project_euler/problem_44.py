from collections.abc import Iterator

from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 44
    https://projecteuler.net/problem=44

    Find the minimal absolute difference between two different pentagonal
    numbers whose sum and difference are pentagonal.
    The nth pentagonal number is defined by P_n = n(3n-1)/2.
    """
    print(min_abs_diff_pentagonal_with_pentagonal_sum_and_difference())


# def test_solution():
#     assert min_abs_diff_pentagonal_with_pentagonal_sum_and_difference() == 5_482_660


# TODO: math this out instead of just brute force
# TODO: proof on smallest; it is not clear weather the first pair found is also
# the one with minimal difference, so find some identities on P(diff_index)
# and start from smallest
def min_abs_diff_pentagonal_with_pentagonal_sum_and_difference() -> int:
    pentagonals = []
    test_bound = 10_000
    for n in range(1, test_bound):
        p_n = n * ((3 * n) - 1) // 2
        pentagonals.append(p_n)

    for i in range(0, test_bound - 2):
        for j in range(i + 1, test_bound - 1):
            pentagonal_sum = pentagonals[i] + pentagonals[j]
            pentagonal_diff = pentagonals[j] - pentagonals[i]
            sum_index = binary_search(pentagonals, pentagonal_sum)
            diff_index = binary_search(pentagonals, pentagonal_diff)
            if sum_index is not None and diff_index is not None:
                print(f"P({i+1}) = {pentagonals[i]}\tP({j+1}) = {pentagonals[j]}")
                print(f"  sum:  P({sum_index+1}) = {pentagonals[sum_index]}")
                print(f"  diff: P({diff_index+1}) = {pentagonals[diff_index]}")
