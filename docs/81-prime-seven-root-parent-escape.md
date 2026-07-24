# Joint parent escape in the balanced prime-seven root family

CMR145--CMR148 show that complete parent-layer moves escape every terminal
four-core component at side five. The balanced non-reciprocal family
`H_7` from CMR120 provides a stronger test: it is the actual root law used by
the recursive `7^k` construction.

The exact root census shows that a one-layer enlargement is still insufficient.
Two root states are trapped under every four-endpoint move and every complete
single-layer move, but both are escaped by an ordered joint move of the two
complete layers.

## 1. Root-family potential census

Recall the seven permutations

```text
H0 = (0,2,6,5,3,4,1)
H1 = (1,0,4,6,2,3,5)
H2 = (2,3,5,4,1,6,0)
H3 = (3,5,0,2,6,1,4)
H4 = (4,1,3,0,5,2,6)
H5 = (5,6,2,1,4,0,3)
H6 = (6,4,1,3,0,5,2).
```

The balanced root family consists of the `42` ordered pairs `(H_i,H_j)` with
`i ne j`.

### Theorem CMR149 — PROVED BY EXHAUSTIVE FINITE CHECK

The exact real-triple potential distribution in the `42` root states is

| potential | number of root states |
|---:|---:|
| 1 | 4 |
| 3 | 2 |
| 4 | 2 |
| 5 | 12 |
| 6 | 2 |
| 7 | 8 |
| 8 | 4 |
| 9 | 8 |

In particular the balanced root family itself contains no potential-zero state,
but it has four states of minimum potential one.

### Proof

The checker evaluates all

\[
42\binom{14}{3}
\]

point triples by exact integer determinants. ∎

## 2. Two root states resist every one-layer escape

Two of the four potential-one root states have a direct potential-zero
four-endpoint move. The remaining two are

```text
R0 = H3 = (3,5,0,2,6,1,4)
R1 = H4 = (4,1,3,0,5,2,6)

R'0 = H4
R'1 = H3.
```

### Theorem CMR150 — PROVED BY EXHAUSTIVE FINITE CHECK

For each of the two displayed ordered states:

1. there are `308` allowed four-endpoint moves;
2. every four-endpoint child has potential at least one;
3. exactly three four-endpoint children have potential one;
4. there are `1158` allowed complete single-layer moves;
5. every complete single-layer child has potential at least one;
6. exactly three complete single-layer children have potential one.

Thus neither the terminal four-board nor the complete one-layer parent bank can
escape these states.

### Proof

The checker enumerates every choice of layer, every four-column subset, every
row rematching, and every complete-layer rematching. It rejects old cells and
opposite-layer collisions and evaluates the potential of every surviving
state. ∎

This is stronger than the `N=4` local trap: merely enlarging the endpoint
support inside the same layer does not suffice.

## 3. Ordered joint parent escape

### Theorem CMR151 — PROVED BY EXACT CERTIFICATES

Both trapped root states have an ordered complete two-layer escape to potential
zero.

For `(R0,R1)=(H3,H4)`, use

```text
G0 = (1,0,2,5,4,6,3)
G1 = (3,6,4,1,2,0,5).
```

Move layer zero first from `R0` to `G0`, then move layer one from `R1` to `G1`.
Every point is moved at both stages, `G0` avoids the old layer `R1`, and the
final layers `G0,G1` are disjoint. Their union has no real collinear triple.

For the reversed root state `(H4,H3)`, use

```text
G'0 = (1,0,2,6,4,3,5)
G'1 = (5,3,4,0,2,6,1).
```

Again use the order zero then one. The final state is saturated and no-three.

### Proof

The movement, intermediate-disjointness, final-disjointness, permutation, and
all determinant conditions are checked exactly. ∎

### Corollary CMR152 — PROVED FOR THE BALANCED `p=7` ROOT FAMILY

Every potential-one state in the balanced prime-seven root family is escaped by
one of:

1. a four-endpoint move;
2. an ordered joint complete-parent move.

A complete single-layer parent bank is not enough in general. The smallest
successful inherited escape object in this exact model is the ordered joint
parent bank.

## 4. Corrected general parent-escape target

The computational evidence at the first two balanced prime bases now has a
consistent form:

- at `p=5`, every terminal four-core component is escaped by an ordered complete
  two-layer bank;
- at the recursive `p=7` root, the only one-layer-parent traps are also escaped
  by an ordered complete two-layer bank.

The next theorem should therefore be stated for a **joint inherited parent
bank**, not for one layer alone.

### Joint parent-escape lemma — OPEN

Let a four-endpoint one-target core arise inside a balanced recursive
prime-power state, and let `A` be its smallest recorded ancestor prefix block.
Allow an ordered rematching of the two inherited layer blocks over `A`. Prove
that either

1. one joint state lowers the fixed global baseline; or
2. failure forces a quotient/carry certificate already paid by the ancestor
   node; or
3. the core lifts to the next ancestor with a strictly decreasing reverse-scale
   signature.

The missing ingredient is no longer local existence of an escape state. It is
a scale-compatible bound for the collateral of the ordered joint parent bank.

No all-`n` theorem is claimed here. The complete root census and all move checks
are in
[`scripts/verify_prime_seven_root_parent_escape.py`](../scripts/verify_prime_seven_root_parent_escape.py).
