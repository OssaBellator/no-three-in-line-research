# Side-four hard-core chambers have one explicit alternating-exchange normal form

## Scope

The eleven positive-minimum side-four raw hosts were previously known to contain nine two-response hosts and two one-response hosts. Their complete full-selector atlas has twenty chambers, but the chamber conditions were stored as opaque affine-row differences.

This chapter makes the hard-core comparison explicit. All nine nontrivial hosts compare the same two perfect matchings, those matchings differ on one alternating four-cycle, and every nontrivial chamber is governed by one integer functional.

The executable checker is:

```text
python scripts/check_prime_power_hard_core_exchange_normal_form.py
```

This is an exact finite scalar-selector theorem. It does not populate genuine survivor signatures, prove labelled child semantics, or close any all-`n` implication. It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2722--CMR2733

### CMR2722 — exact hard-core response-family normal form

Let

\[
Q_1=(3,0,1,2),
\qquad
Q_4=(3,2,1,0).
\]

Reconstructing every side-four raw host from the fixed forbidden diagonal, the target edge `(0,1)`, and every canonical partial-matching deletion set gives exactly eleven hosts whose minimum response triple count is positive.

Their response families are exactly:

```text
9 hosts: [Q1, Q4]
2 hosts: [Q4]
```

No other response occurs on the hard core.

### CMR2723 — one alternating four-cycle

The two hard-core responses share the edges

\[
(0,3),\qquad(2,1).
\]

Their remaining edges are

\[
Q_1\setminus Q_4=\{(1,0),(3,2)\},
\]

and

\[
Q_4\setminus Q_1=\{(1,2),(3,0)\}.
\]

Thus the exchange is the unique alternating four-cycle on source rows `1,3` and target columns `0,2`.

### CMR2724 — exact rank-one cross difference

Use the reduced survivor-background cross coordinates `d_ij` from the affine-selector signature.

The positive-positive response cells of `Q_1` are

\[
(2,1),(3,2),
\]

while those of `Q_4` are

\[
(1,2),(2,1).
\]

Therefore the complete rank-one cross contribution to

\[
F_{Q_1}-F_{Q_4}
\]

is

\[
\boxed{d_{32}-d_{12}}.
\]

### CMR2725 — exact pair-line multisets

Write a line as its primitive normalized equation `ax+by+c=0`, and define

\[
K_-:x-y-1=0,
\]

\[
K_+:x+y-3=0,
\]

\[
K_{30}:3x+y-3=0,
\]

and

\[
K_{03}:x+3y-9=0.
\]

The six unordered response-point pairs of `Q_1` have supporting-line multiset

\[
\boxed{3K_-+K_++K_{30}+K_{03}},
\]

whereas all six pairs of `Q_4` lie on the anti-diagonal:

\[
\boxed{6K_+}.
\]

Hence the complete rank-two background-line contribution to `F_{Q_1}-F_{Q_4}` is

\[
\boxed{3h_{K_-}+h_{K_{30}}+h_{K_{03}}-5h_{K_+}}.
\]

### CMR2726 — exact rank-three constant difference

The response `Q_1` contains exactly one collinear triple, supported on `K_-`. The response `Q_4` contains all four triples from its four anti-diagonal points.

Therefore

\[
\boxed{W_3(Q_1)-W_3(Q_4)=1-4=-3}.
\]

### CMR2727 — explicit hard-core exchange functional

Combining CMR2724--CMR2726 gives the exact affine-row difference

\[
\boxed{
\Delta
=
F_{Q_1}-F_{Q_4}
=
d_{32}-d_{12}
+3h_{K_-}
+h_{K_{30}}
+h_{K_{03}}
-5h_{K_+}
-3.
}
\]

No other reduced-signature coordinate occurs in the hard-core comparison.

### CMR2728 — lexicographic weak/strict chamber split

The response `Q_1` is lexicographically earlier than `Q_4`. Consequently, on every two-response hard-core host,

\[
\boxed{Q_1\text{ is selected}\iff\Delta\le0,}
\]

and

\[
\boxed{Q_4\text{ is selected}\iff\Delta>0.}
\]

The weak inequality belongs to `Q_1` because deterministic tie-breaking selects the earlier response. The complementary `Q_4` chamber is strict.

### CMR2729 — exact integer pressure threshold

All signature coordinates are integral. Therefore the strict chamber can be written without an open inequality:

\[
\boxed{
Q_4\text{ is selected}
\iff
d_{32}+3h_{K_-}+h_{K_{30}}+h_{K_{03}}
\ge
d_{12}+5h_{K_+}+4.
}
\]

Equivalently,

\[
\boxed{
Q_1\text{ is selected}
\iff
d_{32}+3h_{K_-}+h_{K_{30}}+h_{K_{03}}
\le
d_{12}+5h_{K_+}+3.
}
\]

Thus the baseline three-unit rank-three advantage of `Q_1` can be overturned only by at least four units of net background exchange pressure.

### CMR2730 — twenty chambers collapse to one nontrivial functional

The nine two-response hosts each have the same two chambers `Delta<=0` and `Delta>0`. The two one-response hosts have the full signature space as their unique `Q_4` chamber.

Hence the twenty hard-core chambers decompose as

```text
9 copies of the weak Q1 halfspace
9 copies of the strict Q4 halfspace
2 singleton-response full spaces
```

and there is exactly one distinct nontrivial chamber functional.

Host labels remain necessary because their deletion sets, source records, and eventual labelled child semantics differ. The scalar selector comparison itself is host-independent.

### CMR2731 — exact small-signature cube

The checker exhausts

```text
5^2 cross assignments × 4^4 line-load assignments = 6,400 cases
```

using

```text
d12,d32 in {-2,-1,0,1,2}
h_K in {0,1,2,3}
```

for the four relevant lines. In every case it verifies both

\[
\Delta=F_{Q_1}-F_{Q_4}
\]

and the exact weak/strict lexicographic partition.

### CMR2732 — wide deterministic stress and corruption rejection

A second deterministic suite checks 1,000 signatures with wider integer cross coordinates and nonnegative line loads.

The sealed manifest has digest

```text
ae35c2afa6574f602ccc2bb10124c0a5743ae4d712ebd967f93e56680928b1bf
```

and rejects ten independent corruptions affecting the census, responses, exchange cycle, coefficient maps, constant term, chamber strictness, and manifest seal.

### CMR2733 — hard-core frontier reduction and honesty boundary

The scalar hard-core chamber problem is now reduced to one explicit exchange statistic. This is useful for the twenty-chamber worklist because a genuine survivor-signature proof need only evaluate the displayed functional rather than manipulate an opaque sparse row digest.

It does **not** close the hard core. The remaining mathematical obligations include:

1. populate every genuine hard-core survivor signature;
2. prove which side of the exchange threshold each genuine signature occupies;
3. retain destroyed-threshold, labelled-child, return, interface, and recurrent-row terms;
4. prove the selected response has the required semantic correction or routing;
5. complete ordinary review of all twenty chamber arguments.

The two singleton `Q_4` hosts remain irreducible on their current raw allowed-edge sets and still require correction, altered routing, or a changed operation/state.

## Current mathematical status

This chapter advances the finite T21 hard-core selector geometry, but no chamber theorem is marked complete merely from the affine normal form. The classical conjecture remains open.
