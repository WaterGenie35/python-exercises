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


# TODO: optimize
def longest_chain_length_with_starting_num_lt(max_starting_num: int) -> int:
    longest_chain_length = 0
    starting_num = 1
    starting_num_with_longest_chain = starting_num
    while starting_num < max_starting_num:
        chain_length = 1
        head = starting_num
        # Will eventually reach 1 by stipulation
        while head != 1:
            if head % 2 == 0:
                head /= 2
            else:
                head = (3 * head) + 1
            chain_length += 1
        if chain_length > longest_chain_length:
            longest_chain_length = chain_length
            starting_num_with_longest_chain = starting_num
        starting_num += 1
    return starting_num_with_longest_chain
