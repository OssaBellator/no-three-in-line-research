# Hamilton-cycle chord localization diagnostic

Run

```text
python scripts/check_hamilton_cycle_chord_localization.py \
  experiments/hamilton-cycle-chord-example.json
```

The stored normalized host has a 12-vertex Hamilton successor cycle and eight
additional chords:

```text
0->4, 1->5, 2->6, 3->7,
4->8, 5->9, 6->10, 7->11.
```

Every tail and every head occurs once. The exact output includes:

```text
chord count                              8
sqrt threshold                           3
maximum chord degree                     1
maximal distinct-signature matching      8
matching lower bound                     4/3
canonical cycle length                   9 for every chord
outcome distinct_signature_chord_cycle_bank
```

Each chord and its Hamilton return path gives a distinct canonical cycle state.
The distinguished chord arcs are pairwise tail/head-disjoint, while any repeated
support can occur only on the shared Hamilton backbone.

The checker also reports the sparse-case feedback-hub bound `2e+1`. It rejects
loops, Hamilton successor arcs mislabeled as chords, duplicate chords, and any
failure of the maximal-matching lower bound.
