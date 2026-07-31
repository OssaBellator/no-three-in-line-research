# A choice-grid decoder for the cylinder Hall microcensus

`docs/562` independently defined a six-state cylinder microcensus and recovered
the stored Hall quotient kernels.  The missing interface was a type-level map to
one of the established PP3 endpoint objects.  This chapter connects the quotient
choice labels to the complete same-side two-resource choice grid of `docs/159`.

The quotient state is `s in Z/3Z`, the local choice is `c in Z/4Z`, and the
complete four-by-four same-side grid consists of ordered pairs `(a,b)` with
`a!=b`.

## 1. State-level decoding is impossible

### Theorem PP3cqa -- PROVED / CHOICE-GRID CARDINALITY MISMATCH

No injective decoder from the six cylinder microstates to the twelve compatible
ordered pairs of a complete four-by-four same-side choice grid exists.

#### Proof

The grid has `4*3=12` ordered distinct pairs, while the microcensus has six
states.  Pigeonhole. ∎

Thus a grid pair must be carried by a state together with a local choice, not by
the state alone.

## 2. Exact quotient-choice bijection

### Theorem PP3cqb -- PROVED / CYLINDER-TO-GRID PAIR CODE

The map

```text
psi(s,c)=(c, c+s+1 mod 4)
```

is a bijection from `Z/3Z x Z/4Z` to the twelve ordered pairs `(a,b)` with
`a!=b`.

#### Proof

For fixed `c`, the three values `s=0,1,2` give the three elements of `Z/4Z`
different from `c`.  Distinct first coordinates or distinct differences give
distinct pairs, so all twelve compatible pairs occur exactly once. ∎

This decoder is independent of the Hall transition matrices.  It uses only the
already defined syndrome and local-choice types.

## 3. Microscopic lifting of every grid pair

### Theorem PP3cqc -- PROVED / TWO-ORIENTATION GRID WITNESSES

For each of the two cylinder gadgets and each compatible grid pair, exactly two
choice-labelled microscopic transitions decode to that pair, one from each
orientation.  After quotienting orientation, every grid pair has exactly one
choice witness.

#### Proof

Fix `(a,b)`.  By `PP3cqb` there is one quotient pair `(s,c)` with
`psi(s,c)=(a,b)`.  The two microstates `(s,0)` and `(s,1)` both admit choice `c`,
and the cylinder transition rule gives one target from each.  No other syndrome-
choice pair decodes to `(a,b)`. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_hall_choice_grid_decoder.py
```

The checker enumerates all twelve grid pairs, verifies bijectivity, and audits
all 24 choice-labelled transitions per gadget.

## 5. Prime-patching consequence

The independent Hall microcensus now has a precise repository-level role: its
quotient choices can enumerate a complete two-resource choice grid.  What remains
is geometric rather than combinatorial—identify the four abstract choices with
actual endpoint cells at two fixed prime-patching resources and verify that the
cylinder transition witness decodes to the corresponding local matching move.
The Hall ledger row remains fixture-derived until that coordinate map exists.
