# Line-clean hosts have an exact `(d-2)`-factor signature

CMR1534--CMR1541 give a universal spanning `(d-3)`-factor in every extension-
free line-clean host.  That bound is sharp when the target edge and deleted
trace overload one endpoint, but many traces retain the stronger `(d-2)`
permanent denominator of the undeleted extension-free bank.

The exact distinction is finite.  Adjoin the target edge to the deleted trace.
If the union is a partial matching which extends to a perfect matching disjoint
from the opposite layer, its complement supplies a spanning `(d-2)`-regular
subgraph.  Failure has only two forms:

1. the trace already uses a target endpoint; or
2. the target-plus-trace matching leaves one unmatched source and one unmatched
   target joined by the opposite matching.

This chapter proves the dichotomy and attaches the correct permanent coefficient
to every line-clean rook signature.

Fix `d>=4`, normalize the opposite matching as

\[
O=\{(i,i):0\le i<d\},
\]

fix `e=(u,v) notin O`, and let

\[
X\subseteq E(H_e)
\]

be the deleted partial matching.  Put

\[
Y=X\cup\{e\},
\qquad
G=K_{d,d}\setminus(O\cup Y).
\]

## 1. Target compatibility of the deleted trace

### Theorem CMR1542 -- PROVED

The union `Y=X union {e}` is a partial matching if and only if no edge of `X`
uses source `u` or target `v`.

### Proof

The trace `X` is already a partial matching and does not contain `e`.  Adding
`e=(u,v)` preserves the matching property exactly when neither endpoint is
already used. ∎

Call this the **target-disjoint trace** case.

## 2. Exact derangement-extension criterion

Assume `Y` is a partial matching disjoint from `O`.  Let `A` and `B` be its
unmatched source and target sets, with

\[
|A|=|B|=m.
\]

### Theorem CMR1543 -- PROVED

The partial matching `Y` extends to a perfect matching `Y'` disjoint from `O`
except in exactly one case:

\[
\boxed{
m=1
\quad\text{and}\quad
A=B=\{w\}
}
\]

for some label `w`.  Equivalently, the sole residual edge is the forbidden
opposite edge `(w,w)`.

### Proof

If `m=0`, `Y` is already perfect.

If `m=1`, the extension uses the unique residual edge between the unmatched
source and target.  It is allowed exactly when those labels differ.

Assume `m>=2`.  The residual completion graph is the complete bipartite graph
on `A,B` with the surviving diagonal edges of `O` removed.  A singleton source
has at least `m-1>=1` neighbours.  If `S subseteq A` has at least two vertices,
then every target in `B` is adjacent to some member of `S`, because at most one
source can forbid that target's diagonal edge.  Thus

\[
|N(S)|=m\ge|S|.
\]

Hall's theorem gives a perfect residual matching disjoint from `O`.  Adjoin it
to `Y`. ∎

The exceptional case can occur only when `|Y|=d-1`, or equivalently
`|X|=d-2`.

## 3. Exact strong-factor dichotomy

### Theorem CMR1544 -- PROVED

The line-clean allowed graph `G` contains a spanning `(d-2)`-regular subgraph if
and only if both conditions hold:

1. `X` is target-disjoint in the sense of CMR1542;
2. the singleton opposite-edge exception of CMR1543 does not occur.

Otherwise `G` has no spanning `(d-2)`-factor, while CMR1536 still supplies a
spanning `(d-3)`-factor.

### Proof

In the positive case, CMR1543 gives a perfect matching `Y'` such that

\[
Y\subseteq Y',
\qquad
Y'\cap O=\varnothing.
\]

Then

\[
J=K_{d,d}\setminus(O\cup Y')
\]

is `(d-2)`-regular and satisfies `J subseteq G`.

If `X` uses source `u` or target `v`, that shared vertex is incident with three
distinct forbidden edges: one from `O`, one from `X`, and `e`.  Its degree in
`G` is `d-3`, so no spanning `(d-2)`-factor exists.

It remains to treat the singleton exception.  Let `w` be the unique unmatched
source and target of `Y`; thus `Y` matches every other source into every other
target.  Take

\[
A=L\setminus\{w\},
\qquad
B=\{w\}.
\]

Inside

\[
A\times(R\setminus B)
\]

both `O` and `Y` contribute `d-1` forbidden edges.  Hence the allowed crossing
size is

\[
(d-1)^2-2(d-1)=(d-1)(d-3).
\]

A `(d-2)`-factor would require at least

\[
(d-2)(|A|-|B|)=(d-2)^2
\]

crossing edges.  The former number is one smaller, so the capacitated Hall
condition fails. ∎

Thus the factor signature is exact, not merely sufficient.

## 4. Sharpened permanent denominator

Define

\[
q_X=
\begin{cases}
 d-2,&\text{in the CMR1544 strong-factor case},\\
 d-3,&\text{otherwise},
\end{cases}
\]

and

\[
\kappa_d(X,e)
=
\left(\frac d{q_X}\right)^d.
\]

### Theorem CMR1545 -- PROVED

\[
\boxed{
|\operatorname{PM}(G)|
\ge
 d!\left(\frac{q_X}{d}\right)^d.
}
\]

### Proof

CMR1544 gives a spanning `q_X`-regular subgraph.  Divide its adjacency matrix by
`q_X`, apply van der Waerden, and retain its perfect matchings inside `G`, as in
CMR1537. ∎

In the strong-factor case this recovers

\[
\boxed{
|\operatorname{PM}(G)|
\ge
 d!\left(\frac{d-2}{d}\right)^d,
}
\]

which is the same uniform denominator as the undeleted extension-free bank.

## 5. Sharpened prescription probabilities

Let `P` be a compatible allowed prescription of rank `1<=r<=3`, and let `R` be
uniform on `PM(G)`.

### Theorem CMR1546 -- PROVED

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\kappa_d(X,e)}{(d)_r}.
}
\]

### Proof

At most `(d-r)!` complete matchings contain `P`.  Divide by CMR1545. ∎

Thus every line-clean trace has one of only two host-uniform probability
coefficients:

\[
\boxed{
\left(\frac d{d-2}\right)^d
\quad\text{or}\quad
\left(\frac d{d-3}\right)^d.
}
\]

## 6. Two-level collateral and restricted-host criteria

Let

\[
\mathcal C_{off}^{line}
=
\frac{V_1^{off}}d
+
\frac{V_2^{off}}{(d)_2}
+
\frac{V_3^{off}}{(d)_3}.
\]

### Theorem CMR1547 -- PROVED

For the uniform line-clean response associated with trace `X`,

\[
\boxed{
\mathbb E N_{off}(R)
\le
\kappa_d(X,e)\mathcal C_{off}^{line}.
}
\]

If `b` allowed line-clean edges are unavailable and the current potential is
`m`, then

\[
\boxed{
\kappa_d(X,e)
\left[
\mathcal C_{off}^{line}
+
\frac{(m+1)b}{d}
\right]
<
D_S(e)
}
\]

forces one feasible strict-improvement response.

### Proof

Sum CMR1546 over corrected residual prescriptions.  For unavailable edges use
the rank-one case and repeat the feasibility-forcing argument of CMR1540. ∎

## 7. Geometric sufficient classes for the stronger coefficient

### Theorem CMR1548 -- PROVED

A target-disjoint deleted line trace `X` lies in the strong `(d-2)`-factor class
whenever at least one of the following holds:

1. `|X|<=d-3`;
2. `|X|=d-1`;
3. `|X|=d-2` and the unique unmatched source and target of `X union {e}` are
   not joined by `O`.

The only target-disjoint weak class has `|X|=d-2` and one residual opposite
edge.  Every target-endpoint overlap is also weak.

### Proof

Apply CMR1543.  In branch 1 the residual completion side is at least two.  In
branch 2 the target-plus-trace matching is already perfect.  Branch 3 is the
allowed singleton completion. ∎

For a nonaxis line containing the target cell `e`, the allowed trace is
automatically target-disjoint: no other cell of that line uses source `u` or
target `v`.

## 8. Factor-signature endpoint

### Corollary CMR1549 -- PROVED

Every extension-free line-clean rook row carries one exact binary factor
signature:

1. **strong trace:** a spanning `(d-2)`-factor and coefficient
   \[
   (d/(d-2))^d;
   \]
2. **weak trace:** a spanning `(d-3)`-factor and coefficient
   \[
   (d/(d-3))^d.
   \]

The strong class fails only through target-endpoint overlap or one explicitly
identified singleton opposite-edge remainder.  The exact CMR1533 component rook
ratio remains available in both classes and may improve either bound.

The line-clean numerical frontier is therefore reduced to checking destroyed-
credit inequalities separately on these two finite trace signatures, rather
than using the weak coefficient for every line.  No all-`n` theorem is claimed.

Derangement extension, exact factor classification, permanent bounds and
prescription ratios are checked in
[`scripts/verify_prime_power_line_clean_factor_sharpening.py`](../scripts/verify_prime_power_line_clean_factor_sharpening.py).
