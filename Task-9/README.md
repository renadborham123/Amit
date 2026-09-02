# Task-9: Pandas preprocessing pipeline

This task implements the preprocessing assignment in three reusable pieces:

- `Read_data_file(file_path)` reads a CSV into a pandas DataFrame and gives
  short, useful errors for invalid, missing, empty, unreadable, or malformed
  files.
- `Drop_unnecessary_features(df, cols_to_drop)` removes caller-provided
  columns without embedding Titanic-specific names in the function.
- `Check_data_type(df)` returns a transposed data-quality report with datatype
  and unique-value count for each column.

Dataset-specific choices live in `config.py` (`COLS_TO_DROP`), while
`main.py` runs the complete read-inspect-clean-inspect pipeline.

## Run with the included example

From the repository root:

```bash
python Task-9/main.py Task-9/sample_titanic.csv
```

To save the cleaned result:

```bash
python Task-9/main.py Task-9/sample_titanic.csv --output Task-9/cleaned_titanic.csv
```

Or omit the path and enter it when prompted:

```bash
python Task-9/main.py
```

Install dependencies if needed:

```bash
pip install pandas
```
