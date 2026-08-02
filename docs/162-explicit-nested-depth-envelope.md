# An explicit nested square-root depth envelope

PX265 proves `O(log log t_0)` nested depth but leaves an additive `O(1)` in the
cutoff data.  The recurrence itself gives a direct envelope.  Every nonterminal
generation is either a square-root step, or its next block is already below the
following terminal threshold.  Solving the square-root recurrence removes the
last hidden depth constant.

## 1. Square-root and immediate-terminal alternatives

Retain the PX265 notation

\[
\Delta_j\le\Delta_0+j,
\qquad
b_j=\max\{32,16\Delta_j+4\}.
\]

At a nonterminal generation, `h_j>=b_j` and

\[
t_{j+1}
\le
\max\left\{\frac{\sqrt{t_j}}2,\frac{b_j}2\right\}.
\]

### Theorem PX461 -- PROVED

Every nonterminal generation has one of two forms.

1. **Square-root step:** if `h_j>=b_j^2`, then
   
   \[
   \boxed{t_{j+1}\le\sqrt{t_j}/2.}
   \]
2. **Immediate-terminal step:** if `b_j<=h_j<b_j^2`, then
   
   \[
   \boxed{t_{j+1}\le b_j/2<b_{j+1},}
   \]
   
   so every extracted obstruction at generation `j+1` is quantitatively
   terminal.

### Proof

The first statement is the comparison
`h_j^(-1/2)>=b_j/h_j` from PX265.  In the second range the opposite term defines
`q_j`, giving `t_(j+1)<=b_j/2`.  Since `b_(j+1)>=b_j` and `b_j>0`, the strict
inequality follows.  Any next obstruction has order at most `t_(j+1)`. \(\square\)

Thus a chain contains a sequence of square-root steps followed by at most one
immediate-terminal transition.

## 2. Exact number of square-root steps

Put

\[
y_j=\log_2 t_j.
\]

During square-root steps,

\[
y_{j+1}\le\frac{y_j}{2}-1.
\]

### Theorem PX462 -- PROVED

After `s` consecutive square-root steps,

\[
\boxed{
y_s
\le
\frac{y_0+2}{2^s}-2.
}
\]

Consequently the number of square-root steps in any nonterminal chain is at
most

\[
\boxed{
S(t_0)
=
\left\lceil
\log_2\bigl(\log_2\max\{t_0,2\}+2\bigr)
\right\rceil.
}
\]

### Proof

The displayed recurrence solves by induction:

\[
y_s+2\le2^{-s}(y_0+2).
\]

If `s=S(t_0)`, then `y_s<=-1`.  A nonterminal block has
`t_s>=h_s>=b_s>=32`, hence `y_s>=5`, a contradiction.  The chain must stop
strictly before another square-root step is possible. \(\square\)

The bound is deliberately generous for small `t_0` and valid uniformly.

## 3. Explicit total depth and terminal order

### Corollary PX463 -- PROVED

The number of nonterminal transitions before a quantitatively terminal
obstruction is at most

\[
\boxed{
d_*(t_0)
=
S(t_0)+1.
}
\]

Every terminal obstruction has order less than

\[
\boxed{
B_*(t_0,\Delta_0)
=
\max\left\{
32,
16(\Delta_0+d_*(t_0))+4
\right\}.
}
\]

### Proof

PX462 bounds the square-root transitions.  PX461 permits at most one final
immediate-terminal transition.  At terminal generation `j<=d_*`, the
obstruction order is below `b_j`, which is bounded by the displayed quantity.
\(\square\)

## 4. Explicit cumulative spread

### Theorem PX464 -- PROVED

For the original degree envelope `Delta_j<=Delta_0+j`, the product of optimized
cylinder losses along a chain of length `d` is at most

\[
\boxed{
\exp\left(2d\Delta_0+d(d-1)\right).
}
\]

For paired label restrictions with

\[
\Delta_j^{\rm lab}\le3+2j,
\]

the corresponding product is at most

\[
\boxed{
\exp\left(2d^2+4d\right).
}
\]

Both bounds become explicit after substituting `d=d_*(t_0)`.

### Proof

Multiply the per-generation factors `e^(2Delta_j)` and sum the arithmetic
progression.  In label space,

\[
2\sum_{j<d}(3+2j)
=
6d+2d(d-1)
=
2d^2+4d.
\]

\(\square\)

### Corollary PX465 -- PROVED

The cutoff audit PX453 may use the explicit depth witness

\[
\boxed{
d_*(N)
=
1+
\left\lceil
\log_2\bigl(\log_2\max\{N,2\}+2\bigr)
\right\rceil.
}
\]

No unspecified nested-depth constant remains.  Together with PX460, the only
non-effective cutoff input left in PX455 is an explicit divisor-bound witness
for `mathfrak d(N)=N^(o(1))`.

## 5. Verification

Run

```bash
python scripts/verify_product_explicit_nested_depth.py
```

The verifier exhausts the recurrence over finite integer states, checks the
closed logarithmic formula, validates the immediate-terminal inequality, and
checks both cumulative spread exponents.
