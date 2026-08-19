"""Solutions for Task-4: Python functions practice."""

from __future__ import annotations

from math import isqrt


def multiplication_table(number: int, end: int = 10) -> list[str]:
    """Print and return the multiplication table from 1 through ``end``."""

    if end < 1:
        raise ValueError("end must be at least 1")

    lines = [f"{number} * {multiplier} = {number * multiplier}" for multiplier in range(1, end + 1)]
    for line in lines:
        print(line)
    return lines


def is_prime(number: int) -> bool:
    """Return whether ``number`` is prime."""

    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def twin_primes(limit: int = 1000) -> list[tuple[int, int]]:
    """Print and return prime pairs ``(p, p + 2)`` below ``limit``."""

    if limit <= 3:
        return []

    pairs = [
        (number, number + 2)
        for number in range(3, limit - 2, 2)
        if is_prime(number) and is_prime(number + 2)
    ]
    for first, second in pairs:
        print(f"{first} and {second}")
    return pairs


def prime_factors(number: int) -> list[int]:
    """Return the prime factors of ``number``, including repeated factors."""

    if number < 2:
        raise ValueError("number must be at least 2")

    factors: list[int] = []
    divisor = 2
    remaining = number
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2

    if remaining > 1:
        factors.append(remaining)
    return factors


def decimal_to_binary(number: int) -> str:
    """Convert a decimal integer to its binary representation."""

    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number == 0:
        return "0"

    sign = "-" if number < 0 else ""
    remaining = abs(number)
    digits: list[str] = []
    while remaining:
        digits.append(str(remaining % 2))
        remaining //= 2
    return sign + "".join(reversed(digits))


def sum_proper_divisors(number: int) -> int:
    """Return the sum of proper divisors of ``number``."""

    if number == 0:
        # This convention matches the PDF example, which includes 0 in
        # perfectNums(0, 100).
        return 0
    if number == 1:
        return 0

    total = 1
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            total += divisor
            paired_divisor = number // divisor
            if paired_divisor != divisor:
                total += paired_divisor
    return total


def is_perfect(number: int) -> bool:
    """Return whether ``number`` is perfect under the PDF's definition."""

    return number >= 0 and sum_proper_divisors(number) == number


def perfect_numbers(start: int, end: int) -> list[int]:
    """Print and return perfect numbers in the inclusive range."""

    if start > end:
        raise ValueError("start must not be greater than end")

    numbers = [number for number in range(start, end + 1) if is_perfect(number)]
    for number in numbers:
        print(number)
    return numbers


def main() -> None:
    """Run the examples shown in Task4_Functions.pdf."""

    print("Multiplication table for 9:")
    multiplication_table(9)

    print("\nTwin primes below 1000:")
    twin_primes(1000)

    print("\nPrime factors of 56:")
    print(prime_factors(56))

    print("\nBinary representation of 11:")
    print(decimal_to_binary(11))

    print("\nPerfect numbers from 0 to 100:")
    perfect_numbers(0, 100)


if __name__ == "__main__":
    main()
