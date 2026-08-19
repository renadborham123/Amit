# Task-4

This folder contains solutions for the five function exercises in
`Task4_Functions.pdf`:

1. Print a multiplication table.
2. Find twin primes below a limit.
3. Find repeated prime factors.
4. Convert a decimal integer to binary.
5. Find perfect numbers in an inclusive range.

## Run

From the repository root:

```bash
python Task-4/main.py
```

The script runs the PDF examples: the table for `9`, prime factors of `56`,
binary conversion of `11`, and perfect numbers from `0` through `100`.

The PDF example includes `0` in `perfectNums(0, 100)`, so this solution treats
the proper-divisor sum of `0` as `0` to match that expected output.
