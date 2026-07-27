# Universal side-four floors for all line-clean integer budgets

CMR1590--CMR1597 give exact class-specific line-clean slacks.  Their geometric
coefficients still depend on the response side `d`.  This chapter proves that
the three useful permanent ratios are strictly increasing for every `d>=4`.
Their worst values therefore occur at side four, giving simple universal
rational collateral budgets.

These floors close a genuine host-uniform range.  They are weaker than the exact
class budgets, but they require no exponentiation or component analysis and are
valid at every response side.

Put

\[
(d)_3=d(d-1)(d-2).
\]

For the strong, singleton and endpoint-overlap classes define

\[
\rho_{\rm str}(d)=\left(\frac{d-2}{d}\right)^d,
\]

\[
\rho_{\rm sing}(d)
=
\left(\frac{(d-1)(d-3)}{d(d-2)}\right)^d,
\]

and

\[
\rho_{\rm ov}(d)=\left(\frac{d-3}{d}\right)^d.
\]

The exact CMR1591 improvement condition is

\[
\boxed{W_d<D(d)_3\rho(d)}
\]

for the applicable ratio.

## 1. A monotonicity lemma

For fixed `a>0`, define on `x>a`

\[
f_a(x)=x\log\left(1-\frac ax\right).
\]

### Theorem CMR1638 -- PROVED

The function `f_a` is strictly increasing on `(a,infinity)`.
Consequently

\[
\left(1-\frac an\right)^n
\]

is strictly increasing for integers `n>a`.

### Proof

Put `y=a/x`.  Then

\[
f_a'(x)
=
\log(1-y)+\frac{y}{1-y}.
\]

Using the power series on `0<y<1`,

\[
\log(1-y)+\frac{y}{1-y}
=
\sum_{k\ge2}\frac{k-1}{k}y^k>0.
\]

Hence `f_a` is strictly increasing.  Exponentiation preserves the order. ∎

## 2. Strong and overlap ratios

### Theorem CMR1639 -- PROVED

For integers `d>=4`, both `rho_str(d)` and `rho_ov(d)` are strictly increasing.
Their universal floors are

\[
\boxed{\rho_{\rm str}(d)\ge\rho_{\rm str}(4)=\frac1{16}}
\]

and

\[
\boxed{\rho_{\rm ov}(d)\ge\rho_{\rm ov}(4)=\frac1{256}.}
\]

### Proof

Apply CMR1638 with `a=2` and `a=3`.  Evaluate at `d=4`. ∎

## 3. Singleton ratio

Write

\[
\rho_{\rm sing}(d)
=
\left(1-\frac1d\right)^d
\left(1-\frac1{d-2}\right)^d.
\]

### Theorem CMR1640 -- PROVED

The singleton ratio is strictly increasing for integers `d>=4`, and

\[
\boxed{
\rho_{\rm sing}(d)
\ge
\rho_{\rm sing}(4)
=
\left(\frac38\right)^4
=
\frac{81}{4096}.
}
\]

### Proof

The first factor is strictly increasing by CMR1638 with `a=1`.
For the second factor put `n=d-2>=2` and consider

\[
g(n)=\left(1-\frac1n\right)^{n+2}.
\]

For real `x>1`, the derivative of

\[
(x+2)\log(1-1/x)
\]

is

\[
\log(1-1/x)+\frac{x+2}{x(x-1)}.
\]

The inequality

\[
-\log(1-z)\le\frac{z}{1-z}
\qquad(0<z<1)
\]

with `z=1/x` gives the positive lower bound

\[
\frac{2}{x(x-1)}>0.
\]

Thus the second factor is strictly increasing as well.  Their product is
strictly increasing.  Evaluate at `d=4`. ∎

## 4. Universal integer collateral budgets

Let `D>=1` be the destroyed target load and let `W_d` be the common integer
weighted count of CMR1590.

### Theorem CMR1641 -- PROVED

Each of the following is a sufficient host-uniform strict-improvement condition.

### Strong class

\[
\boxed{
W_d
\le
\left\lceil\frac{D(d)_3}{16}\right\rceil-1.
}
\]

### Singleton class

\[
\boxed{
W_d
\le
\left\lceil\frac{81D(d)_3}{4096}\right\rceil-1.
}
\]

### Endpoint-overlap class

\[
\boxed{
W_d
\le
\left\lceil\frac{D(d)_3}{256}\right\rceil-1.
}
\]

### Proof

For a positive real number `x` and integer `W`,

\[
W\le\lceil x\rceil-1
\quad\Longrightarrow\quad
W<x.
\]

Use the three ratio floors from CMR1639--CMR1640 in the exact condition
`W_d<D(d)_3 rho(d)`. ∎

These are universal lower budgets.  The exact CMR1593 budget is always at least
as large and may be substantially larger.

## 5. Universal rank-pure ranges

Assume there are no unavailable response edges, so

\[
W_d=(d-1)(d-2)V_1+(d-2)V_2+V_3.
\]

Let `B_univ` be the appropriate right-hand budget from CMR1641.

### Theorem CMR1642 -- PROVED

Strict improvement is automatic in each rank-pure case whenever

\[
\boxed{
V_1\le
\left\lfloor\frac{B_{\rm univ}}{(d-1)(d-2)}\right\rfloor,
}
\]

\[
\boxed{
V_2\le
\left\lfloor\frac{B_{\rm univ}}{d-2}\right\rfloor,
}
\]

or

\[
\boxed{V_3\le B_{\rm univ}.}
\]

### Proof

Insert the rank-pure form of `W_d` into CMR1641. ∎

The thresholds are not claimed maximal for the exact side-dependent ratio; they
are maximal for the displayed universal floor.

## 6. Unavailable-edge reserve

Write

\[
W_d^{\rm cand}
=(d-1)(d-2)V_1+(d-2)V_2+V_3
\]

and

\[
C_b=(m+1)(d-1)(d-2).
\]

### Theorem CMR1643 -- PROVED

For a universal budget `B_univ`, if

\[
B_{\rm univ}\ge W_d^{\rm cand},
\]

then the line-clean row remains in the automatic range for every integer

\[
\boxed{
0\le b\le
\left\lfloor
\frac{B_{\rm univ}-W_d^{\rm cand}}{C_b}
\right\rfloor.
}
\]

### Proof

The complete weighted count is `W_d=W_d^cand+C_b b`.  Solve
`W_d<=B_univ`. ∎

## 7. Rooted-trace specialization

### Theorem CMR1644 -- PROVED

For a rooted-target trace recurrence, only the strong and singleton universal
budgets are required.  The endpoint-overlap floor `1/256` is never needed in
that subregime.

### Proof

CMR1569--CMR1570 prove that a rooted-target line trace is target-disjoint and
belongs only to the strong or singleton class.  Apply CMR1641. ∎

## 8. Universal-budget endpoint

### Corollary CMR1645 -- PROVED

Every response side `d>=4` now has simple side-independent rational floors for
all three line-clean permanent ratios.  They supply:

1. a universal integer collateral budget;
2. universal rank-pure automatic ranges;
3. a universal unavailable-edge reserve; and
4. a two-class specialization for rooted traces.

The remaining geometric work is to show that the inherited candidate counts and
unavailable-edge count enter one of these universal ranges, or else use the
larger exact side-dependent or component-rook budget.  No all-`n` theorem is
claimed.

Strict monotonicity, side-four minima, destroyed-load budgets and rank-weight
implications are checked through side 500 in
[`scripts/verify_prime_power_line_clean_universal_budget_floors.py`](../scripts/verify_prime_power_line_clean_universal_budget_floors.py).
