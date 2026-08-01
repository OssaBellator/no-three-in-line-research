# Five-point boundary refill obstruction

`docs/585`, `docs/591`, and `docs/597` progressively enlarge the correction
class around the four sharp three-deletion seam repairs.  This chapter closes the
next exact class: delete two additional incidences and refill all five deleted
row and column degrees.

## 1. Search class

For each of the four sharp repairs, let `O` be the original six-block point set
and let `D_3` be its certified three-point deletion set.  The repaired set
`O\D_3` is no-three-in-line but has three deficient columns and two deficient
rows.

Choose two further points from `O\D_3`.  The resulting five deleted points define
a row multiset and a column multiset of size five.  A degree-preserving refill is
any five distinct cells obtained by matching those two multisets exactly.

### Theorem PP3cub — PROVED / COMPLETE FIVE-POINT REFILL ENUMERATION

Across the four sharp repairs there are exactly

```text
4 * C(45,2) = 3960
```

two-additional-deletion cases.  After duplicate refill sets and repeated cells
are removed, they produce exactly `210092` degree-preserving five-point refill
candidates.

#### Proof

The checker reconstructs the eight radius-32 five-block survivors, the four
sharp sixth-block repairs, and then iterates every pair of further deleted
points.  For each pair it enumerates every matching of the deleted column
multiset to the deleted row multiset and canonicalizes the resulting cell set.
The per-repair count is `52523`. ∎

### Theorem PP3cuc — PROVED / FIVE-POINT OBSTRUCTION

None of the `210092` candidates is no-three-in-line.

#### Proof

For each candidate, the checker first rejects any added point on a pair-line of
the retained set, then rejects any added pair whose line contains a retained
point, and finally checks triples entirely among the five additions.  Every
candidate fails one of these exact tests. ∎

### Theorem PP3cud — PROVED / LOCAL CORRECTOR CLASS CLOSED

No corrector obtained by the sharp three deletions, two further deletions, and
exact refill on the five deleted row-column incidences completes the sixth
block.

Consequently the next boundary attempt must do at least one of the following:

1. add cells outside the five deleted degree supports;
2. change at least three additional incidences;
3. alter the preserved saturation interface; or
4. replace the explicit `P/Q` block geometry.

This is a finite obstruction for the radius-32 catalogue, not an all-offset or
all-block theorem.

## Exact audit

```bash
python scripts/check_boundary_five_point_refill_obstruction.py
```
