"""Object-oriented solutions for the five exercises in Task-4."""

from __future__ import annotations

from math import isqrt


class MultiplicationTable:
    """Generate a multiplication table for one number.

    Attributes:
        number (int): Number whose table will be generated.
        end (int): Last multiplier included in the table.
    """

    def __init__(self, number: int, end: int = 10) -> None:
        """Store the number and the final multiplier."""

        if end < 1:
            raise ValueError("end must be at least 1")
        self.number = number
        self.end = end

    def generate(self) -> list[str]:
        """Build the multiplication table lines.

        Returns:
            list[str]: Formatted multiplication statements from 1 to ``end``.
        """

        return [
            f"{self.number} * {multiplier} = {self.number * multiplier}"
            for multiplier in range(1, self.end + 1)
        ]


class TwinPrimeFinder:
    """Find pairs of twin primes below a limit.

    Attributes:
        limit (int): Exclusive upper bound for both primes in each pair.
    """

    def __init__(self, limit: int = 1000) -> None:
        """Store the exclusive upper bound for the search."""

        self.limit = limit

    @staticmethod
    def _is_prime(number: int) -> bool:
        """Check whether a number is prime.

        Returns:
            bool: ``True`` when ``number`` has exactly two positive divisors.
        """

        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        return all(number % divisor for divisor in range(3, isqrt(number) + 1, 2))

    def find(self) -> list[tuple[int, int]]:
        """Find all pairs ``(p, p + 2)`` below ``limit``.

        Returns:
            list[tuple[int, int]]: Twin-prime pairs in ascending order.
        """

        return [
            (number, number + 2)
            for number in range(3, self.limit - 2, 2)
            if self._is_prime(number) and self._is_prime(number + 2)
        ]


class PrimeFactorizer:
    """Calculate the repeated prime factors of one integer.

    Attributes:
        number (int): Number to factorize.
    """

    def __init__(self, number: int) -> None:
        """Store the number to factorize."""

        if number < 2:
            raise ValueError("number must be at least 2")
        self.number = number

    def factorize(self) -> list[int]:
        """Return the prime factors, including repeated factors.

        Returns:
            list[int]: Prime factors whose product equals ``number``.
        """

        factors: list[int] = []
        divisor = 2
        remaining = self.number
        while divisor * divisor <= remaining:
            while remaining % divisor == 0:
                factors.append(divisor)
                remaining //= divisor
            divisor = 3 if divisor == 2 else divisor + 2
        if remaining > 1:
            factors.append(remaining)
        return factors


class DecimalToBinary:
    """Convert one decimal integer to a binary string.

    Attributes:
        number (int): Decimal integer to convert.
    """

    def __init__(self, number: int) -> None:
        """Store the decimal integer."""

        if not isinstance(number, int):
            raise TypeError("number must be an integer")
        self.number = number

    def convert(self) -> str:
        """Convert the stored decimal number to binary.

        Returns:
            str: Binary representation without a ``0b`` prefix.
        """

        if self.number == 0:
            return "0"

        sign = "-" if self.number < 0 else ""
        remaining = abs(self.number)
        digits: list[str] = []
        while remaining:
            digits.append(str(remaining % 2))
            remaining //= 2
        return sign + "".join(reversed(digits))


class PerfectNumberFinder:
    """Find perfect numbers in an inclusive range.

    Attributes:
        start (int): First value considered by the search.
        end (int): Last value considered by the search.
    """

    def __init__(self, start: int, end: int) -> None:
        """Store the inclusive search range."""

        if start > end:
            raise ValueError("start must not be greater than end")
        self.start = start
        self.end = end

    @staticmethod
    def _sum_proper_divisors(number: int) -> int:
        """Calculate the sum of a number's proper divisors."""

        if number == 0:
            # The PDF example includes 0 in perfectNums(0, 100).
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

    def find(self) -> list[int]:
        """Find numbers equal to the sum of their proper divisors.

        Returns:
            list[int]: Perfect numbers in the inclusive configured range.
        """

        return [
            number
            for number in range(self.start, self.end + 1)
            if number >= 0 and self._sum_proper_divisors(number) == number
        ]


def main() -> None:
    """Create objects for all five tasks and print their results."""

    table = MultiplicationTable(9)
    print("Multiplication table for 9:")
    for line in table.generate():
        print(line)

    twin_prime_task = TwinPrimeFinder(1000)
    print("\nTwin primes below 1000:")
    for first, second in twin_prime_task.find():
        print(f"{first} and {second}")

    factor_task = PrimeFactorizer(56)
    print("\nPrime factors of 56:")
    print(factor_task.factorize())

    binary_task = DecimalToBinary(11)
    print("\nBinary representation of 11:")
    print(binary_task.convert())

    perfect_task = PerfectNumberFinder(0, 100)
    print("\nPerfect numbers from 0 to 100:")
    for number in perfect_task.find():
        print(number)


if __name__ == "__main__":
    main()
