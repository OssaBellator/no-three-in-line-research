# Fractional candidate packings contain a heavy arithmetic signature fan

CMR1412--CMR1413 show that, at a positive minimum, every candidate family below
the destroyed-load threshold has fractional transversal and dual packing value at
least `(n-2)/3`.  CMR1414--CMR1421 place every canonical-owner partner incidence
in one finite arithmetic signature.  Combining the two results turns the abstract
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

and two nonowner cells.  By CMR1414 those two cells are eligible partners of the
owner.

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

For an eligible signature `sigma`, let `m_sigma(T)` be the number, zero, one or
two, of nonowner cells of `T` having signature `sigma` relative to `a(T)`, and
put

\[
\mu_\sigma(z)
=
\sum_Tz_Tm_\sigma(T).
\]

## 1. Exact packed-incidence identity

### Theorem CMR1422 -- PROVED

\[
\boxed{
\sum_\sigma\mu_\sigma(z)=2\nu(z).
}
\]

### Proof

Every candidate has exactly two nonowner cells, and CMR1414 makes both eligible.
Each candidate of packing mass `z_T` therefore contributes exactly `2z_T` to the
signature-incidence sum. ∎

No response matching is sampled in this identity.

## 2. Finite signature extraction

Recall

\[
B_n=1+\lfloor\log_2(n-1)\rfloor,
\qquad
K_{p,h,n}=2h(p+1)B_n.
\]

### Theorem CMR1423 -- PROVED

Some eligible signature satisfies

\[
\boxed{
\mu_\sigma(z)
\ge
\frac{2\nu(z)}{K_{p,h,n}}.
}
\]

### Proof

CMR1417 gives at most `K_{p,h,n}` signatures.  Apply CMR1422 and pigeonhole. ∎

Thus a large fractional packing cannot be spread over arbitrarily many unrelated
height, prefix-depth and projective-direction types.

## 3. Positive-minimum quantitative fan

Let `B subseteq C` be an exempt family, and apply the definitions to the
nonexempt candidates `C setminus B`.

### Theorem CMR1424 -- PROVED

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

CMR1412--CMR1413 give a feasible packing of mass

\[
\nu\ge\frac{n-2}{3}.
\]

Insert this value into CMR1423:

\[
\frac{2\nu}{2h(p+1)B_n}
\ge
\frac{n-2}{3h(p+1)B_n}.
\]

∎

For nonroot prime powers this lower bound grows with the side length for fixed
`p`, apart from the explicit depth and dyadic-class factors.  Prime-field and
thin regimes remain separate endpoints.

## 4. Pair and owner dispersion

For one signature define the packed mass on an ordered owner-partner pair by

\[
\mu_\sigma(a,b)
=
\sum_{
T:\ a(T)=a,\ b\in T\setminus\{a\},\ \sigma(a,b)=\sigma
}z_T.
\]

### Theorem CMR1425 -- PROVED

For every ordered pair `(a,b)`,

\[
\boxed{
\mu_\sigma(a,b)\le1.
}
\]

For every owner `a`, the total packed eligible-partner incidence is at most two:

\[
\boxed{
\sum_{\sigma,b}\mu_\sigma(a,b)
\le2.
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

Every candidate owned by `a` contains `a` in its residual prescription.  The
packing constraint on edge `a` therefore gives

\[
\sum_{T:a(T)=a}z_T\le1.
\]

A fixed pair `(a,b)` uses a subfamily of these candidates, proving the first
bound.  Each candidate owned by `a` contributes exactly two eligible incidences,
proving the second.  Divide the class mass by the maximum mass per pair and per
owner. ∎

This excludes concentration of a heavy signature on one physical owner.

## 5. Response-partner dispersion

### Theorem CMR1426 -- PROVED

If the heavy signature has partner type `response`, then for every response edge
`b`,

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
candidate containing it.  The fractional packing constraint on `b` bounds the
total mass of all such candidates by one. ∎

For fixed-layer partners there is no analogous residual-edge constraint, but
CMR1425 still supplies pair and owner dispersion.

## 6. One primitive direction carries a definite mass

For a signature with dyadic band `beta`, let

\[
D_p(\beta)
=
(p-1)\left\lceil\frac{4\beta}{p}\right\rceil^2.
\]

Partition the signature mass by the sign-normalised primitive vector `(u,v)`.

### Theorem CMR1427 -- PROVED

Some primitive vector `q=(u,v)` in the signature satisfies

\[
\boxed{
\mu_{\sigma,q}
\ge
\frac{\mu_\sigma}{D_p(\beta)}.
}
\]

The selected class contains at least

\[
\left\lceil
\frac{\mu_\sigma}{D_p(\beta)}
\right\rceil
\]

distinct parallel ordered owner-partner pairs.

### Proof

CMR1420 bounds the primitive-direction stock inside one projective-direction and
dyadic-height class by `D_p(beta)`.  Pigeonhole the signature mass.  Every fixed
ordered pair has packed mass at most one by CMR1425. ∎

Thus projective concentration produces an actual parallel family, not merely a
residue-class statement.

## 7. One exact displacement carries a definite mass

Fix the primitive vector `q` from CMR1427.  Every corresponding partner has

\[
b-a=tq
\]

for a nonzero signed integer `t` with `v_p(|t|)=d`, where `d` is the signature
depth.  Put

\[
S_{n,p}(d,\beta)
=
\left\lfloor
\frac{n-1}{p^d\beta}
\right\rfloor.
\]

A realized signature always has `S_{n,p}(d,beta)>=1`.

### Theorem CMR1428 -- PROVED

Some signed scale `t` satisfies

\[
\boxed{
\mu_{\sigma,q,t}
\ge
\frac{\mu_\sigma}
{2D_p(\beta)S_{n,p}(d,\beta)}.
}
\]

All incidences in this subfamily have the same exact displacement vector `tq`.
They contain at least

\[
\left\lceil
\frac{\mu_\sigma}
{2D_p(\beta)S_{n,p}(d,\beta)}
\right\rceil
\]

distinct translated owner-partner pairs.

### Proof

The primitive height of `q` is at least `beta`.  Board containment gives

\[
|t|\beta\le n-1.
\]

Among signed integers divisible by `p^d`, there are at most

\[
2S_{n,p}(d,\beta)
\]

possible values.  The exact-depth restriction only reduces this stock.  Apply
CMR1427, pigeonhole the signed scales, and use the unit pair-mass bound from
CMR1425. ∎

The resulting family consists of parallel translates with one exact lattice
displacement, a form directly compatible with prefix and carry analysis.

## 8. Packed-signature endpoint

### Corollary CMR1429 -- PROVED

At a positive minimum, every exempt family of weight below the destroyed-load
threshold yields at least one arithmetic signature

\[
(\text{type},d,\theta,\beta)
\]

of packed eligible-incidence mass at least

\[
\boxed{
\frac{n-2}{3h(p+1)B_n}.
}
\]

Inside it there is an exact displacement class of mass at least

\[
\boxed{
\frac{n-2}
{6h(p+1)B_n
D_p(\beta)
S_{n,p}(d,\beta)}.
}
\]

The first class is dispersed over many canonical owners and ordered pairs; in the
response-partner branch it is also dispersed over many residual response edges.
The second class is a bank of translated owner-partner pairs with identical
primitive direction and signed scale.

The next closing step can therefore target a concrete object: a large fractional
bank of fixed-depth, fixed-projective-direction, fixed-height and eventually
fixed-displacement incidences.  Such a bank must be charged to prefix return,
quotient/carry collision, protected reserve, or a subcritical owner/rook credit
class.  No all-`n` theorem is claimed.

Packed-incidence identities, signature extraction, owner and partner dispersion,
primitive-direction concentration and exact-displacement concentration are
checked in
[`scripts/verify_prime_power_fractional_packed_signature_fans.py`](../scripts/verify_prime_power_fractional_packed_signature_fans.py).
