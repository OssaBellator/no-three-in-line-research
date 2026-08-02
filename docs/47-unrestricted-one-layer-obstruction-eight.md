# Unrestricted one-layer obstruction at base side eight

PX48 settles the arbitrary-map PX28 family negatively at bases six and seven.
Base eight was the decisive recursive case: a template there would make the
factor-independent closure `2 x 4 -> 8` iterable once more to side sixteen.

The exact rectangle search is again negative.

## 1. Search instance

Use the rectangle perfect-matching normal form PX43--PX44.  For one orientation,
the candidate hypergraph is

\[
\mathcal K_8=U\times P\times T\times R
\]

with `8^4=4096` candidate rectangle edges.  A solution would be a perfect
matching of eight edges avoiding:

1. every two-edge diagonal conflict;
2. every three-edge transversal conflict.

The verifier precomputes exact integer line masks for the `16 x 16` scalar grid.
For each candidate edge it stores a bitset of all diagonal-conflict partners.
For every selected pair, the union of the sixteen corner-pair line masks gives
exactly the forbidden transversal completions.

The depth-first search uses four additional exact reductions.

1. It branches on the uncovered vertex of `U,P,T,R` with the fewest legal
   incident edges.
2. It enforces all four matching-coordinate constraints by bitsets.
3. It applies Hall's condition to each of the three remaining coordinate
   projections against the uncovered `U` vertices.
4. It partitions the `512` possible first edges incident with `u=0` into five
   disjoint shards.  The union of the five shards is the complete search.

No probabilistic pruning or floating-point geometry is used.

## Theorem PX49 -- PROVED FINITE

The unrestricted arbitrary-block PX28 family has no normalized no-three
template at base side eight in any global orientation.

The exact shard node counts are:

| Orientation | Shard 0 | Shard 1 | Shard 2 | Shard 3 | Shard 4 | Total |
|---|---:|---:|---:|---:|---:|---:|
| `cc` | 3,336,122 | 3,381,122 | 3,356,577 | 3,311,142 | 3,416,801 | 16,801,764 |
| `cf` | 3,861,211 | 3,874,367 | 3,943,299 | 4,082,627 | 4,058,218 | 19,819,722 |
| `ff` | 3,242,573 | 3,272,105 | 3,225,108 | 3,086,566 | 3,244,262 | 16,070,614 |

The first two shards in each row contain `103` first-edge cases and the other
three contain `102`, so every one of the `512` root cases is covered exactly
once.  Orientation `fc` is infeasible by the exact scalar-transpose equivalence
PX47 applied to `cf`.

### Proof

Run the complete conflict-aware matching search described above.  In every
listed shard, every branch terminates before selecting eight pairwise compatible
conflict-free edges.  PX43 identifies such matchings with all normalized
arbitrary-map PX28 states, and PX39 identifies every unnormalized four-block
state with a normalized representative.  PX47 supplies the remaining crossed
orientation.  Therefore no PX28 template exists at base eight. \(\square\)

## Corollary PX49a -- PROVED FINITE

No saturated side-eight factor can be doubled to side sixteen by the PX28
one-inner-layer construction, even when all four block maps are arbitrary
permutations.

In particular, the proved factor-independent closure

\[
2\times4\longrightarrow8
\]

cannot be iterated through another PX28 template at base eight.

## 2. Complete small-side boundary

The unrestricted arbitrary-map one-inner-layer family is now exactly classified
through base side eight:

| Base side | Template existence |
|---:|---|
| 2 | yes |
| 3 | no |
| 4 | yes |
| 5 | yes |
| 6 | no |
| 7 | no |
| 8 | no |

Thus the successful bases in this range are isolated rather than the beginning
of a universal doubling sequence.

## 3. Verification

The exact solver is implemented in C++ for compact bitset operations and driven
by a Python harness that checks every recorded shard count:

```bash
python scripts/verify_product_unrestricted_eight.py
```

The default run compiles the solver and executes five shards in parallel for
`cc`, `cf`, and `ff`.  A single orientation can be checked with, for example,

```bash
python scripts/verify_product_unrestricted_eight.py --orientation ff
```

The `fc` case is transferred from `cf` by PX47 rather than duplicated.

## 4. Updated boundary

PX49 closes the most obvious recursive use of the side-four template.  Any
infinite product route must now leave at least one assumption of PX28.  The main
remaining possibilities are:

1. select both inner layers nontrivially through the full degree-two host;
2. use a larger outer factor than side two;
3. enlarge the factor-compatible host beyond blockwise digit permutations;
4. prove a repair or resampling theorem in the full selector state space;
5. construct a different infinite family not based on one-inner-layer doubling.

The theorem is a finite obstruction to one construction family, not a
nonexistence result for saturated no-three configurations at side sixteen.
