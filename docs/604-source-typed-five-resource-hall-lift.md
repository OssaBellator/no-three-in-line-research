# Source-typed five-resource Hall lift

`docs/598` showed that an abstract `4 x 5` choice host removes the singleton
residual blocker present in the `4 x 4` model.  This chapter tests the same
enlargement through the repository's actual conditional binary-star interface.

The finite source fixture is
`experiments/binary-resource-star-conditioning-example.json`.  We add one free
left resource and one free right resource, retain its six recorded binary
conflicts, and use the exact partner-fibre rule from
`scripts/check_binary_resource_star_conditioning.py`.

## 1. Lifted conditional host

A decoded choice fixes two left resources in the complete `5 x 5` host.  The
remaining three left resources are matched to the remaining three right
resources after deleting the partner fibre of the selected centre cell.

### Theorem PP3cue — PROVED / SOURCE-TYPED LIFT

The one-free-resource lift is a valid instance of the repository's conditional
binary-resource-star semantics: every recorded conflict touches the fixed left
resource exactly once, and conditioning on its centre deletes precisely that
centre's partner fibre.

#### Proof

The checker uses the six conflict pairs from the stored experiment verbatim and
only adds the new resource with no additional conflict.  Residual completions
are enumerated as perfect matchings after the two selected rows, two selected
columns, and the appropriate partner fibre are removed. ∎

### Theorem PP3cuf — PROVED / ROBUST EMBEDDING CENSUS

Among the `4 * 120 = 480` choices of a second left resource and an injection of
four quotient labels into five right resources:

- `96` give complete twelve-choice decoders;
- `72` have residual blocker number at least two for every decoded choice;
- `24` retain a singleton blocker.

A lexicographically selected best embedding uses second left resource `1` and
choice columns `(1,2,3,4)`.  Its twelve choices have `64` conditional perfect
matchings in total.  Three choices have blocker number two and nine have blocker
number three.

#### Proof

Every one of the twelve syndrome-choice pairs is decoded, checked against the
recorded binary conflicts, and completed by exhaustive residual matching.
Minimum blocker sets are then enumerated from the residual matching family. ∎

### Theorem PP3cug — PROVED / SOURCE IDENTIFICATION LIMIT

The `4 x 5` robustness phenomenon survives the exact finite partner-fibre
interface.  It does **not** yet identify an extra free endpoint resource in the
asymptotic prime-patching host.

Thus this is a source-typed finite bridge, not verification of the Hall ledger
row.

## Exact audit

```bash
python scripts/check_hall_lifted_conditional_star.py
```
