# Auxiliary transposition for a singleton-blocked completion

**Branch:** `research/rational-inverse-expansion`

RI5h--RI5k isolate one desired completion cell occupied by the blocker layer and show that the active completion cycle cannot be installed partially. The blocker layer, however, is a full permutation. One additional blocker cell is enough to move the singleton blocker without extending the active completion component.

## Setup

Let \(N\) be the active-layer matching obtained after installing the selected RI5f completion components, except that one component is held back only because its desired cell

\[
q=(c_0,r_0)
\]

belongs to the blocker matching \(M_1\). Equivalently, the proposed completed active matching contains \(q\). Assume the ambient permutation size is \(n\ge2\).

For any other blocker cell

\[
p=(c_1,r_1)\in M_1,
\qquad c_1\ne c_0,
\]

define the crossed replacement

\[
q'=(c_0,r_1),
\qquad
p'=(c_1,r_0).
\]

## RI5l -- auxiliary blocker transposition -- PROVED

Replace the held-back active component by its full target matching, remove \(q,p\) from \(M_1\), and insert \(q',p'\). The resulting two-layer state:

1. preserves every active-layer row and column;
2. preserves every blocker-layer row and column;
3. keeps the two layers disjoint.

Thus every singleton-blocked RI5h component is occupancy-installable whenever \(n\ge2\).

### Proof

The completed active matching \(N\) contains \((c_0,r_0)\). Since \(p\ne q\) and \(M_1\) is a matching, \(c_1\ne c_0\) and \(r_1\ne r_0\).

Removing \(q,p\) and inserting \(q',p'\) preserves exactly the two blocker columns \(c_0,c_1\) and rows \(r_0,r_1\).

The cell \(q'=(c_0,r_1)\) does not meet the active layer because the active cell in column \(c_0\) is \((c_0,r_0)\). The cell \(p'=(c_1,r_0)\) does not meet the active layer because row \(r_0\) is already used by the active cell in column \(c_0\), so the active matching cannot use row \(r_0\) in column \(c_1\). Hence both replacement blocker cells are disjoint from \(N\). \(\square\)

Combining RI5h and RI5l gives a complete occupancy trichotomy:

- zero blocked desired cells: install directly;
- at least two blocked desired cells: use the RI5h derangement;
- exactly one blocked desired cell: use the RI5l auxiliary transposition.

Opposite-layer occupancy is therefore no longer an obstruction to physical completion. The remaining issue is collateral.

## RI5m -- uniform auxiliary-transposition bank -- PROVED

Fix the singleton blocker \(q\). For every blocker column \(c\ne c_0\), use the auxiliary cell

\[
p_c=(c,M_1(c))
\]

in RI5l. This gives a bank \(\Omega_q\) of exactly

\[
\boxed{|\Omega_q|=n-1}
\]

valid two-layer states, all with the same completed active matching.

Move into the fixed term \(F\):

- all active-layer collateral, which is identical in every bank state;
- all blocker-layer collateral independent of the auxiliary choice.

Let \(\mathcal T\) be the remaining possible new blocker-layer triples, so every \(T\in\mathcal T\) contains at least one newly inserted crossed cell. Then

\[
\boxed{
\Pr_{\Omega_q}(T\text{ occurs})\le\frac1{n-1}.
}
\]

### Proof

For auxiliary column \(c\), the two newly inserted cells are

\[
(c_0,M_1(c))
\qquad\text{and}\qquad
(c,r_0).
\]

A cell of the first form determines \(c\) uniquely because the blocker rows \(M_1(c)\) are distinct. A cell of the second form determines \(c\) from its column. Therefore any exact new triple containing a crossed cell can occur for at most one auxiliary choice. Uniform averaging over the \(n-1\) choices gives the bound. \(\square\)

## RI5n -- collateral criterion and failure localization -- PROVED

Let \(W\) be the paid weight destroyed by completing the selected components, and put

\[
T=\sum_{C\in\mathcal T}w(C).
\]

If

\[
\boxed{
W>F+\frac{T}{n-1},
}
\]

then one RI5l transposition state strictly lowers the paid potential.

If \(W>F\) and this sufficient inequality fails, then

\[
\boxed{
T\ge(n-1)(W-F).
}
\]

More generally, for any finite profile map \(\sigma:\mathcal T\to\Sigma\), with \(|\Sigma|=L\), one profile has raw candidate weight at least

\[
\boxed{
\frac{(n-1)(W-F)}{L}.
}
\]

### Proof

RI5m bounds the expected variable collateral by \(T/(n-1)\). Every bank state destroys the same paid weight \(W\), so a negative expected drift supplies an improving state.

Failure gives \(T/(n-1)\ge W-F\), proving the raw-weight bound. The profile fibres partition \(\mathcal T\), so one of the \(L\) fibres carries at least a \(1/L\) share. \(\square\)

## Interface to RI6

RI5l removes the heavy singleton blocker as a feasibility obstruction. RI6 now receives only two explicit tasks:

1. compare the completed active-layer collateral and the auxiliary-transposition collateral with the destroyed paid weight;
2. if the comparison fails, classify the resulting profile whose raw blocker-layer candidate weight grows linearly with \(n-1\).

The second output is especially rigid: every candidate uses one of two crossed-cell channels attached to the fixed blocker row or blocker column.

## Finite check

`scripts/verify_rational_singleton_transposition.py` exhausts disjoint active and blocker permutations and proposed completed active matchings through size five. It verifies every auxiliary transposition, layer disjointness, uniqueness of the auxiliary choice for every newly created blocker triple, and the exact `1/(n-1)` cylinder cap.