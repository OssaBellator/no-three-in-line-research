# The singleton line-clean exception has an optimal fractional factor

CMR1542--CMR1549 classify line-clean traces into a strong `(d-2)`-factor class
and a weak class.  The weak class has two different mechanisms:

1. target-endpoint overlap, where one allowed-graph vertex really has degree
   `d-3`;
2. a target-disjoint singleton remainder, where the `(d-2)` Hall condition
   fails by exactly one edge.

The second mechanism is much less severe.  Its optimal fractional factor value
is

\[
d-2-\frac1{d-2}
=
\frac{(d-1)(d-3)}{d-2}.
\]

This chapter proves the exact capacity, derives an intermediate permanent
coefficient, and upgrades the line-clean signature from binary to ternary.

Normalize

\[
O=\{(i,i):0\le i<d\},
\qquad d\ge4,
\]

let `e notin O`, and let `X` be a target-disjoint deleted trace such that

\[
Y=X\cup\{e\}
\]

is a partial matching of size `d-1`.  Assume its unique unmatched source and
target have the same label `w`.  Thus `(w,w) in O` is the sole residual edge and
CMR1543 cannot extend `Y` to a perfect matching disjoint from `O`.

Put

\[
G=K_{d,d}\setminus(O\cup Y).
\]

## 1. Exact deficient cut and optimal capacity upper bound

Define

\[
q_{\rm sing}
=
\frac{(d-1)(d-3)}{d-2}
=
d-2-\frac1{d-2}.
\]

### Theorem CMR1550 -- PROVED

Let

\[
A=L\setminus\{w\},
\qquad
B=\{w\}.
\]

Then

\[
\boxed{
|E(G)\cap(A\times(R\setminus B))|
=(d-1)(d-3).
}
\]

Consequently every fractional factor on `G` whose edge weights are at most one
and whose common vertex sum is `q` satisfies

\[
\boxed{q\le q_{\rm sing}.}
\]

### Proof

The rectangle has `(d-1)^2` cells.  The opposite matching contributes `d-1`
forbidden edges and the near-perfect matching `Y` contributes another `d-1`.
They are disjoint.  This gives the crossing count.

For any fractional `q`-factor, total weight leaving `A` is `q(d-1)`.  At most
`q` enters the single target vertex in `B`, so at least `q(d-2)` must cross to
`R\setminus B`.  Unit edge capacities give

\[
q(d-2)\le(d-1)(d-3).
\]

Rearrange. ∎

Thus the one-edge Hall deficit determines the exact possible capacity.

## 2. Every capacitated cut supports `q_sing`

Let `A_0` be any source set and `B_0` any target set with

\[
x=|A_0|>|B_0|,
\qquad
z=d-|B_0|.
\]

Put

\[
m=\min\{x,z\},
\qquad
M=\max\{x,z\}.
\]

### Theorem CMR1551 -- PROVED

\[
\boxed{
|E(G)\cap(A_0\times(R\setminus B_0))|
\ge
q_{\rm sing}(x-|B_0|).
}
\]

### Proof

The forbidden graph is the union of the two matchings `O` and `Y`.  Hence the
crossing rectangle loses at most `2m` cells and contains at least

\[
m(M-2)
\]

allowed edges.

Set

\[
\alpha=d-M,
\qquad
\beta=d-m.
\]

Then `0<=alpha<=beta` and `alpha+beta<d`.  For the larger comparison value
`d-2`, the difference between the allowed-edge lower bound and the required
cut weight is

\[
\alpha(\beta-2).
\]

This is nonnegative except possibly when `alpha=beta=1`, where it equals `-1`.
Replacing `d-2` by

\[
q_{\rm sing}=(d-2)-\frac1{d-2}
\]

reduces the required right side by

\[
\frac{x-|B_0|}{d-2}.
\]

In the sole bad size case `alpha=beta=1`, one has

\[
x-|B_0|=d-2,
\]

so the reduction is exactly one and repairs the deficit.  In all other cases
the `(d-2)` comparison was already valid. ∎

## 3. Scaled integral flow certificate

### Theorem CMR1552 -- PROVED

There are rational edge weights

\[
0\le z_f\le1
\qquad(f\in E(G))
\]

such that every source and target vertex has incident weight exactly

\[
\boxed{q_{\rm sing}.}
\]

Moreover the weights may be chosen with denominator dividing `d-2`.

### Proof

Scale all weights by `d-2`.  Use a bipartite flow network with:

- source-to-left demand and capacity
  \[
  Q=(d-1)(d-3);
  \]
- allowed-edge capacity `d-2`;
- right-to-sink demand and capacity `Q`.

The max-flow cut condition is exactly CMR1551 multiplied by `d-2`.  Therefore a
flow of value `dQ` exists.  Integral capacities give an integral maximum flow.
Divide each allowed-edge flow by `d-2`. ∎

Dividing these weights by `q_sing` gives a doubly stochastic matrix supported on
`G`, with every entry at most `1/q_sing`.

## 4. Intermediate permanent denominator

### Theorem CMR1553 -- PROVED

The singleton-exception response family satisfies

\[
\boxed{
|\operatorname{PM}(G)|
\ge
 d!\left(\frac{q_{\rm sing}}d\right)^d.
}
\]

### Proof

Let `Z` be the fractional factor matrix of CMR1552.  Then `Z/q_sing` is doubly
stochastic.  Van der Waerden gives

\[
\operatorname{per}(Z/q_{\rm sing})
\ge
\frac{d!}{d^d}.
\]

Every perfect-matching monomial of `Z` is at most one, and nonzero monomials are
supported on perfect matchings of `G`.  Hence

\[
\operatorname{per}(Z)
\le
|\operatorname{PM}(G)|.
\]

Multiply by `q_sing^d`. ∎

Equivalently the singleton coefficient is

\[
\boxed{
\kappa_d^{\rm sing}
=
\left(
\frac{d(d-2)}{(d-1)(d-3)}
\right)^d.
}
\]

It lies strictly between the strong and endpoint-overlap coefficients:

\[
\left(\frac d{d-2}\right)^d
<
\kappa_d^{\rm sing}
<
\left(\frac d{d-3}\right)^d.
\]

## 5. Prescription and collateral bounds

Let `P` be a compatible allowed prescription of rank `1<=r<=3`, and let `R` be
uniform on `PM(G)`.

### Theorem CMR1554 -- PROVED

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\kappa_d^{\rm sing}}{(d)_r}.
}
\]

If

\[
\mathcal C_{off}^{line}
=
\frac{V_1^{off}}d
+
\frac{V_2^{off}}{(d)_2}
+
\frac{V_3^{off}}{(d)_3},
\]

then

\[
\boxed{
\mathbb E N_{off}(R)
\le
\kappa_d^{\rm sing}\mathcal C_{off}^{line}.
}
\]

### Proof

At most `(d-r)!` complete matchings contain `P`.  Divide by CMR1553 and sum the
resulting prescription bounds by rank. ∎

## 6. Restricted-host improvement criterion

### Theorem CMR1555 -- PROVED

Let `b` line-clean allowed edges be unavailable and let the current potential be
`m`.  If

\[
\boxed{
\kappa_d^{\rm sing}
\left[
\mathcal C_{off}^{line}
+
\frac{(m+1)b}{d}
\right]
<
D_S(e),
}
\]

then some singleton-exception line-clean response is feasible and has strictly
smaller potential.

### Proof

Use the rank-one case of CMR1554 for unavailable-edge use and repeat the
integer penalty argument of CMR1540. ∎

## 7. Exact ternary line-clean coefficient

### Theorem CMR1556 -- PROVED

Every line-clean trace belongs to exactly one coefficient class.

1. **Strong derangement-extendable trace**
   \[
   \kappa_d^{(2)}
   =
   \left(\frac d{d-2}\right)^d.
   \]
2. **Target-disjoint singleton trace**
   \[
   \kappa_d^{\rm sing}
   =
   \left(
   \frac{d(d-2)}{(d-1)(d-3)}
   \right)^d.
   \]
3. **Target-endpoint-overlap trace**
   \[
   \kappa_d^{(3)}
   =
   \left(\frac d{d-3}\right)^d.
   \]

### Proof

CMR1542--CMR1544 give the strong class, the singleton class, and the endpoint-
overlap class.  CMR1545--CMR1547 give the outer coefficients; CMR1553--CMR1555
give the middle one.  The classes are disjoint and exhaustive. ∎

The exact CMR1533 component-rook ratio may improve any of the three uniform
coefficients.

## 8. Singleton fractional-factor endpoint

### Corollary CMR1557 -- PROVED

The only target-disjoint failure of a spanning `(d-2)`-factor has an optimal
fractional factor value

\[
\boxed{
q_{\rm sing}
=d-2-\frac1{d-2}.
}
\]

Its permanent and prescription losses are therefore intermediate, not as severe
as target-endpoint overlap.  The line-clean destroyed-credit frontier now has
three exact finite signatures and corresponding host-uniform rational
coefficients.

What remains is to compare each coefficient, or its exact component sharpening,
with destroyed target load and then combine those rows with return, persistent-
selector, trace and root/fixed-interface coefficients.  No all-`n` theorem is
claimed.

Scaled fractional flows, exact cut capacities, permanent bounds and
prescription ratios are checked in
[`scripts/verify_prime_power_line_clean_singleton_fractional.py`](../scripts/verify_prime_power_line_clean_singleton_fractional.py).
