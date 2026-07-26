# Fractional candidate packings contain a heavy arithmetic signature fan

CMR1412--CMR1413 show that, at a positive minimum, every candidate family below
the destroyed-load threshold has fractional transversal and dual packing value at
least `(n-2)/3`.  CMR1454--CMR1461 place every canonical-owner partner incidence
in one finite prime-power signature.  Combining the two results turns the global
LP obstruction into a quantitative geometric fan.

Retain one extension-free target bank

\[
H_e=K_{n,n}\setminus(O\cup\{e\}),
\qquad n=p^h\ge4.
\]

Let `C` be a candidate family.  Every `T in C` has a nonempty matching-compatible
residual prescription `P_T`, a fixed canonical owner

\[
a(T)=\min_\prec(P_T\setminus M),
\]

and two nonowner cells.  By CMR1454--CMR1456 those cells are eligible owner
partners and each has one signature

\[
\sigma=(\text{partner type},d,\theta,\beta),
\]

where `d` is the first-separation depth, `theta` the projective direction and
`beta` the dyadic primitive-height band.

Let `z_T` be any feasible fractional packing:

\[
z_T\ge0,
\qquad
\sum_{T:a\in P_T}z_T\le1
\quad(a\in E(H_e)).
\]

Put

\[
\nu(z)=\sum_{T\in\mathcal C}z_T.
\]

For a signature `sigma`, let `m_sigma(T)` be the number, zero, one or two, of
nonowner cells of `T` having that signature relative to `a(T)`, and define

\[
\mu_\sigma(z)=\sum_Tz_Tm_\sigma(T).
\]

## 1. Exact packed-incidence identity

### Theorem CMR1462 -- PROVED

\[
\boxed{
\sum_\sigma\mu_\sigma(z)=2\nu(z).
}
\]

### Proof

Every candidate has exactly two nonowner cells, and both are eligible by the
canonical-owner rule.  A candidate of mass `z_T` therefore contributes exactly
`2z_T` to the signature-incidence sum. ∎

## 2. Finite signature extraction

Recall

\[
B_n=1+\lfloor\log_2(n-1)\rfloor,
\qquad
C_n=2h(p+1)B_n
\]

from CMR1457.

### Theorem CMR1463 -- PROVED

Some eligible signature satisfies

\[
\boxed{
\mu_\sigma(z)
\ge
\frac{2\nu(z)}{C_n}.
}
\]

### Proof

There are at most `C_n` signature positions.  Apply CMR1462 and pigeonhole. ∎

## 3. Positive-minimum quantitative fan

Let `B subseteq C` be an exempt family, and apply the definitions to the
nonexempt candidates `C setminus B`.

### Theorem CMR1464 -- PROVED

At a positive minimum with guaranteed destroyed load `L`, every exempt family
satisfying

\[
\sum_{T\in B}v_T<L
\]

admits a feasible dual packing and an eligible signature `sigma` with

\[
\boxed{
\mu_\sigma
\ge
\frac{n-2}{3h(p+1)B_n}.
}
\]

### Proof

CMR1412--CMR1413 give a feasible packing of mass at least `(n-2)/3`.  Insert
that value into CMR1463. ∎

This is the first direct quantitative passage from the global transversal
obstruction to one prefix-depth, projective-direction and height class.

## 4. Pair and owner dispersion

For one signature define the packed mass on an ordered owner-partner pair by

\[
\mu_\sigma(a,b)
=
\sum_{
T:\ a(T)=a,\ b\in T\setminus\{a\},\ \sigma(a,b)=\sigma
}z_T.
\]

### Theorem CMR1465 -- PROVED

For every ordered pair `(a,b)`,

\[
\boxed{\mu_\sigma(a,b)\le1.}
\]

For every owner `a`, the total packed eligible-partner incidence is at most two:

\[
\boxed{
\sum_{\sigma,b}\mu_\sigma(a,b)\le2.
}
\]

Consequently a signature of mass `mu_sigma` is supported on at least

\[
\boxed{\lceil\mu_\sigma\rceil}
\]

distinct ordered owner-partner pairs and at least

\[
\boxed{\left\lceil\mu_\sigma/2\right\rceil}
\]

distinct canonical owners.

### Proof

Every candidate owned by `a` contains `a` in its residual prescription, so the
packing constraint on edge `a` gives total owner mass at most one.  A fixed pair
uses a subfamily of those candidates.  Each candidate contributes exactly two
eligible incidences, giving the owner bound.  Divide the class mass by the
maximum mass per pair and per owner. ∎

## 5. Response-partner dispersion

### Theorem CMR1466 -- PROVED

If the signature has partner type `response`, then for every response edge `b`,

\[
\sum_a\mu_\sigma(a,b)\le1.
\]

Hence a response-type signature of mass `mu_sigma` uses at least

\[
\boxed{\lceil\mu_\sigma\rceil}
\]

distinct response partner edges.

### Proof

Every response-type partner belongs to the residual prescription of the
candidate containing it.  Apply the packing constraint on `b`. ∎

Fixed-layer partners lack this residual-edge constraint, but CMR1465 still gives
pair and owner dispersion.

## 6. One primitive direction carries definite mass

For a dyadic band `beta`, put

\[
D_p(\beta)
=
(p-1)\left\lceil\frac{4\beta}{p}\right\rceil^2.
\]

Partition the signature mass by the canonically oriented primitive vector
`q=(u,v)`.

### Theorem CMR1467 -- PROVED

Some primitive vector in the signature satisfies

\[
\boxed{
\mu_{\sigma,q}
\ge
\frac{\mu_\sigma}{D_p(\beta)}.
}
\]

The selected class contains at least

\[
\left\lceil\frac{\mu_\sigma}{D_p(\beta)}\right\rceil
\]

distinct parallel ordered owner-partner pairs.

### Proof

CMR1460 bounds the primitive-direction stock by `D_p(beta)`.  Pigeonhole the
signature mass and use the unit pair-mass bound from CMR1465. ∎

Unlike CMR1460, which fixes one owner and therefore one real line, this global
packing statement yields a bank of parallel translated lines across many owners.

## 7. One exact displacement carries definite mass

Fix the primitive vector `q` from CMR1467.  Every corresponding partner has

\[
b-a=tq
\]

for a nonzero signed integer `t` with `v_p(|t|)=d`.  Put

\[
S_{n,p}(d,\beta)
=
\left\lfloor\frac{n-1}{p^d\beta}\right\rfloor.
\]

A realized signature has `S_{n,p}(d,beta)>=1`.

### Theorem CMR1468 -- PROVED

Some signed scale `t` satisfies

\[
\boxed{
\mu_{\sigma,q,t}
\ge
\frac{\mu_\sigma}
{2D_p(\beta)S_{n,p}(d,\beta)}.
}
\]

All incidences in this subfamily have the same exact displacement vector `tq`,
and they contain at least

\[
\left\lceil
\frac{\mu_\sigma}
{2D_p(\beta)S_{n,p}(d,\beta)}
\right\rceil
\]

distinct translated owner-partner pairs.

### Proof

The primitive height of `q` is at least `beta`.  Board containment gives
`|t|beta<=n-1`.  There are at most

\[
2S_{n,p}(d,\beta)
\]

signed multiples of `p^d` in that range; requiring exact valuation only reduces
the stock.  Apply CMR1467, pigeonhole the signed scales, and use CMR1465. ∎

## 8. Packed-signature endpoint

### Corollary CMR1469 -- PROVED

At a positive minimum, every exempt family of weight below the destroyed-load
threshold yields an arithmetic signature of packed eligible-incidence mass at
least

\[
\boxed{
\frac{n-2}{3h(p+1)B_n}.
}
\]

Inside it there is an exact displacement class of mass at least

\[
\boxed{
\frac{n-2}
{6h(p+1)B_nD_p(\beta)S_{n,p}(d,\beta)}.
}
\]

The signature class is dispersed over many canonical owners and ordered pairs;
in the response-partner branch it is also dispersed over many residual response
edges.  The exact-displacement subclass is a bank of parallel translates with
one lattice displacement.

The active quantitative target is now sharper than the one-owner loaded-line
endpoint: rule out or pay this globally packed fixed-depth, fixed-direction and
fixed-displacement bank using prefix return, quotient/carry collision, protected
reserve, or a subcritical owner/rook credit class.  No all-`n` theorem is
claimed.

Packed-incidence identities, signature extraction, owner and partner dispersion,
primitive-direction concentration and exact-displacement concentration are
checked in
[`scripts/verify_prime_power_fractional_packed_signature_fans.py`](../scripts/verify_prime_power_fractional_packed_signature_fans.py).
