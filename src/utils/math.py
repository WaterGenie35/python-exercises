from typing import List


# TODO: optimize
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    factor = 3
    while factor**2 <= n:
        if n % factor == 0:
            return False
        factor += 2
    return True


# TODO: optimize
def nth_prime(n: int) -> int:
    if n == 1:
        return 2
    i = 2
    head = 3
    while i < n:
        head += 2
        if is_prime(head):
            i += 1
    return head


# TODO: optimize? see problem 12
def divisors_of(n: int) -> List[int]:
    divisors = []
    pairs = []
    head = 1
    while head**2 <= n:
        if n % head == 0:
            divisors.append(head)
            factor_pair = n / head
            if head != factor_pair:
                pairs.append(factor_pair)
        head += 1
    divisors.extend(reversed(pairs))
    return divisors


def choose(n: int, k: int) -> int:
    product = 1
    bound = min(k, n - k) + 1
    for i in range(1, bound):
        product *= (n + 1.0 - i) / i
    return round(product)
