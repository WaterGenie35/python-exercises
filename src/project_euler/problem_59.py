import os
from collections.abc import Iterator
from typing import List, Tuple


def solution():
    """
    Solution to Project Euler problem 59
    https://projecteuler.net/problem=59
    """
    print(ascii_sum_of_xor_decrypt(parse_cipher("problem_59_cipher.txt")))


def test_solution():
    assert ascii_sum_of_xor_decrypt(parse_cipher("problem_59_cipher.txt")) == 129_448


def parse_cipher(filename: str) -> List[int]:
    codes = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            codes_str = line.strip().split(",")
            codes.extend([int(code_str) for code_str in codes_str])
    return codes


def ascii_sum_of_xor_decrypt(codes: List[int]) -> int:
    test_words = ["the ", "to ", "of "]
    message = None
    for key in generate_key():
        decrypted_codes = []
        is_valid = True
        for i, code in enumerate(codes):
            decrypted = code ^ key[i % len(key)]
            if decrypted < 0 or decrypted > 255:
                is_valid = False
                break
            decrypted_codes.append(chr(decrypted))
        if not is_valid:
            continue

        message = "".join(decrypted_codes)
        match = True
        for test_word in test_words:
            if message.find(test_word) < 0:
                match = False
                break
        if match:
            break
    return sum([ord(char) for char in message])


def generate_key() -> Iterator[Tuple[int]]:
    start = ord('a')
    end = ord('z')
    for ord_1 in range(start, end + 1):
        for ord_2 in range(start, end + 1):
            for ord_3 in range(start, end + 1):
                yield (ord_1, ord_2, ord_3)
