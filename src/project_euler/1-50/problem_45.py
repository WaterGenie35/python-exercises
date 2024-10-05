def solution():
    """
    Solution to Project Euler problem 45
    https://projecteuler.net/problem=45

    Find smallest triangle number greater than 40_755 that is also pentagonal
    and hexagonal.
      Triangle: T(n) = n(n+1)/2
      Pentagonal: P(n) = n(3n-1)/2
      Hexagonal: H(n) = n(2n-1)
    """
    print(triangular_pentagonal_hexagonal_number_gt(40_755))


def test_solution():
    assert triangular_pentagonal_hexagonal_number_gt(40_754) == 40_755
    assert triangular_pentagonal_hexagonal_number_gt(40_755) == 1_533_776_805


def triangular_pentagonal_hexagonal_number_gt(lower_bound: int) -> int:
    i = 1
    j = 1
    k = 1
    t_i = 1
    p_j = 1
    h_k = 1
    while t_i <= lower_bound or t_i != p_j or p_j != h_k:
        if t_i <= p_j and t_i <= h_k:
            i += 1
            t_i = i * (i + 1) // 2
        elif p_j <= h_k:
            j += 1
            p_j = j * ((3 * j) - 1) // 2
        else:
            k += 1
            h_k = k * ((2 * k) - 1)

    # TODO: existence proof?
    return t_i
