# Prime-patching parity index supplement: doc 693

| Document | Theorems | Exact content | Evidence boundary |
|---|---|---|---|
| `693` | `PP3del--PP3den` | Reconstructs the canonical eighteenth state, proves all six minimum-four nineteenth cores fail through budget six, gives a row/column-preserving budget-seven correction to 152 points, and computes the exact raw twentieth spectrum with nine minimum-four cores | Exact finite coordinate transition only; no recurrence or promoted row |

## Conservation checks

- The canonical predecessor is reconstructed from the seventeen-block state, the
  eighteenth `P0/-39` block, and the certified six-point correction. This forces
  `(42,378)` and excludes the stale point `(42,193)`.
- The nineteenth deletion and addition multisets agree exactly in both coordinates:

```text
rows:    8,13,16,46,73,75,75,
columns: 1,34,76,77,150,151,152.
```

- The corrected set has 152 distinct points and a full exact triple audit finds no
  collinear triple.
- The next origin advances from `72` to `76`; all 1,032 twentieth attempts are
  evaluated against the corrected state rather than the stale source snapshot.

## Promotion rule

The correction advances the finite chain from eighteen to nineteen blocks and
makes the budget-six lower bound sharp. It does not provide a periodic state
signature, recurrence, or asymptotic coordinate source path. The boundary row
therefore remains `fixture_derived`, candidate completion remains `25/30`, and the
all-`n` theorem remains open.
