# Two-component anchor rerouting radius

The comparison section of `docs/654-fourteen-pair-saturated-anchor-reservoir.md`
records that the canonical thirteen-pair source has two incidence components of
size two, and every minimum-crossing anchor matching uses exactly four cross-
component pairs. The question is whether deleting either small component admits
a uniformly bounded global repair.

## PP3daq — Exact boundary-flow theorem

There are exactly 104 anchor matchings with the minimum four cross-component
pairs. For every one of those matchings and for either two-pair incidence
component:

- both deleted source rows are paired to targets outside the component; and
- exactly two surviving source rows are paired to targets inside the component.

Thus deletion removes two outgoing assignments and invalidates exactly two
incoming assignments. The boundary flow is always `(2,2)` across all 208
matching/component cases.

## PP3dar — Four-assignment rerouting radius

Delete either two-pair component and restrict to the eleven surviving `P` and
`Q` rows. Among all valid anchor permutations on those eleven rows, the minimum
Hamming distance from the surviving part of the original matching is exactly
four in every one of the 208 cases.

Two changes are forced immediately because two surviving rows point into the
deleted component. The exact assignment search proves that two changes never
suffice and that four always suffice. Hence the canonical `13 -> 11` source
deletion has a uniform finite anchor rerouting radius four at the permutation
level.

## PP3das — Uniform optimal-rerouting multiplicity

For each of the 208 cases, exactly 144 surviving anchor permutations attain the
minimum rerouting distance four. The multiplicity is independent of which
minimum-crossing matching or which two-pair component is deleted.

This supplies substantial combinatorial freedom for a future coordinate-level
nesting rule, but does not choose one geometrically safe rerouting.

## Evidence boundary

The checker certifies only the anchor-permutation layer of the canonical finite
source. A uniform prefix construction must still realize one of these four-
assignment repairs inside the integer insertion process while preserving all
mixed-run and cross-run no-three constraints.

Run

```bash
python scripts/check_prefix_two_component_rerouting.py
```
