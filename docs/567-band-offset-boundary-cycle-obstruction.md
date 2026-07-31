# Band-offset boundary seams and bounded-cycle obstruction

`docs/561` showed that placing the explicit side-four and side-seven candidate
blocks on one common diagonal makes every dihedral seam illegal.  A natural next
attempt is to move the next block into a different horizontal band.  This chapter
audits all bounded vertical offsets in a fixed exact window and then tests whether
locally legal seams compose into a repeatable zero-drift controller.

Let `P` and `Q` be the coordinate blocks from `docs/561`, with side lengths four
and seven.  Each has four distinct dihedral variants.  A transition

```text
(X,i) --h--> (Y,j)
```

places variant `j` of `Y` immediately to the right of variant `i` of `X`, with
vertical-origin difference `h`.

## 1. Exact finite band-offset seam graph

### Theorem PP3cpx -- PROVED / BOUNDED OFFSET SEAM ENUMERATION

For a fixed offset radius `H`, legality of every candidate transition is an exact
finite coordinate test.  For `H=24`, the explicit four/seven catalogue has 282
legal transitions among the eight typed variants.  The minimum absolute legal
offsets by ordered block type are

```text
P->P : 10,
P->Q : 16,
Q->P : 16,
Q->Q : 24.
```

#### Proof

There are four variants of each block, four ordered type pairs, and
`2H+1=49` offsets.  Translate the right block by its left block's width and the
candidate offset, then test every triple of the union by the integer determinant
criterion.  Exhaustion gives the transition set and the four minima. ∎

Thus the diagonal obstruction is not an obstruction to every isolated seam:
large enough band changes do produce locally legal joins.

## 2. Local seam legality is not compositional

### Theorem PP3cpy -- PROVED / SHORTEST ZERO-DRIFT CYCLE OBSTRUCTION

Form the directed offset-labelled graph from `PP3cpx`.  Among its zero-total-
offset closed walks there are

```text
242 walks of length two,
84 walks of length three,
1172 shortest mixed P/Q walks of length four.
```

After placing two periods of each walk, every one contains a collinear triple.
Hence no zero-drift controller of length two or three, and no shortest mixed
zero-drift controller, is globally legal.

#### Proof

Enumerate closed walks with total offset zero.  Reconstruct two consecutive
periods in absolute coordinates and apply the determinant test to the full point
set, not merely adjacent block pairs.  The audit finds zero globally legal
examples in all three finite classes. ∎

The first length-two witness is the horizontal triple

```text
(0,0), (3,0), (8,0).
```

Horizontal witnesses are the most common failure: 207 of 242 length-two walks,
54 of 84 length-three walks, and 553 of 1172 shortest mixed length-four walks.

## 3. Required state enlargement

### Theorem PP3cpz -- PROVED / LONG-RANGE LINE-STATE REQUIREMENT

A boundary seam automaton whose state records only block type, dihedral variant,
and vertical origin cannot certify global no-three-in-line legality.  Any sound
finite-state boundary compiler must additionally retain enough line-incidence
history to detect triples whose first two points lie in nonadjacent earlier
blocks.

#### Proof

Every transition in the walks of `PP3cpy` is locally legal by construction, and
the total offset returns to zero.  Nevertheless the full two-period placement is
illegal.  Therefore the transition state omits information relevant to future
legality.  The displayed witnesses are concrete indistinguishable histories for
the local seam state and force a history refinement. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_boundary_band_offset_cycles.py
```

The checker reconstructs the 282-edge graph, the four sharp minimum offsets, all
short zero-drift classes above, and their first long-range witnesses.

## 5. Prime-patching consequence

Band permutation rescues isolated four/seven joins but not yet a repeatable
marker controller.  The next boundary object must be a line-state automaton,
a seam corrector that destroys inherited row lines, or a different local block
catalogue.  The synthetic boundary ledger row is not promoted.
