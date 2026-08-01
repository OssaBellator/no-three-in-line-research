# State-only support-cell decoder obstruction

`docs/576` identifies the unary-to-unary risk with consecutive nesting of
state-one support terminals in the eliminated automaton encoding.  A coordinate
decoder might try to assign one fixed support-chord cell type to each automaton
state and compute risk from the resulting cell multiset.  This chapter proves
that such a state-only decoder cannot recover the nesting statistic.

## 1. Fixed terminal inventory

### Theorem PP3crq -- PROVED / PROFILE TERMINAL MULTISET

For original leaf count thirty and encoded binary profile nine, every encoded
object has terminal inventory

```text
(state 0, state 1, state 2)=(10,11,9).
```

The profile contains exactly `168212023980` objects.

#### Proof

The encoded unary count is `30-1-2*9=11`, the encoded leaf count is `9+1=10`,
and the binary count is nine.  These are precisely the three terminal types in
the automaton decoder.  The exact profile coefficient gives the family size. ∎

## 2. State-only cell labels do not determine risk

### Theorem PP3crr -- PROVED / TERMINAL-MULTISET OBSTRUCTION

Within the same fixed terminal inventory, there are

```text
367479684
```

objects of support-nesting risk zero and

```text
92378
```

objects of risk ten.  Therefore no statistic depending only on the multiset of
state-labelled support cells can equal the nesting risk.

#### Proof

The exact risk dynamic program gives positive coefficients at risks zero and ten.
By `PP3crq`, every object in both subfamilies has the same terminal multiset.
Any state-only cell assignment produces the same cell multiset for both and
cannot distinguish their risks. ∎

## 3. Minimum information required by a geometric decoder

### Theorem PP3crs -- PROVED / ANCESTRY-SENSITIVE DECODER REQUIREMENT

Any exact coordinate realization of the support-nesting risk must retain at
least parent-child incidence between state-one terminals, or equivalent
support-chord ancestry data.  Terminal coordinates or state labels alone are
insufficient.

#### Proof

The risk counts state-one parent/state-one child edges.  `PP3crr` shows that all
zero-order terminal data can remain fixed while the edge count varies from zero
to ten.  Hence some incidence information is necessary. ∎

## 4. Exact audit

Run

```bash
python scripts/check_prefix_state_only_cell_obstruction.py
```

The result does not refute a richer support-chord decoder.  It specifies the
minimum kind of geometric state that such a decoder must expose.
