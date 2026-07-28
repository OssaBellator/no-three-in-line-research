# `m=10` sparse-core owner-cover Pareto bank and canonical words

`docs/348` identifies sixteen distance-five states with the joint minimum of two
flaw supports and eight atomic triples.  They form eight global-sign-complement
pairs, and their two supports share one owner.  This chapter refines the
shortest-path collateral problem by adding the owner-cover number as a third
coordinate.

No general bounded-collateral word theorem is claimed.

## 1. Three-coordinate shortest-path recursion

For a clean signed state `x`, write

```text
H(x) = number of flaw supports,
Z(x) = number of atomic collinear triples,
tau(x) = minimum number of owners meeting every flaw support.
```

For a shortest clean-macro path `x_0,...,x_d`, define its peak vector

```text
(max_i H(x_i), max_i Z(x_i), max_i tau(x_i)).
```

### Proposition PP3brk -- PROVED / OWNER-COVER PARETO RECURSION

For every clean cycle at minimum macro distance `d`, the nondominated peak
vectors over shortest paths satisfy an exact backward recursion.  For every
orientation first reached in layer `d`, combine its current triple
`(H,Z,tau)` with every Pareto vector of a legal rotated target cycle at minimum
distance `d-1`, take coordinatewise maxima, and discard dominated vectors.

#### Proof

Target fibre regeneration permits any clean orientation over the rotated target
cycle.  Therefore only the target cycle's shortest-path Pareto set remains after
one legal source rotation.  Every shortest path has one such first step, and
every recursively admitted first step gives a shortest path.  Coordinatewise
maxima compose path peaks exactly. ∎

The recursion is evaluated only on the backward cone of the eight canonical
minimum-core representatives.

## 2. Exact owner-cover Pareto classification

Call a shortest path **star-local** when every flawed state on the path has
owner-cover number at most one.  The star centre may change between steps.

### Theorem PP3brl -- VERIFIED FINITELY / FOUR COMPLEMENT-PAIRED TYPES

The sixteen minimum-core states split into four classes of four states each:

| canonical representatives | shortest-path Pareto set `(peak H, peak Z, peak tau)` |
|---|---|
| orientations `209`, `402` | `{(2,8,2)}` |
| orientations `382`, `25` | `{(3,12,1)}` |
| orientations `478`, `42` | `{(3,12,2)}` |
| orientations `293`, `311` | `{(3,12,2), (4,16,1)}` |

Each listed orientation represents its global-sign-complement pair.
Consequently:

```text
8 states admit a star-local shortest path,
8 states require owner-cover two on every shortest path,
4 states pay one extra support and four extra atomic triples to remain star-local.
```

For the tradeoff class, the support/atomic optimum `(3,12)` necessarily has
owner-cover peak two, while the star-local alternative has peak `(4,16,1)`.
The two vectors are genuinely incomparable.

#### Verification

The checker reconstructs the complete `m=10` root-cube distance layers and the
sixteen-state minimum core, computes exact support, atomic, and owner-cover
statistics for every state in the required backward cone, and compares every
nondominated vector with the hard-coded four-class ledger. ∎

This shows that a one-owner star rule is sufficient for half of the sparse core,
but not universal even at fixed shortest-path length.

## 3. Canonical five-step word bank

### Theorem PP3brm -- VERIFIED FINITELY / COMPLETE PARETO WORD BANK

The following words attain every nondominated profile.  A word entry
`[a,b,c]` denotes the three-owner source rotation on owners `a,b,c`.

| orientation | peak `(H,Z,tau)` | canonical five-step word |
|---:|---:|---|
| 478 | `(3,12,2)` | `[0,2,3] [1,4,5] [7,8,9] [3,4,6] [0,6,9]` |
| 293 | `(3,12,2)` | `[0,5,7] [1,3,5] [2,4,6] [0,1,6] [5,8,9]` |
| 293 | `(4,16,1)` | `[0,1,8] [3,6,7] [0,1,2] [0,6,9] [2,4,8]` |
| 382 | `(3,12,1)` | `[5,7,8] [0,4,6] [0,6,9] [1,3,9] [2,6,8]` |
| 209 | `(2,8,2)` | `[1,5,8] [0,1,7] [4,8,9] [0,2,7] [1,3,6]` |
| 42 | `(3,12,2)` | `[1,4,6] [2,4,8] [3,7,9] [0,2,6] [1,5,9]` |
| 311 | `(3,12,2)` | `[0,4,6] [3,5,9] [1,2,8] [4,6,9] [0,4,8]` |
| 311 | `(4,16,1)` | `[3,4,6] [1,2,8] [4,6,9] [0,6,8] [3,4,5]` |
| 25 | `(3,12,1)` | `[2,4,6] [3,5,8] [0,5,8] [1,7,8] [0,4,9]` |
| 402 | `(2,8,2)` | `[2,3,5] [4,5,7] [0,1,3] [4,5,6] [7,8,9]` |

Global sign complementation gives the corresponding word for the second state in
each pair.  The checker also hard-codes the complete orientation trace of every
word, preventing accidental acceptance of a word with the correct owner masks
but the wrong regenerated fibres.

The bank gives the first exact comparison between bounded collateral and
star-locality at `m=10`:

1. some shortest paths preserve the original `(2,8)` collateral but must leave a
   one-owner star;
2. some remain star-local with only the sharp `(3,12)` excursion;
3. some cannot remain star-local at any collateral level on a shortest path;
4. the tradeoff class can buy star-locality for exactly one extra support and
   four extra atomic triples.

The next structural task is to identify a cycle/support invariant predicting
these four types and to turn the finite word bank into a uniform local rule with
controlled predecessor charge.

Compile and run the exact checker with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_sparse_core_owner_cover_words.cpp \
  -o /tmp/check_m10_sparse_core_owner_cover_words

OMP_NUM_THREADS=12 \
  /tmp/check_m10_sparse_core_owner_cover_words
```

The next theorem identifier after this chapter is `PP3brn`.
