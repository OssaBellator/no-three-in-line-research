# Shared-state cache pilot for `(5,2)` radius-three support twenty

PX589--PX591 reject radius-three supports through eighteen in the `(5,2)`
class.  The first open stratum has

\[
\boxed{71{,}860}
\]

selectors at symmetric-difference support twenty.  An independent-selector
coordinate census is too expensive at the observed branching cost.  This
chapter gives two exact compression ledgers and validates a shared-top search
on the largest repeated top signature.

Let `L_2` be the exact radius-two layer, let `F_0` be the certified centre, and
let `C_20` be the radius-three support-twenty stratum.

## 1. Radius-two parent incidence

Join `P in L_2` to `F in C_20` when `F` is a simple alternating-cycle neighbour
of `P`.

### Theorem PX592 -- PROVED FINITE

The bipartite parent graph has exactly

\[
\boxed{1{,}669{,}828}
\]

directed incidences.

Every selector in `C_20` has between `5` and `241` radius-two parents.  Every
radius-two parent has between `0` and `594` support-twenty children; exactly
`4,237` of the `26,550` radius-two parents have no such child.

Thus parent overlap is substantial: the average selector has more than twenty
radius-two witnesses, while some single parents control almost six hundred
support-twenty selectors.

### Theorem PX593 -- PROVED FINITE

Apply the deterministic greedy cover rule:

1. choose a radius-two parent covering the largest number of currently
   uncovered selectors;
2. break ties by choosing the lexicographically largest parent selector;
3. mark all its support-twenty children covered and repeat.

This produces a cover of all `71,860` selectors using exactly

\[
\boxed{699}
\]

radius-two parents.  The first one hundred selected parents cover

\[
\boxed{43{,}726}
\]

selectors.

This is an explicit cover, not a claim of minimum set-cover size.  It reduces
the number of parent-indexed search groups from `26,550` to `699`.

## 2. Exact top- and bottom-signature ledger

For a selector

\[
F=(F_0,\ldots,F_{13}),
\]

where `F_r` is the two-bit row mask inside the 14-column abstract host, define

\[
\operatorname{top}(F)=(F_0,\ldots,F_6),
\qquad
\operatorname{bottom}(F)=(F_7,\ldots,F_{13}).
\]

### Theorem PX594 -- PROVED FINITE

The support-twenty layer has exactly

\[
\boxed{38{,}553}
\]

distinct top signatures and the same number of distinct bottom signatures.
Exactly `29,632` seven-row signatures occur in both collections.  The largest
multiplicity of either a top or bottom signature is `46`.

Consequently a top-signature cache reduces the number of independent top-half
problems from `71,860` to `38,553`.  This is weaker compression than the greedy
parent cover, but it shares the full fourteen-variable column-order search,
not merely selector generation.

## 3. Simultaneous-selector coordinate recursion

Let `E` be the 56 potential cells of the complete abstract host and let
`C` be a family of candidate selectors.  For each `e in E`, store the bitset

\[
B_e=\{F\in C:e\in F\}.
\]

During a partial coordinate assignment, maintain the active candidate bitset
`A`.  Whenever three host cells `e,f,g` become scalar-complete and collinear,
replace

\[
A\leftarrow A\setminus(B_e\cap B_f\cap B_g).
\]

### Theorem PX595 -- PROVED

The active-bitset recursion is exactly equivalent to running the no-three
coordinate CSP independently on every selector in `C`.

### Proof

A candidate is deleted exactly when three cells selected by that candidate
have become scalar-complete and collinear.  Every invalid candidate is deleted
when the last unresolved coordinate of its first completed bad triple is
assigned.  Conversely every deleted candidate contains the displayed triple.
Thus at every partial assignment `A` is precisely the family of candidates not
yet disproved.  An empty bitset permits exact pruning, while a surviving
candidate at a complete assignment is an actual no-three embedding. \(\square\)

This gives a logically exact shared coordinate tree; it is not a probabilistic
or heuristic filter.

## 4. Largest repeated top signature

The most frequent top signature is

```text
3, 768, 12, 3072, 144, 8224, 4160
```

or, as selected abstract column pairs by top row,

```text
{0,1}, {8,9}, {2,3}, {10,11}, {4,7}, {5,13}, {6,12}.
```

It occurs in exactly `46` support-twenty selectors.

### Theorem PX596 -- PROVED FINITE

For this common top signature, the exact number of no-three top-half column
orders is:

| Column embedding | Clean `(A_0,A_1)` orders | Top-search nodes |
|---|---:|---:|
| concatenated | 65,296 | 576,716 |
| interleaved | 1,584 | 39,556 |

Scaling the seven top row coordinates by two preserves collinearity, so the
same top-order lists serve both row embeddings for each column embedding.

### Theorem PX597 -- PROVED FINITE

None of the `46` selectors sharing this signature has a full no-three embedding
in any radix orientation.

The shared bottom-row CSP totals are:

| Orientation | Shared top orders | Bottom-CSP nodes | Feasible selectors |
|---:|---:|---:|---:|
| 0 | 65,296 | 291,211 | 0 |
| 1 | 1,584 | 6,842 | 0 |
| 2 | 65,296 | 293,813 | 0 |
| 3 | 1,584 | 9,539 | 0 |
| **Total** |  | **601,405** | **0** |

The concatenated lists are split into sixteen deterministic `4,081`-order
shards in each of orientations zero and two.  The interleaved orientations are
small enough to run as single cases.

### Corollary PX598 -- PROVED REDUCTION

The open `(5,2)` radius-three support-twenty stratum is reduced from `71,860` to

\[
\boxed{71{,}814}
\]

selectors.  More importantly, PX595--PX597 validate shared-top enumeration and
active-candidate bitsets on the largest repeated signature.  The next exact
target is to process the remaining top signatures in decreasing multiplicity,
with separate caches for concatenated and interleaved column embeddings.

This is a finite local obstruction.  It does not prove that the remaining
support-twenty selectors, the `(5,2)` canonical class, universal
`2 x 7 -> 14`, or exact all-side closure are impossible.

## 5. Verification

Compile and run the reuse census:

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_reuse.cpp \
  -o /tmp/side7_c52_r3_s20_reuse
/tmp/side7_c52_r3_s20_reuse
```

Compile and run the shared-top coordinate verifier:

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_cache.cpp \
  -o /tmp/side7_c52_r3_s20_cache

/tmp/side7_c52_r3_s20_cache interleaved
for orientation in 0 2; do
  for shard in {0..15}; do
    /tmp/side7_c52_r3_s20_cache concatenated "$orientation" "$shard"
  done
done
```

The reuse census regenerates `L_1,L_2,C_20`, checks all incidence, signature,
and greedy-cover counts, and identifies the recorded 46-selector signature
class.  The coordinate cases regenerate the exact clean top orders and assert
every recorded shared bottom-CSP node total using integer collinearity on
`[14]^2`.
