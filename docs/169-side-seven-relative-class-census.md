# Exact side-seven relative-class census

The effective rectangle-label repair theorem now closes doubling above the active
cutoff, but a structural finite-range bridge is still missing.  The first
unresolved base after the special closures PX41, PX51, and PX60 is side seven.
This chapter removes the factor-enumeration ambiguity at that side.

A saturated configuration on `[7]^2` is a simple bipartite graph between the
seven scalar rows and seven scalar columns, with degree two at every vertex.
Every component is an even cycle.  Alternating the edges of each component gives
the two permutation layers.  If a component has length `2L`, it contributes one
`L`-cycle to the relative permutation

\[
h=\tau_0^{-1}\tau_1.
\]

Thus the relative cycle type is determined by the selected graph itself and is
independent of the alternating colouring.

## 1. Exact saturated graph census

### Theorem PX493 -- PROVED FINITE

There are exactly

\[
\boxed{132}
\]

labelled saturated no-three configurations on `[7]^2`.

Their bipartite component half-length partitions are:

| Relative cycle type | Saturated configurations |
|---|---:|
| `(7)` | 60 |
| `(5,2)` | 32 |
| `(4,3)` | 20 |
| `(3,2,2)` | 20 |

No other derangement cycle type occurs.

### Proof

Process the seven scalar rows in order.  In each row choose one of the
`binom(7,2)=21` unordered column pairs.  Maintain column degrees and reject a
choice if a column cannot finish at degree two.  Since each row contains exactly
two selected points, a newly completed collinear triple must contain exactly one
new point and two previously selected points.  Exact integer determinant tests
therefore give a complete incremental search.

At a completed state, traverse the degree-two bipartite graph and record half of
each component length.  The verifier visits 51,967 search nodes and obtains the
displayed counts. \(\square\)

## 2. Ordered factor-pair counts

A graph with `c` even-cycle components has exactly `2^c` ordered alternating
colourings into two permutation layers.  Reversing the colours on any component
changes the ordered pair, while every ordered decomposition arises this way.

### Corollary PX494 -- PROVED

The 132 configurations give exactly

\[
\boxed{488}
\]

ordered saturated side-seven factor pairs, distributed as follows.

| Relative cycle type | Graphs | Colourings per graph | Ordered factors |
|---|---:|---:|---:|
| `(7)` | 60 | 2 | 120 |
| `(5,2)` | 32 | 4 | 128 |
| `(4,3)` | 20 | 4 | 80 |
| `(3,2,2)` | 20 | 8 | 160 |

The total is `120+128+80+160=488`.

## 3. Canonical full-selector target

PX50 proves that arbitrary blockwise digit permutations make the complete
side-two outer host depend on an inner factor only through the conjugacy class of
its relative permutation.

### Corollary PX495 -- PROVED REDUCTION

Universal side-seven doubling

\[
2\times7\longrightarrow14
\]

in the arbitrary block-map full-selector family reduces exactly to four
canonical host problems, one for each of

\[
(7),\qquad(5,2),\qquad(4,3),\qquad(3,2,2).
\]

One successful `(T,P,Q,H)` host and spanning no-three degree-two selector for
each class would cover all 488 ordered factors by conjugation transport.

This is a finite structural reduction, not a proof that the four templates
exist.

## Verification

Run

```bash
python scripts/verify_product_side_seven_relative_classes.py
```

The verifier performs the complete row-pair search, checks every determinant,
extracts every bipartite component partition, and verifies the ordered-factor
multiplicities.