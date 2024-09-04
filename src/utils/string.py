from typing import Dict


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


# https://en.wikipedia.org/wiki/Long_and_short_scales#Comparison
HUMANIZE_POWERS_STEP = {
    3: "thousand",
    6: "million",
    9: "billion",
    12: "trillion",
    15: "quadrillion",
    18: "quintillion",
    21: "sextillion",
    24: "septillion",
    27: "octillion",
    30: "nonillion",
}

HUMANIZE_DIGIT = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

HUMANIZE_TENS_LT_20 = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

HUMANIZE_TENS_GTE_20 = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def humanize_number(n: int, powers_step: Dict[int, str] = HUMANIZE_POWERS_STEP) -> str:
    # Supports up to "nonillion" (10**30) for now
    # E.g. for (12_000_000_345 * 10**30) + 14_011,
    # the 12_000_000_345 will be humanized as as "twelve billion three hundred
    # and forty-five nonillion" (as opposed to twelve duodecillion and three
    # hundred and forty-five nonillion), plus the remaining "fourteen thousand
    # and eleven".
    parts = []
    if n < 10:
        return HUMANIZE_DIGIT[n]

    if n < 20:
        return HUMANIZE_TENS_LT_20[n]

    if n < 100:
        # 21 to 99 separates tenth and unit words with a hyphen
        tenth_digit = n // 10
        parts.append(HUMANIZE_TENS_GTE_20[tenth_digit * 10])

        unit_digit = n % 10
        if unit_digit != 0:
            parts.append(HUMANIZE_DIGIT[unit_digit])

        return "-".join(parts)

    if n < 1_000:
        # 100 to 999 separates hundredth and tenth words with "and"
        hundredth_digit = n // 100
        parts.append(f"{HUMANIZE_DIGIT[hundredth_digit]} hundred")

        remaining_digits = n % 100
        if remaining_digits != 0:
            parts.append(humanize_number(remaining_digits))

        return " and ".join(parts)

    # Separates every 1_000 powers with comma and "and"
    #  - Use oxford comma
    #  - Just "and" with no comma if there's only 1 such power
    powers = sorted(powers_step.keys(), reverse=True)

    largest_step = 10 ** powers[0]
    remaining = n
    if n >= largest_step:
        overflow_digits = n // largest_step
        remaining %= largest_step
        parts.append(f"{humanize_number(overflow_digits, powers_step)} {powers_step[powers[0]]}")

    for power in powers[1:]:
        powerth_digits = remaining // 10**power
        if powerth_digits != 0:
            parts.append(f"{humanize_number(powerth_digits)} {powers_step[power]}")
        remaining %= 10**power

    if remaining != 0:
        parts.append(humanize_number(remaining))

    if len(parts) <= 2:
        return " and ".join(parts)

    non_last_parts = ", ".join(parts[:-1])
    last_part = parts[-1]
    return f"{non_last_parts}, and {last_part}"
