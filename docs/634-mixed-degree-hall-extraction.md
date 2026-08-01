# Mixed-degree Hall reserve extraction

The sharp theorem in `docs/628` assumes all three restricted forbidden families
have maximum degree two.  The recorded Hall interface already treats the partner
fibre as matching-shaped.  This chapter exploits that mixed degree profile.

## 1. Collision-degree reduction

### Theorem PP3cxq -- PROVED / MIXED-DEGREE COLLISION BOUND

Suppose the partner restriction is a partial matching and the source and
host-defect restrictions have maximum degree two on both resource sides.  The
resource collision graph on either side has maximum degree at most four.

#### Proof

A degree-`d` forbidden family creates at most `d(d-1)` collision neighbours at a
resource vertex.  The degree profile `(1,2,2)` therefore contributes at most

```text
1*0 + 2*1 + 2*1 = 4.
```

The matching-shaped family creates no collision edge.  ∎

## 2. Sharp reserve threshold

### Theorem PP3cxr -- PROVED / TWENTY-EIGHT-RESOURCE INTERFACE

Twenty-six unused resources per side force six resources on which all three
restricted families are partial matchings.  Hence twenty-eight resources per side
before the selected local pair suffice for the six-resource Hall core.

#### Proof

A graph of maximum degree four has an independent set of size at least
`ceil(N/5)` by greedy deletion.  For `N=26` this is six.  Choose independent sets
on the left and right collision graphs; no two selected resources share a
forbidden neighbour in any family, so every restriction becomes a partial
matching.  Apply the six-resource completion theorem from `docs/622`.  ∎

## 3. Sharpness

### Theorem PP3cxs -- PROVED / TWENTY-FIVE-RESOURCE OBSTRUCTION

The constant twenty-six is sharp under only the mixed degree hypotheses.
Twenty-five resources can have collision graph equal to five disjoint copies of
`K5`, whose independence number is five.

Each `K5` is the edge-disjoint union of the two Hamilton cycles with steps one
and two modulo five.  Realize each cycle as the collision graph of one degree-two
forbidden family by assigning a unique opposite-side neighbour to every cycle
edge.  The matching-shaped partner family may be empty.

Thus the source obligation is reduced from three degree-two families and thirty-
eight total resources to one matching-shaped plus two degree-two families and
twenty-eight total resources.  The actual asymptotic host still has to prove those
degree statements.
