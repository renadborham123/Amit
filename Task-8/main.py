"""NumPy solutions for Task-8."""

from __future__ import annotations

from numbers import Integral
from typing import Any

import numpy as np


def _validated_shape(shape: Any, *, identity: bool = False) -> int | tuple[int, ...]:
    """Validate a NumPy shape and normalize it to an int or tuple."""

    if isinstance(shape, Integral) and not isinstance(shape, bool):
        normalized = int(shape)
        if normalized < 0:
            raise ValueError("shape dimensions cannot be negative")
        return normalized

    if isinstance(shape, (tuple, list)):
        if not shape:
            raise ValueError("shape must contain at least one dimension")
        dimensions = tuple(int(dimension) for dimension in shape)
        if any(dimension < 0 for dimension in dimensions):
            raise ValueError("shape dimensions cannot be negative")
        if identity:
            if len(dimensions) != 2 or dimensions[0] != dimensions[1]:
                raise ValueError("identity mode requires a square shape or an integer size")
            return dimensions[0]
        return dimensions

    raise ValueError("shape must be an integer or a tuple/list of integers")


def array_factory(mode: str, shape: int | tuple[int, ...], value: Any = None) -> np.ndarray:
    """Create a NumPy array according to a requested factory mode.

    Args:
        mode: One of ``zeros``, ``ones``, ``full``, or ``identity``.
        shape: Array shape for the first three modes, or matrix size for
            ``identity``. A square tuple is also accepted for ``identity``.
        value: Fill value required by the ``full`` mode.

    Returns:
        numpy.ndarray: The generated array.

    Raises:
        ValueError: If the mode, shape, or required fill value is invalid.
    """

    if not isinstance(mode, str):
        raise ValueError("mode must be a string")
    normalized_mode = mode.strip().lower()

    if normalized_mode == "identity":
        normalized_shape = _validated_shape(shape, identity=True)
    else:
        normalized_shape = _validated_shape(shape)

    if normalized_mode == "zeros":
        return np.zeros(normalized_shape)
    if normalized_mode == "ones":
        return np.ones(normalized_shape)
    if normalized_mode == "full":
        if value is None:
            raise ValueError("full mode requires a value")
        return np.full(normalized_shape, value)
    if normalized_mode == "identity":
        return np.eye(normalized_shape)

    raise ValueError(
        "unsupported mode; choose 'zeros', 'ones', 'full', or 'identity'"
    )


def secure_reshape_and_stack(
    data1: Any,
    data2: Any,
    new_shape: tuple[int, int] | list[int],
) -> np.ndarray:
    """Reshape one dataset and vertically stack it with a second dataset.

    Inputs are converted to NumPy arrays before reshaping. A one-dimensional
    second dataset is treated as one row so it can be stacked with the first
    matrix. Shape and column mismatches are exposed as a consistent,
    company-grade ``ValueError`` message.

    Args:
        data1: Values to reshape into a two-dimensional matrix.
        data2: Existing one- or two-dimensional dataset to append vertically.
        new_shape: Two-dimensional shape for the first dataset.

    Returns:
        numpy.ndarray: The vertically combined matrix.

    Raises:
        ValueError: If conversion, reshape, or vertical stacking fails.
    """

    try:
        arr1 = np.asarray(data1)
        arr2 = np.asarray(data2)

        if arr1.ndim == 0 or arr2.ndim == 0:
            raise ValueError("both datasets must contain at least one dimension")

        if len(new_shape) != 2:
            raise ValueError("new_shape must contain exactly two dimensions")
        reshaped_arr1 = arr1.reshape(tuple(new_shape))

        if reshaped_arr1.ndim != 2:
            raise ValueError("reshaped data1 must be a two-dimensional matrix")
        if arr2.ndim == 1:
            arr2 = arr2.reshape(1, -1)
        elif arr2.ndim != 2:
            raise ValueError("data2 must be one- or two-dimensional")

        combined_dataset = np.vstack((reshaped_arr1, arr2))
        return combined_dataset
    except (TypeError, ValueError) as error:
        raise ValueError(f"Company-grade Error: {error}") from error


def main() -> None:
    """Run the examples represented in the assignment image."""

    print("Array factory examples:")
    print(array_factory("zeros", (2, 3)))
    print(array_factory("ones", (2, 2)))
    print(array_factory("full", (2, 2), value=7))
    print(array_factory("identity", 3))

    data1 = [1, 2, 3, 4, 5, 6]
    data2 = [[7, 8, 9], [10, 11, 12]]
    print("\nSecure reshape and stack:")
    print(secure_reshape_and_stack(data1, data2, (2, 3)))


if __name__ == "__main__":
    main()
