# Thirteen-pair saturated anchor reservoir

This chapter extends the saturated anchor frontier from eleven and twelve pairs
to thirteen pairs and tests whether the resulting source nests.

## 1. Explicit source

### Theorem PP3cyo — PROVED / SATURATED 13 BY 13 SOURCE

The permutations

```text
P=(9,4,7,3,0,1,12,8,11,10,2,6,5),
Q=(7,12,9,1,4,3,8,0,2,11,5,10,6)
```

form a twenty-six-cell no-three-in-line set on a `13 x 13` grid with degree two
in every row and column. The pairing permutation

```text
(1,0,3,2,5,4,7,8,6,10,12,9,11)
```

partitions the source into thirteen anchor pairs with distinct endpoint rows and
columns.

#### Proof

`scripts/check_prefix_saturated_anchor_reservoir_13.py` checks the permutations,
resource degrees, anchor distinctness, and every determinant. ∎

## 2. Complete run audit

### Theorem PP3cyp — PROVED / 4,096 EMBEDDINGS

All `2^12=4096` ordered compositions of thirteen unary nodes embed on the anchor
lines with globally distinct rows and columns and no mixed-run collinear triple.
The maximum coordinate magnitude in the canonical greedy construction is `180`.

#### Proof

The checker inserts each run in the primitive direction of its anchor line,
skips used resources and mixed forbidden lines, and verifies all triples. ∎

## 3. Source nesting obstruction

### Theorem PP3cyq — PROVED / NESTED SOURCE, NONNESTED ANCHORS

The alternating incidence components have pair-sizes

```text
2, 2, 4, 5.
```

Deleting either two-pair component removes two rows and two columns and leaves an
induced eleven-pair saturated no-three source. But no anchor matching can remain
inside the incidence components: each two-pair component contains rows with no
admissible internal anchor partner.

#### Proof

The cycle lengths of the row permutation induced by `P` and `Q` are `2,4,2,5`.
Deleting either length-two component preserves degree two and inherits no-three
legality. Direct partner enumeration excludes a component-respecting anchor
matching. ∎

## Consequence

Saturated sources are now certified at consecutive sizes eleven, twelve, and
thirteen. The thirteen-source contains genuine eleven-source subsystems, but the
anchor structure does not descend, so no uniform extension rule is established.
