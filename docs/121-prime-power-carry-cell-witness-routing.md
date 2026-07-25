# Heavy thin carry cells route internally or through an earlier exit depth

CMR303 leaves one local alternative in which many canonical thin-blocker events
share one prefix carry cell and one projective direction.  The third point of
such a line has an exact primitive continuation parameter.  Its p-adic
valuation decides whether the event stays inside the carry cell or exits it at
a strictly earlier depth.

Work in a normalized board of size

\[
t=p^h.
\]

Let a compatible candidate line contain Hall endpoint cells `P,Q`.  Write their
exact displacement as

\[
Q-P=G(u,v),
\]

where

\[
G=\gcd(|Q_x-P_x|,|Q_y-P_y|)>0
\]

and `(u,v)` is a primitive integer direction.  Put

\[
b=v_p(G).
\]

Every other grid point `W` on the line has a unique integer parameter

\[
W=P+q(u,v).
\]

## 1. Exact prefix-membership criterion

### Theorem CMR310 — PROVED

The two Hall endpoints lie in one common depth-`b` prefix carry cell.  The third
point `W` lies in that same cell if and only if

\[
\boxed{p^b\mid q.}
\]

If `p^b` does not divide `q`, then

\[
c=v_p(q)<b
\]

is exactly the first separation depth of `P` and `W`, and their projective
direction modulo `p` is the same as the line direction of `P,Q`.

### Proof

The displacement `Q-P` is divisible by `p^b` in both coordinates, so the Hall
endpoints have the same two coordinate residues modulo `p^b`.

Because `(u,v)` is primitive, at least one of `u,v` is a `p`-adic unit.  Hence
both coordinates of

\[
W-P=q(u,v)
\]

are divisible by `p^b` exactly when `q` is divisible by `p^b`.  If
`c=v_p(q)<b`, division of `W-P` by `p^c` leaves a nonzero projective residue
which is a unit multiple of `[u:v]`. ∎

## 2. Heavy-cell routing

### Theorem CMR311 — PROVED

Let `F` be `M` compatible line events whose Hall endpoint pairs lie in one
depth-`b` carry cell and have one common projective direction.  Choose one third
witness for every event.  At least one of the following holds.

1. **Internal routing.** At least
   \[
   \boxed{\operatorname{ceil}(M/2)}
   \]
   witnesses remain in the same depth-`b` cell.
2. **Crossing routing.** At least
   \[
   \boxed{\operatorname{ceil}(M/2)}
   witnesses leave the cell.

When `b>=1`, the crossing population contains a subfamily of size at least

\[
\boxed{
\operatorname{ceil}\left(\frac{M}{2b}\right)
}
\]

with one common strict exit depth `c<b` and the original projective direction.

### Proof

Partition the events by the divisibility criterion in CMR310.  One class has
size at least `ceil(M/2)`.  In the crossing class, the integer
`v_p(q)` belongs to `{0,...,b-1}`.  Pigeonholing those `b` possibilities gives
the final bound. ∎

## 3. Internal scaling

### Theorem CMR312 — PROVED

Suppose one event is internally routed and `b>=1`.  Subtract the common depth-
`b` prefix residue from all three cells and divide both coordinates by `p^b`.
The result is a compatible collinear triple in an integer board of side

\[
\boxed{t/p^b.}
\]

The operation preserves distinct source coordinates, distinct target
coordinates, and the primitive projective direction after removal of any
additional common power of `p`.

### Proof

All three cells have the same coordinate residues modulo `p^b`, so subtraction
and division produce integer coordinates in `[0,t/p^b-1]`.  Affine determinants
scale by `p^{2b}`, hence collinearity is preserved.  Coordinate equality is
preserved under the injective affine rescaling, and the direction statement is
immediate. ∎

## 4. Consequence for thin blockers

### Corollary CMR313 — PROVED

Apply CMR311 to the heavy-cell alternative in CMR304 or CMR305.  A sharp
width-two or width-three blocker therefore yields at least one of:

1. a scaled internal population in a strict p-adic subboard when `b>=1`;
2. a crossing population with one common exit depth `c<b` and one projective
   direction;
3. a top-depth population with `b=0`, already owned by the parent-scale
   direction ledger.

Quantitatively, before the final factor `2b`, the routed population has size

\[
\Omega_p\left(\frac{\sqrt t}{\log t}\right).
\]

### Proof

CMR304 and CMR305 supply the heavy-cell population.  CMR311 routes at least half
of it, and CMR312 handles the internal case.  When `b=0`, every integer
continuation parameter is divisible by `p^b=1`, so the cell is the parent-scale
cell and no finer routing is asserted. ∎

## 5. Remaining no-return statement

The heavy-cell obstruction now has an exact local transition.  Internal events
scale to a smaller p-adic rectangle; external events carry a strict exit depth;
and depth zero is assigned to the parent direction ledger.  What remains is to
show that the closure process cannot repeatedly revisit the same scaled
rectangle or exit signature after coarse repairs.  That is a bounded-reuse
problem, not a missing local classification.

No all-`n` theorem is claimed here.  Prefix membership, exit depths, internal
scaling, and routing counts are checked in
[`scripts/verify_prime_power_carry_cell_routing.py`](../scripts/verify_prime_power_carry_cell_routing.py).
