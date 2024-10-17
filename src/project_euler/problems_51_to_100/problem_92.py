def solution():
    """
    Solution to Project Euler problem 92
    https://projecteuler.net/problem=92
    """
    print(nums_digits_squared_chain_ending_in_89_starting_lt(max_starting_num=10_000_000))


# TODO: optimize
# def test_solution():
#     assert nums_digits_squared_chain_ending_in_89_starting_lt(max_starting_num=10_000_000) == 8_581_146


def nums_digits_squared_chain_ending_in_89_starting_lt(max_starting_num: int) -> int:
    count = 0
    group_1 = set([1])
    group_89 = set([89])
    n = 1
    while n < max_starting_num:
        if n in group_89:
            count += 1
            n += 1
            continue

        head = n
        chain = [head]
        while head != 1 and head != 89:
            head = sum_of_digits_squared(head)
            chain.append(head)
            if head in group_1 or head in group_89:
                break
        if head == 89 or head in group_89:
            count += 1
            [group_89.add(num) for num in chain]
        else:
            [group_1.add(num) for num in chain]
        n += 1

    return count


SQUARED = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def sum_of_digits_squared(num: int) -> int:
    total = 0
    n = num
    while n > 0:
        digit = n % 10
        total += SQUARED[digit]
        n //= 10
    return total
