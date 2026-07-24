# All successful crossed side-nine hosts have two-cycle repair

This note upgrades PX19 from one representative host to every successful
ordered `3 x 3` factor-pair instance in the `cf` orientation.

There are four ordered saturated no-three factor pairs at side three:

\[
A_0=((0,2,1),(1,0,2)),
\qquad
A_1=((1,0,2),(0,2,1)),
\]

\[
B_0=((1,2,0),(2,0,1)),
\qquad
B_1=((2,0,1),(1,2,0)).
\]

Within each lettered family, the second pair is obtained only by swapping the
two permutation layers.

## Theorem PX20 — PROVED

The exhaustive full-selector census has exactly eight successful ordered
factor-pair instances in the crossed `cf` orientation. They are precisely

\[
A_r\times B_s
\quad\text{and}\quad
B_s\times A_r,
\qquad r,s\in\{0,1\}.
\]

Every one of these eight hosts has:

- `6,840` degree-two states;
- `1,359,432` unordered single-cycle adjacencies;
- `2` no-three states;
- `6,814` bad states with an improving one-cycle move;
- `24` states requiring a two-cycle batch.

The two-cycle profiles are always

\[
20\text{ copies of }3\longrightarrow3\longrightarrow0
\]

and

\[
4\text{ copies of }3\longrightarrow4\longrightarrow0.
\]

Hence every successful ordered `3 x 3` crossed host has repair radius two and
maximum necessary uphill barrier one.

## Proof

The full product host uses all four layer products. Swapping the two outer
layers or the two inner layers therefore leaves the host unchanged. Thus the
eight successful ordered instances reduce to two distinct hosts:

\[
A_0\times B_0
\qquad\text{and}\qquad
B_0\times A_0.
\]

The exact repair-graph enumeration gives the displayed census for both
representatives. Layer-swap invariance transfers it to all eight ordered
instances. \(\square\)

## Verification

Run

```bash
python scripts/verify_product_all_side_nine_batches.py
```

The script recomputes the complete repair graph for both distinct hosts using
only the standard library.

## Consequence for the open target

The bounded-batch pattern is not an accident of one selected side-nine
representative: it holds throughout the complete successful crossed family at
that size. This remains finite evidence. A general theorem must still explain
why feasible hosts should admit bounded batches and why infeasible hosts such
as all tested `2 x 5` products produce a recognizable obstruction instead.
