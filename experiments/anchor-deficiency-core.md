# Weighted anchor-deficiency regression

This experiment accompanies:

- [`docs/150-anchor-threshold-ownership-deficiency.md`](../docs/150-anchor-threshold-ownership-deficiency.md);
- [`docs/151-canonical-anchor-deficiency-core.md`](../docs/151-canonical-anchor-deficiency-core.md);
- [`docs/152-weighted-anchor-core-completion.md`](../docs/152-weighted-anchor-core-completion.md);
- [`scripts/check_anchor_deficiency_core.py`](../scripts/check_anchor_deficiency_core.py);
- [`anchor-deficiency-core-example.json`](anchor-deficiency-core-example.json).

Run

```bash
python scripts/check_anchor_deficiency_core.py \
  experiments/anchor-deficiency-core-example.json
```

There are three macros of capacity two and six numerical labels. At threshold
one, labels `0,1,2,3` are acceptable only for macro zero, while labels `4,5`
are acceptable only for macros one and two respectively.

An exact maximum acceptable matching has size four. With the checker's
lexicographic tie-breaking it leaves labels `0,1` unmatched and leaves one slot
unmatched in each of macros one and two.

The alternating-reachability core is

```text
X = {0,1,2,3},
Y = the two slots of macro 0,
|X|-|Y| = 2.
```

There is no acceptable edge from `X` to the complement of `Y`, so every full
balanced ownership needs two assignments across this all-bad cut.

For the unmatched labels and slots, the completion matrix is

```text
       macro 1   macro 2
0         6         7
1         5         8
```

Its slot-expanded energy is

```text
E_slot = 26,
d = 2,
E_slot/d = 13.
```

The exact minimum-bottleneck completion uses weights `7` and `5`, so

```text
minimum bottleneck = 7 <= 13 = E_slot/d.
```

The checker logic was reproduced and executed locally against this fixture on
25 July 2026. It returned maximum acceptable matching size four, the displayed
Dulmage core, deficiency two, and minimum bottleneck seven.

The finite fixture verifies the matching/core identities. It does not establish
the asymptotic controller-slack hypotheses of PP3vy.