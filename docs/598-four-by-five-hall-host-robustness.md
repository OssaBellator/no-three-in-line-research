# Four-by-five Hall host robustness

The complete `4 x 4` coordinate grid necessarily contains six quotient choices
with singleton residual blockers.  This chapter adds one column while retaining
four quotient labels and two fixed selected rows.

### Theorem PP3ctm -- PROVED / FOUR-BY-FIVE EXTENSION CENSUS

For the canonical label injection into columns `0,1,2,3`, the twelve decoded
pairs have `51` no-three-in-line residual matching extensions.  Their extension
counts are

```text
3 extensions: 4 choices,
4 extensions: 4 choices,
5 extensions: 1 choice,
6 extensions: 3 choices.
```

#### Proof

After fixing a decoded pair in rows zero and one, the checker assigns distinct
remaining columns to rows two and three and rejects every collinear matching.
Direct enumeration gives the stated census. ∎

### Theorem PP3ctn -- PROVED / SINGLE-EXCLUSION ROBUSTNESS

Every decoded pair in the canonical `4 x 5` host has residual blocker number at
least two.  Seven choices have blocker number two and five have blocker number
three.

#### Proof

For each extension family, the checker enumerates residual-cell hitting sets in
increasing cardinality.  No singleton meets every extension.  The first blockers
have the stated sizes. ∎

### Theorem PP3cto -- PROVED / INJECTION-INVARIANT MINIMUM

All `120` injections of the four quotient labels into the five coordinate
columns have minimum blocker number exactly two.

#### Proof

The checker repeats the complete pair, extension, and blocker census for every
ordered injection.  Every injection has minimum two. ∎

Thus one additional coordinate column removes the intrinsic singleton-blocker
obstruction.  The remaining task is to identify such a five-column host inside
the actual prime-patching endpoint geometry and include its source exclusions.

Run:

```bash
python scripts/check_hall_four_by_five_host.py
```
