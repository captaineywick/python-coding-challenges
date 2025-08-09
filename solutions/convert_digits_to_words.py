def convert_num_to_words(num: int, words: str = "") -> str:
    if num == 0:
        return words.strip()

    small_units = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    mid_units = {
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
    }
    large_units = {1_000_000_000: "Billion", 1_000_000: "Million", 1_000: "Thousand"}
    if num < 20:
        return (words + small_units[num] + " ").strip()

    elif num < 100:
        tens = (num // 10) * 10
        remainder = num % 10
        words += mid_units[tens] + " "
        if remainder:
            words += small_units[remainder] + " "
        return words.strip()

    for value, word in large_units.items():
        if num >= value:
            count = num // value
            words = convert_num_to_words(count, words) + f" {word} "
            remainder = num % value
            if remainder:
                words = convert_num_to_words(remainder, words)
            return words.strip()

    # handle hundreds
    hundreds = num // 100
    remainder = num % 100
    words += small_units[hundreds] + " Hundred "
    if remainder:
        words = convert_num_to_words(remainder, words)
    return words.strip()


sample_numbers = [
    0,
    1086,
    112,
    21,
    16,
    99,
    1_000_100,
    1_116_000_123,
    999_999_999_999,
]
for n in sample_numbers:
    print(convert_num_to_words(n))
