"""Completed solutions for the Final Project 6-7 notebook."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Counter
from numbers import Real
from pathlib import Path
from typing import Iterable


class BankAccount:
    """Manage deposits, withdrawals, and the balance of a bank account."""

    def __init__(self, initial_balance: Real = 0) -> None:
        """Initialize the account with a non-negative balance."""

        self._validate_amount(initial_balance, "initial balance", allow_zero=True)
        self.balance = initial_balance

    @staticmethod
    def _validate_amount(amount: Real, label: str, *, allow_zero: bool = False) -> None:
        """Validate a numeric monetary amount."""

        if isinstance(amount, bool) or not isinstance(amount, Real):
            raise TypeError(f"{label} must be a number")
        if amount < 0 or (amount == 0 and not allow_zero):
            qualifier = "non-negative" if allow_zero else "greater than zero"
            raise ValueError(f"{label} must be {qualifier}")

    def deposit(self, amount: Real) -> Real:
        """Add a positive amount and return the updated balance."""

        self._validate_amount(amount, "deposit amount")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: Real) -> Real:
        """Withdraw a positive amount when sufficient funds are available."""

        self._validate_amount(amount, "withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def check_balance(self) -> Real:
        """Return the current account balance."""

        return self.balance


class Calculator:
    """Perform basic arithmetic operations as instance methods."""

    def __init__(self) -> None:
        """Initialize a calculator with no stored state."""

        pass

    def add(self, a: Real, b: Real) -> Real:
        """Return the sum of two numbers."""

        return a + b

    def subtract(self, a: Real, b: Real) -> Real:
        """Return the difference between two numbers."""

        return a - b

    def multiply(self, a: Real, b: Real) -> Real:
        """Return the product of two numbers."""

        return a * b

    def divide(self, a: Real, b: Real) -> Real | str:
        """Return a divided by b, or a clear message for zero division."""

        if b == 0:
            return "Error! Division by zero."
        return a / b

    def calculator(self, operation: str, a: Real, b: Real) -> Real | str:
        """Dispatch an operation name to the corresponding calculator method."""

        operations = {
            "1": self.add,
            "add": self.add,
            "2": self.subtract,
            "subtract": self.subtract,
            "3": self.multiply,
            "multiply": self.multiply,
            "4": self.divide,
            "divide": self.divide,
        }
        key = operation.strip().lower()
        if key not in operations:
            return "Invalid choice! Please select add, subtract, multiply, or divide."
        return operations[key](a, b)


class Animal(ABC):
    """Abstract base class for animals with a shared description method."""

    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound made by this animal."""

    def describe(self) -> str:
        """Return a general description of the concrete animal."""

        return f"{self.__class__.__name__} is an animal."


class Dog(Animal):
    """Represent a dog."""

    def make_sound(self) -> str:
        """Return the dog's sound."""

        return "Woof"


class Cat(Animal):
    """Represent a cat."""

    def make_sound(self) -> str:
        """Return the cat's sound."""

        return "Meow"


class Cow(Animal):
    """Represent a cow."""

    def make_sound(self) -> str:
        """Return the cow's sound."""

        return "Moo"


class TextFileReader:
    """Read a text file and report its lines, words, and characters."""

    def __init__(self, file_path: str | Path) -> None:
        """Initialize the reader with a path and an empty content buffer."""

        self.file_path = Path(file_path)
        self.content = ""

    def read_file(self) -> str:
        """Read and store the complete UTF-8 file content."""

        self.content = self.file_path.read_text(encoding="utf-8")
        return self.content

    def _ensure_content(self) -> str:
        """Load content on demand before counting or displaying it."""

        if self.content == "":
            self.read_file()
        return self.content

    def count_lines(self) -> int:
        """Return the number of newline-separated lines in the file."""

        return len(self._ensure_content().splitlines())

    def count_words(self) -> int:
        """Return the number of whitespace-separated words."""

        return len(self._ensure_content().split())

    def count_characters(self) -> int:
        """Return the total number of characters, including newlines."""

        return len(self._ensure_content())

    def display_content(self) -> None:
        """Print the stored file content."""

        print(self._ensure_content(), end="")


def count_word_frequency(words: Iterable[str]) -> dict[str, int]:
    """Return the frequency of each unique word in an iterable."""

    return dict(Counter(words))


def read_txt_file(file_path: str | Path) -> str:
    """Read a UTF-8 text file, returning a useful error string on failure."""

    try:
        return Path(file_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except (OSError, UnicodeDecodeError):
        return "Error: An error occurred while reading the file."


class UserExtractor:
    """Extract unique usernames and passwords from ``username:password`` lines."""

    def __init__(self, file_path: str | Path) -> None:
        """Initialize the source path and an empty username dictionary."""

        self.file_path = Path(file_path)
        self.usernames: dict[str, str] = {}

    def extract_usernames(self) -> dict[str, str] | str:
        """Read the file and return a dictionary keyed by unique usernames."""

        content = read_txt_file(self.file_path)
        if content.startswith("Error:"):
            return content

        for line in content.splitlines():
            username, separator, password = line.partition(":")
            if separator and username.strip():
                self.usernames[username.strip()] = password.strip()
        return self.usernames


class Person:
    """Base class for people working or receiving care in a hospital."""

    def __init__(self, name: str, age: int) -> None:
        """Store a person's name and age."""

        self.name = name
        self.age = age

    def view_info(self) -> str:
        """Return basic personal information."""

        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    """Represent a hospital patient and their medical record."""

    def __init__(self, name: str, age: int, medical_record: str) -> None:
        """Store patient details and initialize the shared person fields."""

        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self) -> str:
        """Return the patient's medical record."""

        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    """Represent a hospital staff member and their position."""

    def __init__(self, name: str, age: int, position: str) -> None:
        """Store staff details and initialize the shared person fields."""

        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        """Return staff information including their position."""

        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Department:
    """Group patients and staff members within a hospital department."""

    def __init__(self, name: str) -> None:
        """Store the department name and create empty member lists."""

        self.name = name
        self.patients: list[Patient] = []
        self.staff: list[Staff] = []

    def add_patient(self, patient: Patient) -> None:
        """Add a patient to the department."""

        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        """Add a staff member to the department."""

        self.staff.append(staff_member)


class Hospital:
    """Manage a hospital and its departments."""

    def __init__(self, name: str, location: str) -> None:
        """Store hospital details and initialize its department list."""

        self.name = name
        self.location = location
        self.departments: list[Department] = []

    def add_department(self, department: Department) -> None:
        """Add a department to the hospital."""

        self.departments.append(department)


def demo() -> None:
    """Run a short demonstration for each final-project task."""

    account = BankAccount(100)
    print("Bank account:", account.deposit(50), account.withdraw(30), account.check_balance())

    calculator = Calculator()
    print("Calculator:", calculator.calculator("add", 10, 4))

    print("Animals:")
    for animal in (Dog(), Cat(), Cow()):
        print(animal.describe(), "-", animal.make_sound())

    print("Word frequency:", count_word_frequency(["Welcome", "Ali", "Ali", "Hi"]))

    hospital = Hospital("City Hospital", "123 Main St")
    cardiology = Department("Cardiology")
    cardiology.add_patient(Patient("Alice", 30, "No known allergies"))
    cardiology.add_staff(Staff("Dr. Smith", 45, "Cardiologist"))
    hospital.add_department(cardiology)
    print("Hospital:", hospital.name, "-", hospital.departments[0].name)


if __name__ == "__main__":
    demo()
