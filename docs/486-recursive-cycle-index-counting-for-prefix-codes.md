# Recursive cycle-index counting for prefix codes

`docs/480` applies Burnside's lemma after a finite symmetry group and all optimal
codes have been listed.  Complete marker trees often have recursively generated
automorphism groups, so orbit counts can be computed from cycle data without
listing every labeled schedule.

Fix a rooted prefix tree whose leaves have equal survival, or more generally a
survival-preserving automorphism group `G` acting on an invariant set of optimal
leaf assignments.  Risk class `i` must occupy exactly `m_i` leaves.

## 1. Recursive tree automorphisms

### Theorem PP3cgo -- PROVED / WREATH-PRODUCT TREE SYMMETRY

The survival-preserving automorphism group of a rooted binary tree is computed
recursively.  Nonisomorphic child subtrees contribute the direct product of their
automorphism groups.  Two isomorphic child subtrees contribute their wreath
product with the child swap.  For the complete binary tree,

```text
|G_d|=2 |G_(d-1)|^2,   |G_0|=1.
```

#### Proof

Every rooted automorphism restricts to automorphisms of the child subtrees.  It
may interchange the children exactly when the rooted, survival-labelled
subtrees are isomorphic.  These independent choices give the stated product or
wreath-product decomposition. ∎

## 2. Fixed assignments from cycle lengths

### Theorem PP3cgp -- PROVED / CYCLE-INDEX FIXED COUNT

Let `g in G` have leaf-cycle lengths `ell_1,...,ell_q`.  The number of risk-class
assignments fixed by `g` is the coefficient of
`x_1^(m_1)...x_r^(m_r)` in

```text
product_(h=1)^q (x_1^(ell_h)+...+x_r^(ell_h)).
```

In the two-class case, the number of fixed assignments with `m` leaves of the
first class is the coefficient of `x^m` in
`product_h (1+x^(ell_h))`.

#### Proof

A fixed assignment is constant on every cycle of `g`.  Assigning one risk class
to a cycle contributes the corresponding variable raised to that cycle length.
Multiplying over independent cycles and extracting the required multiplicities
counts exactly the fixed assignments. ∎

## 3. Burnside and orbit--stabilizer certificate

### Theorem PP3cgq -- PROVED / RECURSIVE ORBIT CERTIFICATE

The number of genuinely different optimal schedules is

```text
(1/|G|) sum_(g in G) Fix(g).
```

A canonical representative, its stabilizer size, and the equality
`|orbit| |stabilizer|=|G|` give an exact certificate for each orbit.  Group cycle
types with identical fixed-count polynomials may be aggregated before the
Burnside sum.

#### Proof

Burnside's lemma gives the orbit count.  Orbit--stabilizer proves each individual
orbit size.  Aggregating equal cycle types preserves the sum because their fixed
counts are identical by the preceding theorem. ∎

## 4. Stored exact fixture

The audit `scripts/check_recursive_prefix_code_orbits.py` uses the complete
binary tree of depth three.  Its recursive automorphism-group orders are
`1,2,8,128`.  Among the `binom(8,4)=70` balanced two-risk assignments, the ten
automorphism cycle types have total fixed sum `640`.  Burnside therefore gives
five orbits, with sizes

```text
2, 4, 16, 16, 32
```

and stabilizer sizes `64,32,8,8,4`.

## 5. Prime-patching consequence

Support-chord repair schedules can now be counted and canonicalized modulo the
recursive symmetries of their marker trees.  This avoids carrying thousands of
isomorphic bank assignments into later geometric compatibility checks.
