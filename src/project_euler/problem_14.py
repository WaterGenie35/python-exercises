def solution():
    """
    Solution to Project Euler problem 14
    https://projecteuler.net/problem=14

    Find a number less than 1_000_000 that has the longest Collatz sequence.
    Let f(k) = { k / 2  if k is even
               { 3k + 1 if k is odd
    Then define the ith term a_i in the Collatz sequence starting with n to be:
      a_i = { n          for i = 1
            { f(a_{i-1}) for i > 1
    """
    print(longest_chain_length_with_starting_num_lt(1_000_000))


def test_solution():
    assert longest_chain_length_with_starting_num_lt(1_000_000) == 837_799


def longest_chain_length_with_starting_num_lt(max_starting_num: int) -> int:
    # With:
    #   - memory optimization (trade space for time)
    #   - chain length of 2k (even) = 1 + chain length of k,
    #     so we can start the search from max_starting_num // 2
    #   - n odd -> 3n+1 even, so -> (3n+1)/2,
    #     so chain length of odd n is 2 + chain length of (3n+1)/2
    longest_chain_length = 0
    starting_num = max_starting_num // 2
    starting_num = 1
    starting_num_with_longest_chain = starting_num
    memory = {}
    while starting_num < max_starting_num:
        chain_length = 1
        head = starting_num
        # Will eventually reach 1 by stipulation
        while head != 1:
            if head % 2 == 0:
                head /= 2
                chain_length += 1
            else:
                head = ((3 * head) + 1) // 2
                chain_length += 2
            if head in memory:
                chain_length += memory[head]
                break
        memory[starting_num] = chain_length
        if chain_length > longest_chain_length:
            longest_chain_length = chain_length
            starting_num_with_longest_chain = starting_num
        starting_num += 1
    return starting_num_with_longest_chain
