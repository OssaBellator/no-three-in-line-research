# Extreme support-seven closure of the p=31 three-triple core

## Status

This note keeps AC as the sole active research track and proves AC5ov--AC5ow for the explicit `p=31`, `n=30` three-triple endpoint. It closes the two extreme seven-extra distributions: all seven additional addresses in blue, and all seven in red.

## AC5ov -- complete extreme seven-extra census -- PROVED

For the all-blue family,

\[
|A_R|=0,\qquad |A_B|=7,
\]

the exact search closes

\[
\boxed{480{,}700}
\]

support choices after

\[
\boxed{171{,}025{,}856}
\]

admissible partial states.

For the all-red family,

\[
|A_R|=7,\qquad |A_B|=0,
\]

the search closes

\[
\boxed{657{,}800}
\]

support choices after

\[
\boxed{144{,}149{,}641}
\]

admissible partial states.

Neither search reaches a complete collision-free state of potential at most two.

### Proof

Each family is partitioned into exact contiguous lexicographic shards. The same occurrence-faithful branch-and-bound rule used in AC5os is applied: outside cells are fixed; retained values are assigned to the selected layer-row addresses; collisions and partial potential above two terminate a branch. The committed shard intervals cover both support universes without overlap or omission, and all complete-leaf counts are zero. QED.

## AC5ow -- no extreme seven-extra endpoint improvement -- PROVED

No endpoint with seven additional addresses all in one layer lowers the explicit three-triple state:

\[
\boxed{\Phi\ge3}
\]

for both distributions `(0,7)` and `(7,0)`.

This does not yet close the mixed distributions `(1,6)` through `(6,1)`.

## Deterministic audit

Compile:

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_extreme.cpp -o verify_support_seven_extreme
```

Run shards `0` through `6`. Their expected total ledger is:

- support choices: `1138500`;
- partial states: `315175497`;
- complete potential-at-most-two endpoints: `0`.

## Remaining frontier

1. Search the six mixed seven-extra distributions for the first lower endpoint or a complete closure.
2. Finish the independent barrier-nine switch component from the same three-triple state.
3. Convert any wider-support endpoint into a legal low-barrier switch ordering.
4. Explain structurally why single-layer expansion cannot lower the core.

AC6 and the general no-three-in-line conjecture remain open.
