# Recorded shell catalogue coset absence

The `docs/517` source actions have cycle-resource vectors

```text
(1,0,1), (1,1,0), (0,1,1).
```

Their integer span is the even-coordinate-sum sublattice.  This chapter checks
whether the recorded source catalogue already contains the odd action needed by
the conditional repair of `docs/595`.

### Theorem PP3ctv -- PROVED / RECORDED ACTION PARITY

Every recorded source action has coordinate sum two, and every nonnegative
integer schedule formed from the recorded catalogue has even total cycle sum.

#### Proof

This follows directly from the three stored incidence columns and is checked
over a finite generating box as a diagnostic of the parity formula. ∎

### Theorem PP3ctw -- PROVED / ODD-COSET SOURCE ABSENCE

The recorded source catalogue contains no odd-coordinate-sum action and therefore
cannot realise the coset-crossing action required in `docs/595`.

#### Proof

The complete recorded catalogue consists of the three displayed columns.  Each
lies in the even-sum lattice, so no catalogue element crosses the missing coset.
∎

### Theorem PP3ctx -- PROVED / CONDITIONAL UNIT-ACTION COST

For each unit odd cycle action, exact target service `(12,10,8)` has a
nonnegative integer schedule with sixteen active controls, using the odd action
twice.  The original schedule uses fifteen active controls, so the conditional
throughput penalty is `1/20` per twenty slots.

#### Proof

The checker exhaustively solves the three augmented integer systems.  The
minimum positive odd-action count is two and the minimum total active count is
sixteen in each case. ∎

The lattice repair remains conditional because no such odd action is present in
the recorded clean-macro source catalogue.

Run:

```bash
python scripts/check_shell_recorded_odd_action_absence.py
```
