# Atomic packet correction closes the linear residue interface

PX305--PX310 prove strict improvement or a growing clean-star child whenever the
old packet mass is superlinear relative to the correction block.  The residual
range is linear because the aggregate Bernoulli argument asks for a positive
first-order gap.

For lexicographic termination, a positive total gap is stronger than necessary.
One may inspect a single packet correction.  If it is blocked by an inherited
position constraint, the old packet triple itself is already a clean-star child.
If it is admissible, its exact support-one creation formula gives either strict
improvement or a prospective clean-star/loaded-line child.

Thus every positive packet residue satisfies the strict-sign-or-child interface.
The remaining issue is absorption of the resulting bounded children, not packet
dispersion.

## 1. Blocked corrections are selected-star children

Retain the correction graph of PX300.  Call an edge `e={r,s}` **admissible** when
both prospective swapped cells avoid the inherited ordinary forbidden-position
graph.  Otherwise call it blocked.

Let `B` be any family of blocked correction edges and put

\[
D_B=\sum_{e\in B}w_e.
\]

### Theorem PX319 -- PROVED

Some selected point centres an endpoint-disjoint clean star of order at least

\[
\boxed{
\left\lceil\frac{2D_B}{hK}\right\rceil
}
\]

whenever `D_B>0`.

In particular, every individual blocked packet defect may be removed from the
unassigned packet coordinate and designated as a clean-star child at the next
lexicographic level.

### Proof

The sum of the weighted correction degrees over all selected rows is `2D_B`.
Hence one row `r` has weighted degree at least `2D_B/h`.  PX303 converts that
incidence into an endpoint-disjoint selected-point star of order at least
`mu(r)/K`, giving the displayed integer bound.

Every packet certificate counted by `w_rs` is the collinear triple consisting
of the selected centre `P_r`, the selected partner `P_s`, and its certifying
background anchor.  It is therefore literally a clean-star ray.  Reclassifying
one such ray as a designated child lowers the unassigned packet coordinate
without changing any shallower coordinate. \(\square\)

The blocked case is consequently a child conversion, not a failed move.

## 2. Exact atomic correction sign

Fix one admissible correction edge `e`.  Let `w_e` be its old packet
destruction, let `f_e^1,f_e^2` be its two prospective cells, and use the exact
quantities of PX307:

\[
c_e=\mu_e(f_e^1)+\mu_e(f_e^2)+\lambda_e.
\]

### Theorem PX320 -- PROVED

Executing only the correction `e` satisfies

\[
\boxed{
\Phi(M^e)-\Phi(M)
\le
-w_e+c_e.
}
\]

Therefore `w_e>c_e` gives a deterministic strict improvement.

### Proof

The correction destroys all `w_e` old packet certificates assigned to its row
pair.  Every newly created triple contains at least one of the two new cells,
and PX307 counts these triples exactly by `c_e`.  Any additional old triple
destroyed by deleting the two original selected cells only strengthens the
inequality. \(\square\)

## 3. Failure of atomic sign is structured

Assume the line-occupancy bound `K` from PX308.

### Theorem PX321 -- PROVED

If an admissible correction edge is not strictly improving, then at least one
of the following prospective children exists after executing it.

1. A new cell centres an endpoint-disjoint clean star of order at least

   \[
   \boxed{
   \left\lceil\frac{w_e}{3K}\right\rceil.
   }
   \]

2. The line through the two new cells contains at least

   \[
   \boxed{
   \left\lceil\frac{w_e}{3}\right\rceil+2
   }
   \]

   selected/background points, including the two new cells.

### Proof

Nonimprovement in the sufficient inequality of PX320 implies `c_e>=w_e`.
Among the three nonnegative terms

\[
\mu_e(f_e^1),\quad \mu_e(f_e^2),\quad\lambda_e
\]

one is at least `ceil(w_e/3)`.

If a `mu` term is large, PX228 gives a clean star of order at least that term
divided by `K`.  If `lambda_e` is large, its counted fixed points lie on the
line through the two new cells, giving the displayed loaded-line occupancy.
\(\square\)

All other triples created by the atomic correction can be assigned to the same
deeper generation.  Historical-position and packet-complement constraints from
PX278 prevent the paid parent packet certificates from returning.

## 4. Packet strict-sign-or-child without a mass threshold

### Corollary PX322 -- PROVED

For every state with `D_pkt(M)>0`, the packet sector satisfies the exact
strict-sign-or-child interface of PX280.

More explicitly, at least one of the following holds.

1. blocked packet mass is converted to a selected clean-star child by PX319;
2. one admissible correction strictly lowers the full triple potential;
3. one admissible correction removes its parent packet mass and creates a
   prospective clean-star or loaded-line child quantified by PX321.

No lower bound such as `D_pkt>=12hK^2` is required.

### Proof

Choose a positive-weight correction edge.  If it is blocked, use PX319.  If it
is admissible, apply PX320 and PX321.  In the nonimproving case, execute the
correction, remove its old packet certificates from the current unresolved
coordinate, and assign the complete new-certificate list to the next level.
The first affected lexicographic coordinate strictly decreases. \(\square\)

PX310 remains useful because it gives a *large* child or an immediate
improvement from large mass.  PX322 closes the previously open linear packet
residue at the causal-interface level.  What remains is the common terminal
absorption problem for the bounded clean-star/loaded-line children.

## 5. Verification

Run

```bash
python scripts/verify_product_atomic_packet_child.py
```

The verifier exhausts integer first-order ledgers, checks the strict-or-star-or-
line trichotomy, and validates the blocked-mass selected-star averaging bound.
