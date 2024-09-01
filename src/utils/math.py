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
