# Repeated corrected boundary transitions

`docs/609` constructs sharp six-point seam correctors, and `docs/615` finds one
corrected seventh-block transition.  This chapter performs the next complete
radius-32 transition audit from that corrected seven-block state.

The stored corrected state contains fifty-six points.  For every typed `P` or
`Q` block and every offset from `-32` through `32`, form the cross-line conflict
hypergraph whose vertices are old and new points and whose hyperedges are the
new collinear triples.

## 1. Eighth-step transversal census

### Theorem PP3cwd -- PROVED / COMPLETE RADIUS-32 EIGHTH TRANSVERSAL CENSUS

Across the `8*65=520` typed eighth-block attempts, the exact minimum transversal
histogram is

```text
4:1, 5:6, 6:21, 7:68, 8:164,
9:2, 10:4, 11:34, 12:41, 13:107, 14:72.
```

Exactly ninety-six attempts have minimum transversal size at most seven.  Their
minimum transversal families contain exactly 808 distinct sets.

#### Proof

The checker builds every cross-line triple exactly with integer determinants.
For each hypergraph it solves minimum hitting set by branch-and-bound with a
disjoint-edge packing lower bound.  It then enumerates every hitting set at the
certified minimum for the ninety-six relevant attempts, deduplicating the
selected point masks.  The displayed counts sum to 520, and the enumerated
minimum-set count is 808. ∎

## 2. Unique seven-point degree correction

### Theorem PP3cwe -- PROVED / UNIQUE CORRECTED EIGHTH TRANSITION THROUGH SIZE SEVEN

Among all 808 minimum transversals, and all extra deletions raising their total
size to at most seven, exactly one degree-preserving no-three-in-line refill
exists.  It uses block `P1` at offset `31`.  Its minimum conflict transversal has
size five and its complete correction has size seven:

```text
delete:
(0,2), (1,3), (23,108), (24,49), (28,110), (28,113), (30,110)

add:
(0,110), (1,113), (23,2), (24,110), (28,3), (28,108), (30,49).
```

Every row and column multiplicity is preserved.

#### Proof

For each minimum transversal, the checker enumerates zero, one, two, or three
additional deletions as needed to reach total size seven.  It assigns the deleted
row multiset to the deleted column multiset by exact backtracking, pruning any
candidate point on an inherited pair line and any mixed or internal new triple.
There is exactly one successful core and one successful eighth-block attempt.
The listed deletion and addition multisets have identical row and column
multiplicities, and the resulting sixty-four-point state has no collinear triple.
∎

## 3. Ninth-step obstruction

### Theorem PP3cwf -- PROVED / NO RAW NINTH EXTENSION IN THE AUDITED RADIUS

The unique corrected eight-block state has no raw ninth-block extension among
the 520 typed radius-32 attempts.

#### Proof

Append every typed block at every audited offset and test all triples by exact
integer determinants.  Every attempt contains a collinear triple. ∎

## Consequence

The corrected-state transition graph now contains a path through eight blocks,
but the audited path is not yet periodic or strongly connected.  A ninth-step
corrector, a larger offset range, or a different block catalogue is still
required.  This is a bounded exact transition result, not an all-length boundary
construction.
