from utils.prime_table import PRIMES
from utils.search import binary_search


def test_binary_search():
    assert binary_search([], 1) is None
    assert binary_search([1], 1) == 0
    assert binary_search([1, 2], 1) == 0
    assert binary_search([1, 2], 2) == 1
    assert binary_search([2, 5, 7, 10, 13, 200], 13) == 4
    assert binary_search([2, 5, 7, 10, 13, 200], 12) is None
    assert binary_search(PRIMES, 65_325) is None
    assert binary_search(PRIMES, 65_327) == 6_525
