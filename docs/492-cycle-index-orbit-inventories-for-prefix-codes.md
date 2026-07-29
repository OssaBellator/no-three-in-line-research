# Cycle-index orbit inventories for prefix codes

`docs/486` counts optimal schedules with one prescribed multiplicity profile.
A single cycle-index inventory can count all profiles simultaneously and can
therefore expose which risk-class compositions admit genuinely different
marker schedules.

Let a finite survival-preserving automorphism group `G` act on the leaves of a
fixed optimal prefix tree.  Color `i` represents one bank or risk class.

## 1. Multivariate orbit inventory

### Theorem PP3chg -- PROVED / CYCLE-INDEX PROFILE COUNT

Define

```text
Z_G(z_1,...,z_r)
 = (1/|G|) sum_(g in G)
   product_(cycles c of g) (sum_i z_i^|c|).
```

For every multiplicity vector `m=(m_1,...,m_r)`, the coefficient of
`product_i z_i^(m_i)` is exactly the number of `G`-orbits of leaf assignments
having that profile.

#### Proof

An assignment is fixed by `g` exactly when it is constant on every cycle of
`g`.  Choosing color `i` for a cycle of length `|c|` contributes
`z_i^|c|`.  The product records all fixed assignments by profile.  Averaging
the fixed counts is Burnside's lemma. ∎

## 2. Recursive tree evaluation

### Theorem PP3chh -- PROVED / WREATH-PRODUCT INVENTORY

For a recursively specified marker tree, the cycle types of its
survival-preserving automorphism group can be computed bottom-up.  Direct
products combine child cycle multisets, while an allowed equal-survival child
swap joins corresponding child cycles according to the induced permutation.

Consequently, the complete inventory polynomial is computable without listing
all leaf assignments.

#### Proof

Every rooted-tree automorphism is assembled from child automorphisms and
permutations of isomorphic equal-survival child subtrees.  Cycle decomposition
is functorial under these compositions.  Induction over the finite tree gives
all group cycle types and their multiplicities, after which `PP3chg` applies. ∎

## 3. Canonical reconstruction certificate

### Theorem PP3chi -- PROVED / ORBIT-INVENTORY AUDIT

A finite certificate consists of the tree, generators or recursively listed
automorphisms, their cycle-type multiplicities, the averaged inventory
coefficients, and one canonical representative for every nonempty orbit.

Verification checks group action, cycle types, coefficient divisibility by
`|G|`, profile preservation, and that every assignment maps to exactly one
canonical representative.

#### Proof

These are precisely the finite identities used by Burnside averaging and
orbit partitioning.  Any failure identifies one permutation, cycle type,
coefficient, or duplicate/missing representative. ∎

## 4. Stored exact fixture

The audit `scripts/check_prefix_code_orbit_inventory.py` uses the complete
depth-three binary marker tree.  Its automorphism group has order `128`.  For
binary bank colors, the orbit inventory by the number of one-colored leaves is

```text
1, 1, 3, 3, 5, 3, 3, 1, 1.
```

Thus all `256` assignments collapse to `21` schedule orbits.  The Burnside
fixed sums are

```text
128,128,384,384,640,384,384,128,128,
```

and direct canonical-orbit enumeration independently verifies every
coefficient.

## 5. Prime-patching consequence

One symmetry computation now answers every equal-risk multiplicity query on
the same marker tree.  This separates genuinely different geometric schedules
from mere relabelings before any later chord or residue constraints are added.
