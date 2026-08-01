# Endpoint-reusing support-chord census

The convex point embedding in `docs/594` has no collinear triples.  This chapter
uses an ancestry-sensitive chord model instead: every unary node carries the
chord joining the two endpoint lines at the endpoints of its subtree interval.
Unary nodes in one maximal unary chain have the same interval and hence reuse
the same chord.

### Theorem PP3cts -- PROVED / REPEATED-CHORD DP

A dynamic program indexed by encoded size, binary-node count, root type, and top
unary-chain length exactly counts repeated support-chord pairs.

#### Proof

Adding a unary root above a unary child of top-chain length `t` creates exactly
`t` new repeated-chord pairs.  Adding it above a leaf or binary root starts a new
chain.  A binary root combines the two child totals without creating a cross
collision.  These constructors are disjoint and exhaustive. ∎

### Theorem PP3ctt -- PROVED / PROFILE AGGREGATE

At encoded size thirty with nine binary nodes, the family size is

```text
168212023980,
```

and the aggregate repeated-chord-pair count is

```text
925166131890.
```

The exact mean is `11/2`.

#### Proof

The checker evaluates the recurrence through size thirty and independently
checks the family count against the Lagrange profile formula. ∎

### Theorem PP3ctu -- PROVED / ENDPOINT-REUSE TYPE GAP

The census supplies a nonzero ancestry-sensitive geometric incidence coordinate,
but coincident chords are not legal distinct support cells in the prime-patching
grid.

#### Proof

The coordinate is defined by actual interval endpoints and distinguishes unary
chain structure, unlike terminal inventory.  However two nodes on one unary
chain receive identical chord endpoints.  A further perturbation or
source-defined endpoint multiplicity rule is required. ∎

Run:

```bash
python scripts/check_prefix_repeated_chord_pairs.py
```
