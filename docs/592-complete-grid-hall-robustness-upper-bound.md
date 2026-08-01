# Complete-grid Hall robustness upper bound

`docs/580` and `docs/586` decode the twelve quotient choices into the twelve ordered distinct pairs in the first two rows of a `4 x 4` grid. Six pair geometries have one legal residual matching and six have two. This chapter proves that no alternative bijective relabelling of the same complete grid can remove that split.

## 1. Fragility is a geometry invariant

### Theorem PP3csu -- PROVED / COMPLETE-BIJECTION ROBUSTNESS CEILING

Among the twelve ordered distinct row-pair geometries,

```text
6 have minimum residual-cell blocker size 1,
6 have minimum residual-cell blocker size 2.
```

Every injective decoder from the twelve quotient choices onto these twelve geometries is a bijection. Therefore every complete bijective decoder contains exactly six singleton-blocker choices, regardless of how quotient labels are permuted.

#### Proof

The extension count and blocker size depend only on the selected pair of grid cells. A bijection preserves the multiset of the twelve pair geometries, hence preserves the six/six blocker multiset. ∎

## 2. One fixed host exclusion

### Theorem PP3csv -- PROVED / SINGLE-CELL SURVIVAL PROFILE

For the eight possible residual cells in rows two and three, forbidding one cell kills either one or two of the twelve pair geometries. Precisely four residual cells kill one pair and four kill two pairs.

Thus a complete decoder retains either

```text
11 or 10
```

quotient choices after one fixed residual-cell exclusion. Relabelling the quotient states changes which states fail but cannot improve the total number of survivors for that geometric exclusion.

#### Proof

For each residual cell, inspect all legal matching extensions of every pair. A pair is killed exactly when every extension contains the forbidden cell. The complete census gives the histogram `{1:4,2:4}`. ∎

## 3. Necessary enlargement

### Theorem PP3csw -- PROVED / COMPLETE FOUR-BY-FOUR HOST IS INSUFFICIENT FOR UNIFORM ROBUSTNESS

No decoder that is bijective onto all twelve ordered distinct pair geometries of this `4 x 4` host can have minimum blocker size two. Uniform single-exclusion robustness requires at least one structural change:

1. a larger residual matching host;
2. additional extension cells or gadgets;
3. a decoder not constrained to cover each pair geometry exactly once;
4. host-specific information that avoids the forbidden geometry before quotient decoding.

#### Proof

`PP3csu` forces six singleton-blocker geometries in every complete bijection. ∎

## 4. Exact audit

Run

```bash
python scripts/check_hall_bijection_robustness_bound.py
```

The checker enumerates all twelve pair geometries, all eighteen legal no-three-in-line matching extensions, the six/six blocker split, and the eight single-cell exclusion profiles.

## 5. Prime-patching consequence

Changing the quotient-to-cell labels cannot solve the Hall robustness problem inside the present complete grid. The next meaningful step is to identify a larger or richer actual endpoint host, not to search more permutations of the same twelve geometries.
