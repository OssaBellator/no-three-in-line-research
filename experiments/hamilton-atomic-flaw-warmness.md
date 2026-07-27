# Atomic Hamilton flaw warmness

Run:

```bash
python scripts/check_hamilton_atomic_flaw_warmness.py \
  experiments/hamilton-atomic-flaw-warmness-audit.json
```

An atomic flaw records one selected collinear triple together with the two or
three signed pair assignments that own its cells.  In a Hamilton pair cycle
those assignments form a directed path forest, so their exact probabilities
are

```text
two owners:   1/[4(m-1)_2]
three owners: 1/[8(m-1)_3].
```

For a two-owner flaw, choose either owner uniformly and flip its orientation.
For a three-owner flaw, rotate the three successors and choose the three fresh
signs uniformly.  The labelled deletion maps are injective and their images are
disjoint from the target flaw.

The exact audit is:

| `m` | states | two-owner flaws | three-owner flaws | two-owner warmness | three-owner warmness |
|---:|---:|---:|---:|---:|---:|
| 4 | 96 | 16 | 208 | 12 | 6 |
| 5 | 768 | 144 | 1,888 | 24 | 24 |
| 6 | 7,680 | 256 | 7,904 | 40 | 60 |

Every deletion output has multiplicity one.  Thus the deletion output is uniform
on exactly

```text
two-owner:   2|A| states,
three-owner: 8|A| states,
```

and its density relative to the uniform signed Hamilton measure is bounded by

```text
M_2 = 2(m-1)(m-2),
M_3 = (m-1)(m-2)(m-3).
```

These polynomial warm-start constants feed the total-variation regeneration
bound in `docs/309`.
