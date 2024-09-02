def solution():
    """
    Solution to Project Euler problem 2
    https://projecteuler.net/problem=2

    Find the sum of even-valued Fibonacci terms whose values do not exceed 4 million.
    Start the Fibonacci sequence with 1 and 2.
    """
    print(sum_of_even_fibonacci_lt(4_000_000))


def test_solution():
    assert sum_of_even_fibonacci_lt(4_000_000) == 4_613_730


def sum_of_even_fibonacci_lt(max_term: int) -> int:
    # Let e(n) be the nth ven Fibonacci term
    # e(n) = f(3n-1) by induction on P(k): f(3k-2) is odd and f(3k-1) is even
    # e(n) = 4e(n-1) + e(n-2) by algebra
    # Here, e(1) = f(2) = 2 and e(2) = f(5) = 8
    sum = 0
    prev = 2
    head = 8
    while head <= max_term:
        sum += head
        tmp = head
        head = (4 * head) + prev
        prev = tmp
    return sum
