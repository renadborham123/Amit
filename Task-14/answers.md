# Task-14: Linear Regression Interview Questions

This folder contains the answers and verified calculations for
`Linear Regression Interview Questions_v1.pdf`.

## Multiple-choice answer key

| Question | Answer | Short explanation |
| ---: | :---: | --- |
| 1 | A | Linear regression learns from labelled examples, so it is supervised. |
| 2 | A | Its primary task is predicting a continuous value. |
| 3 | A | A neural network with a linear output unit can represent linear regression. |
| 4 | D | Least squares is standard; maximum likelihood is equivalent under Gaussian noise. |
| 5 | D | Mean Squared Error evaluates continuous predictions. |
| 6 | A | L1/Lasso can drive coefficients exactly to zero for feature selection. |
| 7 | A | Smaller residuals mean predictions are closer to observations. |
| 8 | B | A correlation of -0.95 indicates a strong negative relationship. |
| 9 | D | One one-way statement is not enough to determine a Pearson correlation. |
| 10 | B | More data normally reduces overfitting risk; the statement is false. |
| 11 | D | Normal equations need no learning rate or iterations, but can be slow with many features. |
| 12 | C | With an intercept, ordinary least squares residuals sum to zero in both fits. |
| 13 | B | A very large Ridge penalty increases bias. |
| 14 | B | Ridge coefficients approach zero but generally do not become exactly zero. |
| 15 | A | Lasso can make coefficients exactly zero. |
| 16 | A | Squared error gives outliers disproportionately large influence. |
| 17 | A | Structure in residuals versus predictions indicates model misspecification. |
| 18 | A | Raising degree beyond a perfect degree-3 fit increases overfitting risk. |
| 19 | B | A lower degree may be too simple and underfit the data. |
| 20 | C | Compared with a higher-degree fit, degree 2 has higher bias and lower variance. |
| 21 | A | A descends faster than B and C diverges, so `l2 < l1 < l3`. |
| 22 | A | Training error commonly rises as the training set includes more difficult examples. |
| 23 | E* | Precisely, more data lowers variance while bias is usually approximately unchanged; no A-D pair says that. |
| 24 | C | The plotted points lie exactly on a line, giving RMSE 0. |
| 25 | B | Scenario 2 has the lowest validation error (105). |
| 26 | D | An important feature should reduce both training and validation error. |
| 27 | A | Underfitting calls for more expressive features: more variables and/or polynomial terms. |
| 28 | D | Regularization adds bias, so it is not the remedy for an underfit model. |

`*` The PDF prints option E as “Can't Say False”; the answer above uses the
technically correct interpretation and explains why A-D are not exact.

## Numerical questions

### Hours and exam result

For `(X, Y) = (1,2), (2,4), ..., (5,10)`, the exact line is:

```text
y = 2x + 0
```

Therefore `w = 2` and `b = 0` (option A).

For the first point `(x=1, y=2)` with `w=b=0`, the standard squared-error
gradient is `dw=-4, db=-4`. The PDF's answer choices use a different
single-point convention for the intercept and list `dw=-4, db=-2` (option A);
the distinction is noted rather than hidden.

With `alpha=0.01`, `dw=-4`, and `db=-2`:

```text
w_new = 0 - 0.01(-4) = 0.04
b_new = 0 - 0.01(-2) = 0.02
```

This is option A.

For `y=[2,4,6,8,10]` and `y_pred=[1.8,3.6,5.4,7.2,9.0]`,

```text
MSE = (0.2² + 0.4² + 0.6² + 0.8² + 1.0²) / 5 = 0.44
```

The exact value is `0.44`; none of the printed options contains it. Option C
(`0.4`) is the nearest approximate choice.

A small learning rate is preferred because it avoids overshooting the minimum
(option B).

## Lasso worked example

Using the PDF's data, `lambda=0.1`, and `(w0,w1,w2)=(1,0.5,1)`:

- Predictions: `[3.5, 4.5, 6.5, 7.5]`
- MSE: `6`
- L1 penalty: `0.1 * (|0.5| + |1|) = 0.15`
- Total Lasso loss: `6 + 0.15 = 6.15`

The PDF's displayed predictions are used above to reproduce its stated loss.
However, substituting the displayed weights into its model equation gives
`[3.5, 5.0, 6.5, 8.0]`, not `[3.5, 4.5, 6.5, 7.5]`. The worksheet's `6.15`
loss is therefore a transcription example. In addition, the standard MSE of
the worksheet's displayed predictions is `6.75`, not `6`; `main.py` preserves
the worksheet's stated `6`/`6.15` values and reports the direct model
arithmetic separately.

Answers to the follow-up Lasso/Ridge questions:

1. Lasso's goal is to minimize squared error plus a coefficient penalty (B).
2. Its regularization term is `sum(abs(w_j))` (B).
3. L1 can set weights to zero, performing feature selection (B).
4. In high-dimensional data it selects features and shrinks coefficients (B).
5. A very high Lasso `lambda` drives coefficients toward zero and can underfit (B).
6. Ridge with `lambda=0` becomes ordinary MSE (A).
7. With many correlated features, Lasso is usually more interpretable because it selects a sparse subset (A).
8. For irrelevant/redundant features, prefer Lasso for automatic selection (A).
9. A very high Ridge `lambda` shrinks coefficients too much and underfits (B).
10. For automatic feature selection, prefer Lasso because it can set coefficients exactly to zero (A).

### Proof of the final statement

Lasso minimizes a data-loss term plus

```text
lambda * sum_j |w_j|
```

For a coefficient at zero, the subgradient of `|w_j|` is the interval
`[-1, 1]`. Therefore `w_j = 0` is optimal whenever the data-loss gradient
falls inside `[-lambda, lambda]` after scaling. The L1 term creates this
thresholding behavior: an irrelevant feature can have `w_j=0`, so it is
automatically removed from the model. Ridge uses `lambda * sum_j w_j^2`, whose
gradient shrinks coefficients continuously but does not generally set them
exactly to zero.
