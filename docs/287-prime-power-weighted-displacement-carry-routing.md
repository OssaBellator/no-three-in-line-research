# Exact-displacement packings route through one prefix carry cell

CMR1469 produces a fractional bank of ordered owner-partner incidences with
one exact displacement.  This chapter routes that bank through the existing
carry-cell dichotomy in weighted form.

Fix a response owner of matching side `d` inside an inherited envelope

\[
t=p^k.
\]

Let one CMR1469 class have first-separation depth `s`, primitive vector `q`,
and exact displacement

\[
v=mq,
\qquad v_p(|m|)=s.
\]

An **incidence copy** consists of a candidate triple `T`, its canonical owner
`a(T)`, and one chosen nonowner partner `b` in the exact-displacement class.
It has weight `z_T`.  If both nonowner cells qualify, the candidate supplies
two copies.  Let the total copy mass be `mu`.
For one copy, denote the other nonowner cell of `T` by `w`.

## Endpoint prefix cell

### Theorem CMR1470 -- PROVED

For every incidence copy,

\[
b=a+v
\]

and `a,b` lie in one common depth-`s` two-coordinate prefix cell.  At depth
`s+1` they lie in distinct child cells with one fixed nonzero offset

\[
\boxed{p^{-s}v\pmod p.}
\]

### Proof

Both coordinates of `v` are divisible by `p^s`.  Because `q` is primitive and
`v_p(m)=s`, at least one coordinate of `p^{-s}v` is nonzero modulo `p`. ∎

## Heavy full prefix cell

Partition copies by the common depth-`s` cell of their endpoints.

### Theorem CMR1471 -- PROVED

There are at most `p^{2s}` cell classes.  Some cell `C` carries mass

\[
\boxed{\mu_C\ge\frac{\mu}{p^{2s}}.}
\]

That cell supports at least `ceil(mu_C)` distinct ordered owner-partner pairs
and at least `ceil(mu_C/2)` distinct owners.  For response-type partners it
also supports at least `ceil(mu_C)` distinct partner edges.

### Proof

A depth-`s` cell is specified by two residues modulo `p^s`.  Pigeonhole the
mass.  CMR1465 bounds mass per ordered pair by one and mass per owner by two;
CMR1466 supplies the response-partner bound. ∎

## Weighted internal/crossing split

Write every third witness uniquely as

\[
w=a+r q.
\]

### Theorem CMR1472 -- PROVED

Inside one heavy cell `C`, partition the incidence copies into:

1. **internal copies**, with `p^s` dividing `r`;
2. **crossing copies**, with `p^s` not dividing `r`.

One class has mass at least

\[
\boxed{\mu_C/2.}
\]

The internal copies have all three cells in `C`.  A crossing copy has exact
exit depth

\[
c=v_p(r)<s
\]

and projective direction `[q]` from its owner to the witness.

### Proof

The prefix-membership criterion is CMR310, applied copy by copy.  The two
classes partition the mass. ∎

### Theorem CMR1473 -- PROVED

If `s>=1` and the crossing class has mass `mu_cross`, some common exit depth
`c<s` carries mass

\[
\boxed{\mu_c\ge\frac{\mu_{\rm cross}}s
\ge\frac{\mu_C}{2s}.}
\]

It retains the original projective direction and is supported on at least
`ceil(mu_c)` ordered pairs and `ceil(mu_c/2)` owners.

### Proof

There are exactly `s` possible valuations `0,...,s-1`.  Pigeonhole and use the
CMR1465 support bounds. ∎

## Internal strict scaling

### Theorem CMR1474 -- PROVED

For an internal subfamily with `s>=1`, subtract the common depth-`s` residue
and divide both coordinates by `p^s`.  Every incidence copy becomes a
compatible collinear triple in an envelope of side

\[
\boxed{p^{k-s}<p^k.}
\]

The distinguished endpoint displacement becomes

\[
\boxed{p^{-s}v=(m/p^s)q,}
\]

whose scalar is a `p`-adic unit.  Total copy mass, distinct-pair support and
all edge-packing inequalities are preserved under the injective scaling.

### Proof

CMR312 gives integral scaling, collinearity and compatibility.  The affine map
is injective on the cell, so pair identities and packing constraints transport
bijectively.  Exact valuation of `m` makes `m/p^s` a unit. ∎

When `s=0`, every copy is internal but no strict scaling is claimed; this is the
parent-scale exact-displacement branch.

## Quantitative splice from CMR1469

Let

\[
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}
\]

be the guaranteed exact-displacement mass of CMR1469.

### Theorem CMR1475 -- PROVED

The CMR1469 bank yields one depth-`s` cell with mass at least

\[
\boxed{\frac{M_0}{p^{2s}}.}
\]

It then yields at least one of:

1. an internally scaled strict-envelope bank of mass at least
   \[
   \boxed{\frac{M_0}{2p^{2s}}};
   \]
2. when `s>=1`, a crossing bank with one strict exit depth `c<s` and mass at
   least
   \[
   \boxed{\frac{M_0}{2sp^{2s}}};
   \]
3. when `s=0`, a parent-scale exact-displacement bank of mass at least `M_0`.

### Proof

Combine CMR1471--CMR1474 with the lower bound from CMR1469. ∎

## Absolute prefix-token stock

For fixed owner stage, partner type, depth `s`, projective direction and exact
displacement, define the full-cell token

\[
\tau=(s,c_x,c_y,[q],v).
\]

### Theorem CMR1476 -- PROVED

There are exactly `p^{2s}` possible full-cell tokens at depth `s`.  Across any
finite collection of exact-displacement banks with total copy mass `M`, one
token receives mass at least

\[
\boxed{M/p^{2s}.}
\]

If every bank uses at least `R` distinct tokens and the token sets are pairwise
disjoint, their number is at most `floor(p^{2s}/R)`.

### Proof

Count the two coordinate residues modulo `p^s` and apply weighted pigeonhole or
ordinary set packing. ∎

Attach the absolute envelope stage, factor owner and layer to the token when
comparing different structural stages.

## Carry-routing endpoint

### Corollary CMR1477 -- PROVED

Every CMR1469 exact-displacement bank has a canonical quantitative response:

1. strict internal scaling to a lower prime-power envelope;
2. concentration at one earlier exit depth in the same projective direction;
3. the parent-scale depth-zero displacement branch; or
4. finite consumption/reuse of one absolute full-cell token.

Thus the packed translation bank no longer ends in anonymous prefix mass.  The
remaining quantitative task is to assign Lyapunov payment to strict scaling,
earlier-depth transfer, depth-zero translated pairs and repeated absolute
tokens strongly enough to obtain the same-owner inequality `Av<v`.  No
all-`n` theorem is claimed.

The weighted partitions, support bounds, scaling and token arithmetic are
checked in
[`scripts/verify_prime_power_weighted_displacement_carry_routing.py`](../scripts/verify_prime_power_weighted_displacement_carry_routing.py).
