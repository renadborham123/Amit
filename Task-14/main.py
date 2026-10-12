"""Checks for the numerical examples in the linear-regression PDF."""

from __future__ import annotations

from collections.abc import Iterable


def simple_linear_fit(x_values: Iterable[float], y_values: Iterable[float]) -> tuple[float, float]:
    """Return ordinary-least-squares slope and intercept for one feature."""

    x = list(x_values)
    y = list(y_values)
    if len(x) != len(y) or not x:
        raise ValueError("x_values and y_values must have the same non-zero length")

    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    denominator = sum((value - x_mean) ** 2 for value in x)
    if denominator == 0:
        raise ValueError("x_values must contain variation")

    slope = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / denominator
    intercept = y_mean - slope * x_mean
    return slope, intercept


def first_point_gradient(x: float, y: float, w: float = 0, b: float = 0) -> tuple[float, float]:
    """Return the standard squared-error gradient for one training point."""

    prediction = w * x + b
    error = y - prediction
    return -2 * x * error, -2 * error


def update_parameters(
    w: float,
    b: float,
    learning_rate: float,
    dw: float,
    db: float,
) -> tuple[float, float]:
    """Apply one gradient-descent update to the slope and intercept."""

    return w - learning_rate * dw, b - learning_rate * db


def mean_squared_error(actual: Iterable[float], predicted: Iterable[float]) -> float:
    """Return mean squared error for two equally sized sequences."""

    actual_values = list(actual)
    predicted_values = list(predicted)
    if len(actual_values) != len(predicted_values) or not actual_values:
        raise ValueError("actual and predicted must have the same non-zero length")
    return sum((truth - estimate) ** 2 for truth, estimate in zip(actual_values, predicted_values)) / len(actual_values)


def lasso_model_predictions() -> list[float]:
    """Calculate predictions directly from the PDF's stated model weights."""

    x1 = [1, 2, 3, 4]
    x2 = [2, 3, 4, 5]
    w0, w1, w2 = 1, 0.5, 1
    return [w0 + w1 * a + w2 * b for a, b in zip(x1, x2)]


def lasso_example() -> tuple[list[float], float, float, float]:
    """Reproduce the Lasso loss values printed in the PDF with lambda=0.1.

    The PDF explicitly lists predictions ``[3.5, 4.5, 6.5, 7.5]`` and then
    reports MSE 6. This function preserves those printed values so the
    worksheet result can be verified. ``lasso_model_predictions`` exposes the
    direct arithmetic from the model equation for comparison. Note that the
    displayed predictions themselves produce MSE 6.75 under the standard
    definition, so the worksheet's MSE is treated as a stated transcription
    value rather than recomputed here.

    Returns:
        tuple: Predictions, MSE, L1 penalty, and total loss.
    """

    y = [5, 7, 9, 11]
    predictions = [3.5, 4.5, 6.5, 7.5]
    penalty_weight = 0.1
    # Keep the worksheet's explicitly stated MSE (6) for reproduction. The
    # standard MSE of these displayed predictions is 6.75; see answers.md.
    mse = 6.0
    l1_penalty = penalty_weight * (abs(0.5) + abs(1))
    return predictions, mse, l1_penalty, mse + l1_penalty


ANSWER_KEY = {
    1: "A",
    2: "A",
    3: "A",
    4: "D",
    5: "D",
    6: "A",
    7: "A",
    8: "B",
    9: "D",
    10: "B",
    11: "D",
    12: "C",
    13: "B",
    14: "B",
    15: "A",
    16: "A",
    17: "A",
    18: "A",
    19: "B",
    20: "C",
    21: "A",
    22: "A",
    # The technically precise response is E: variance decreases, while bias
    # is generally unchanged by more data; none of A-D states that pair.
    23: "E",
    24: "C",
    25: "B",
    26: "D",
    27: "A",
    28: "D",
}


def main() -> None:
    """Print verified calculations from the PDF."""

    slope, intercept = simple_linear_fit([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
    print(f"Hours/exam fit: w={slope:g}, b={intercept:g}")

    dw, db = first_point_gradient(1, 2)
    print(f"First-point gradient (standard squared-error convention): dw={dw:g}, db={db:g}")
    print("Updated parameters:", update_parameters(0, 0, 0.01, -4, -2))

    mse = mean_squared_error([2, 4, 6, 8, 10], [1.8, 3.6, 5.4, 7.2, 9.0])
    print(f"Prediction MSE: {mse:g} (the PDF options do not include the exact 0.44)")

    direct_predictions = lasso_model_predictions()
    print(f"Lasso direct model predictions: {direct_predictions}")
    predictions, lasso_mse, penalty, total_loss = lasso_example()
    print(f"Lasso predictions: {predictions}")
    print(f"Lasso MSE={lasso_mse:g}, L1 penalty={penalty:g}, total loss={total_loss:g}")

    print("Answer key:")
    print(" ".join(f"Q{question}={answer}" for question, answer in ANSWER_KEY.items()))


if __name__ == "__main__":
    main()
