# Ancestry-labelled support-interval risk

`docs/582` proved that terminal state counts cannot recover the prefix
support-nesting risk.  This chapter adds the missing parent-child incidence and
one canonical coordinate label while retaining the exact coefficient dynamic
program.

Use the size-preserving unary-binary encoding of `docs/564--576`.  Give each
encoded subtree its canonical inorder interval.  A `U` parent with a `U` child
contributes one nesting edge, labelled by the size of the child subtree; this is
the span of its encoded support interval.

## 1. Incidence sufficiency

### Theorem PP3csi -- PROVED / ANCESTRY-AWARE RISK RECURRENCE

The state tuple

```text
(encoded size, binary nodes, root type)
```

together with total object count, total `U-U` edge count, and total `U-U`
interval span is closed under the unary and binary constructors.

#### Proof

A unary root preserves the child statistics.  If the child root is unary it adds
one nesting edge and adds the child size to the span.  A binary root forms an
ordered product, so counts multiply and both additive statistics satisfy the
standard product-rule convolution. ∎

### Theorem PP3csj -- PROVED / EXACT SUPPORT-SPAN AGGREGATE

At original leaf count thirty and encoded binary profile nine, the exact family
size is

```text
168212023980.
```

The aggregate nesting-edge count remains

```text
638045608200,
```

with mean `110/29`.  The aggregate ancestry-labelled interval span is

```text
4963626417750,
```

with exact mean

```text
7186475/243542.
```

#### Proof

Evaluate the finite recurrence from `PP3csi` through encoded size thirty.  The
count agrees with the closed profile formula, and exact integer accumulation
gives the two displayed moments. ∎

## 2. Coordinate interpretation and remaining gap

### Theorem PP3csk -- PROVED / STATE-COUNT SEPARATION BY SPAN

The interval-span statistic is genuinely ancestry-sensitive: it cannot be
reconstructed from the fixed terminal inventory `(10,11,9)`, because the
recurrence charges the sizes of specifically nested child subtrees.  Thus it
supplies the first nontrivial coordinate-labelled aggregate beyond terminal
counts.

It is not yet a prime-patching geometric risk because the canonical inorder
intervals have not been embedded as actual support chords in the grid.

#### Proof

Terminal inventory contains no parent relation or child size.  The span charge
uses both, so two encodings with the same inventory can receive different
charges.  The exact DP stores that additional incidence. ∎

## 3. Exact audit

Run

```bash
python scripts/check_prefix_ancestry_span_dp.py
```
