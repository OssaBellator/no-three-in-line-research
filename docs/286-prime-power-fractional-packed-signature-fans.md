# Fractional candidate packings contain a heavy arithmetic signature fan

CMR1412--CMR1413 show that, at a positive minimum, every subthreshold
candidate family in an extension-free response graph of matching side `d` has
fractional packing value at least `(d-2)/3`.  CMR1454--CMR1461 place every
canonical-owner partner incidence in one finite prime-power signature.

Retain one extension-free target bank

\[
H_e=K_{d,d}\setminus(O\cup\{e\}),
\qquad d\ge4,
\]

inside an inherited prime-power envelope of side

\[
t=p^k
\]

and ambient coordinate span `W_omega<=t-1`.
Every candidate `T` has residual prescription `P_T`, canonical owner

\[
a(T)=\min_\prec(P_T\setminus M),
\]

and two eligible nonowner cells.  Each owner-partner incidence has signature

\[
\sigma=(\text{partner type},s,\theta,H),
\]

where `s` is first-separation depth, `theta` projective direction and `H`
dyadic primitive-height band.

Let `z_T` be a feasible fractional packing:

\[
z_T\ge0,
\qquad
\sum_{T:a\in P_T}z_T\le1
\quad(a\in E(H_e)).
\]

Put

\[
\nu(z)=\sum_Tz_T.
\]

If `m_sigma(T)` is the number, zero through two, of nonowner cells of `T` with
signature `sigma`, define

\[
\mu_\sigma(z)=\sum_Tz_Tm_\sigma(T).
\]

### Theorem CMR1462 -- PROVED

\[
\boxed{\sum_\sigma\mu_\sigma(z)=2\nu(z).}
\]

### Proof

Every candidate has exactly two eligible nonowner incidences. ∎

Put

\[
B_\omega=1+\left\lfloor\log_2\max\{1,W_\omega\}\right\rfloor,
\qquad
C_\omega=2k(p+1)B_\omega.
\]

### Theorem CMR1463 -- PROVED

Some eligible signature satisfies

\[
\boxed{\mu_\sigma(z)\ge\frac{2\nu(z)}{C_\omega}.}
\]

### Proof

Apply CMR1462 and pigeonhole over the CMR1457 signature stock. ∎

### Theorem CMR1464 -- PROVED

At a positive minimum with guaranteed destroyed load `L`, every exempt family
of weight below `L` admits a feasible dual packing and a signature with

\[
\boxed{
\mu_\sigma\ge
\frac{d-2}{3k(p+1)B_\omega}.}
\]

### Proof

CMR1412--CMR1413 give packing mass at least `(d-2)/3`.  Insert this into
CMR1463. ∎

For one signature define packed mass on ordered owner-partner pair `(a,b)` by

\[
\mu_\sigma(a,b)=
\sum_{T:a(T)=a,\ b\in T\setminus\{a\},\ \sigma(a,b)=\sigma}z_T.
\]

### Theorem CMR1465 -- PROVED

For every ordered pair,

\[
\boxed{\mu_\sigma(a,b)\le1.}
\]

For every owner,

\[
\boxed{\sum_{\sigma,b}\mu_\sigma(a,b)\le2.}
\]

Thus a class of mass `mu_sigma` uses at least `ceil(mu_sigma)` ordered pairs
and at least `ceil(mu_sigma/2)` owners.

### Proof

Every candidate owned by `a` contains response edge `a`, so the packing
constraint on `a` bounds owner mass by one.  Each candidate contributes two
partner incidences. ∎

### Theorem CMR1466 -- PROVED

For a response-partner signature and every response edge `b`,

\[
\sum_a\mu_\sigma(a,b)\le1.
\]

Hence it uses at least `ceil(mu_sigma)` distinct response partner edges.

### Proof

Every such partner lies in the residual prescription, so apply its packing
constraint. ∎

For a dyadic band `H`, put

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2.
\]

### Theorem CMR1467 -- PROVED

Some primitive direction in the signature carries mass

\[
\boxed{\mu_{\sigma,q}\ge\frac{\mu_\sigma}{D_p(H)}.}
\]

The class contains at least `ceil(mu_sigma/D_p(H))` distinct parallel ordered
owner-partner pairs.

### Proof

Use the CMR1460 direction stock and CMR1465 pair-mass bound. ∎

Fix that primitive vector `q`.  Every partner difference has form

\[
b-a=mq
\]

with nonzero signed integer `m` and `v_p(|m|)=s`.  Put

\[
S_{\omega,p}(s,H)=
\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor.
\]

A realized class has `S_{omega,p}(s,H)>=1`.

### Theorem CMR1468 -- PROVED

Some signed scale `m` satisfies

\[
\boxed{
\mu_{\sigma,q,m}
\ge
\frac{\mu_\sigma}
{2D_p(H)S_{\omega,p}(s,H)}.}
\]

All incidences have one exact displacement vector `mq`, and there are at least
the ceiling of this mass distinct translated owner-partner pairs.

### Proof

Board containment gives `|m|H<=W_omega`.  There are at most
`2S_{omega,p}(s,H)` signed multiples of `p^s` in that range.  Pigeonhole and
use CMR1465. ∎

### Corollary CMR1469 -- PROVED

Every subthreshold exempt family at a positive minimum yields a signature of
packed incidence mass at least

\[
\boxed{
\frac{d-2}{3k(p+1)B_\omega}}
\]

and an exact-displacement class of mass at least

\[
\boxed{
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}.}
\]

The class is dispersed over canonical owners and ordered pairs; in the response
branch it is also dispersed over residual response edges.  The exact-
displacement subclass is a bank of parallel translates.  The theorem applies
to scattered residual factors because matching side `d`, envelope depth `k`
and coordinate span `W_omega` are kept distinct.  The open task is to pay this
bank through prefix return, quotient/carry collision, protected reserve or a
subcritical owner/rook credit class.  No all-`n` theorem is claimed.

Checked in full-grid and synthetic inherited-coordinate specializations by
[`scripts/verify_prime_power_fractional_packed_signature_fans.py`](../scripts/verify_prime_power_fractional_packed_signature_fans.py).
