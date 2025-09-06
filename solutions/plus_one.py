from typing import List


def plus_one(digits: List[int]) -> List[int]:
    i = len(digits) - 1
    print(f"Index: {i}")
    carry = 1
    while i >= 0 and carry:
        print(f"Current index: {i}")
        new_val = digits[i] + carry
        print(f"New value: {new_val}")
        digits[i] = new_val % 10  # dividend - (divisor * quotient ) = remainder 4
        print(f"Remainder: {new_val % 10}")
        carry = (
            new_val // 10
        )  # how many whole times 10 fits into 4? dividend/divisor quotient 0
        print(f"Quotient: {carry}")
        i -= 1

    if carry:  # still have a carry after the loop
        digits.insert(0, carry)
    print(f"Final digits adjusted: {digits}")
    return digits


sample_digits = [9, 9]
plus_one(sample_digits)
