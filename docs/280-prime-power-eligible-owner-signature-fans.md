# Eligible owner signatures turn collateral into finite geometric fans

CMR1398--CMR1405 give every possible new triple a fixed canonical entering-edge
owner before a response is sampled.  CMR1406--CMR1413 then show that a positive
minimum must retain a large owner support or a large fractional candidate packing.
The missing bridge is geometric: translate one owner load into finitely many
primitive-height, prefix-depth and projective-direction fans.

This chapter supplies that bridge.  The statements are deterministic for one
response and therefore remain valid under every response distribution.

Let

\[
n=p^h\ge4,
\]

let `O` and `M` be the fixed and current matching layers, let `e in M` be the
omitted target edge, and let

\[
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

Fix a response `R in PM(H_e)` and an entering edge

\[
a\in R\setminus M.
\]

Write `Gamma_a(R)` for the newly created physical triples whose canonical
CMR1215 owner is `a`, and put

\[
\gamma_a(R)=|\Gamma_a(R)|.
\]

## 1. Eligible partners

A selected cell `b != a` is **eligible for `a`** when either

1. `b in O`, in which case its type is `fixed`; or
2. `b in R`, in which case its type is `response`, and either `b in M` or
   `a prec b` in the fixed owner order.

### Theorem CMR1414 -- PROVED

Every triple in `Gamma_a(R)` has exactly two eligible partners of `a`.

### Proof

The two nonowner cells are selected from `O union R`.  A fixed-layer cell is
eligible by definition.  A response-layer cell which already lies in `M` is also
eligible.  Every remaining response-layer cell is entering.  Since `a` is the
least entering edge of a triple owned by `a`, every other entering cell in that
triple is larger than `a`.  Thus both nonowner cells are eligible. ∎

## 2. Primitive line capacity

For an eligible partner `b`, write

\[
b-a=t(u,v),
\]

where `t` is a nonzero signed integer, `(u,v)` is primitive and its sign is
normalised by

\[
u>0\quad\text{or}\quad u=0,\ v>0.
\]

Put

\[
H(a,b)=\max(|u|,|v|)
\]

and

\[
\kappa_n(H)
=
\max\left\{
\left\lfloor\frac{n-1}{H}\right\rfloor-1,
0
\right\}.
\]

### Theorem CMR1415 -- PROVED

The real line through `a` and `b` contains at most

\[
\left\lfloor\frac{n-1}{H(a,b)}\right\rfloor+1
\]

grid cells.  Hence, after `a` and `b` are fixed, there are at most
`kappa_n(H(a,b))` possible third grid cells on that line.

### Proof

Consecutive lattice points on the line differ by the primitive vector `(u,v)`.
If the extreme grid points use parameters whose difference is `m`, then one
coordinate has span `mH(a,b)`.  That span is at most `n-1`, so

\[
m\le\left\lfloor\frac{n-1}{H(a,b)}\right\rfloor.
\]

The number of grid points is at most `m+1`.  Remove the two fixed points. ∎

## 3. Exact eligible-incidence domination

Let `E_a(R)` be the set of eligible partners of `a`.

### Theorem CMR1416 -- PROVED

\[
\boxed{
2\gamma_a(R)
\le
\sum_{b\in E_a(R)}\kappa_n(H(a,b)).
}
\]

### Proof

Each owned triple contributes its two nonowner cells as two eligible incidences.
For a fixed eligible partner `b`, CMR1415 bounds the number of possible third
cells, and therefore the number of owned triples using the incidence `(a,b)`, by
`kappa_n(H(a,b))`.  Sum over eligible partners. ∎

The factor two is exact at the incidence level: every owned triple contributes
one incidence for each of its two partners.

## 4. Finite prime-power signatures

Let

\[
k(a,b)=\gcd(|b_x-a_x|,|b_y-a_y|),
\qquad
d(a,b)=v_p(k(a,b)),
\]

let

\[
\theta(a,b)=[u:v]\in\mathbf P^1(\mathbf F_p),
\]

and let

\[
\beta(a,b)=2^{\lfloor\log_2H(a,b)\rfloor}.
\]

The **eligible signature** is

\[
\sigma(a,b)
=
(\text{partner type},d(a,b),\theta(a,b),\beta(a,b)).
\]

Put

\[
B_n=1+\lfloor\log_2(n-1)\rfloor
\]

and

\[
K_{p,h,n}=2h(p+1)B_n.
\]

### Theorem CMR1417 -- PROVED

For one owner, at most `K_{p,h,n}` eligible signatures occur.

### Proof

There are two partner types.  Since `1<=k(a,b)<=p^h-1`, its valuation lies in
`{0,...,h-1}`.  The projective line has `p+1` directions, and the primitive
height has `B_n` dyadic bands.  Multiply the stocks. ∎

This is the finite signature set needed by a host-uniform upper quotient.

## 5. Heavy signature extraction

For a signature `sigma`, let

\[
E_{a,\sigma}(R)
=
\{b\in E_a(R):\sigma(a,b)=\sigma\}
\]

and define its exact capacity mass

\[
C_{a,\sigma}(R)
=
\sum_{b\in E_{a,\sigma}(R)}\kappa_n(H(a,b)).
\]

### Theorem CMR1418 -- PROVED

There is a signature `sigma` such that

\[
\boxed{
C_{a,\sigma}(R)
\ge
\frac{2\gamma_a(R)}{K_{p,h,n}}.
}
\]

If `gamma_a(R)>0`, the chosen signature has `kappa_n(beta)>0` and

\[
\boxed{
|E_{a,\sigma}(R)|
\ge
\left\lceil
\frac{2\gamma_a(R)}
{K_{p,h,n}\,\kappa_n(\beta)}
\right\rceil.
}
\]

### Proof

CMR1416 and CMR1417 pigeonhole the total capacity over at most
`K_{p,h,n}` classes.  Inside the dyadic band `beta<=H<2beta`, monotonicity gives

\[
\kappa_n(H)\le\kappa_n(\beta).
\]

Divide the class capacity by this maximum per-partner contribution. ∎

Thus a large owner load cannot remain diffuse over unrelated arithmetic line
types.

## 6. Averaged owner loads still produce a deterministic fan

Let `mu` be any probability distribution on responses containing a fixed allowed
entering owner `a`.  Expectations below are conditional on `a in R`.

### Theorem CMR1419 -- PROVED

\[
2\mathbf E_\mu\gamma_a(R)
\le
\sum_\sigma
\kappa_n(\beta_\sigma)
\mathbf E_\mu|E_{a,\sigma}(R)|.
\]

Consequently some signature satisfies

\[
\kappa_n(\beta_\sigma)
\mathbf E_\mu|E_{a,\sigma}(R)|
\ge
\frac{2\mathbf E_\mu\gamma_a(R)}{K_{p,h,n}}.
\]

For every fixed signature in the support, some response realizes at least

\[
\left\lceil
\mathbf E_\mu|E_{a,\sigma}(R)|
\right\rceil
\]

partners of that signature.

### Proof

Average CMR1416 and replace each exact capacity in a dyadic class by the larger
band value `kappa_n(beta)`.  Pigeonhole the finite signature stock.  The final
statement is the elementary fact that a finite average cannot exceed every
realized integer value. ∎

This applies in particular to the exact rook-conditioned owner distributions of
CMR1398--CMR1405.

## 7. Direction and scale stock inside one signature

For a dyadic band `beta` define

\[
D_p(\beta)
=
(p-1)
\left\lceil\frac{4\beta}{p}\right\rceil^2.
\]

### Theorem CMR1420 -- PROVED

Fix a projective direction `theta`.  The number of sign-normalised primitive
vectors `(u,v)` satisfying

\[
\beta\le\max(|u|,|v|)<2\beta,
\qquad
[u:v]=\theta
\]

is at most

\[
\boxed{D_p(\beta).}
\]

For one owner and one signature `(type,d,theta,beta)`, the number of possible
grid partners is at most

\[
\boxed{
2D_p(\beta)
\left\lfloor
\frac{n-1}{p^d\beta}
\right\rfloor.
}
\]

### Proof

For a fixed nonzero projective residue, there are `p-1` nonzero scalar
representatives modulo `p`.  In the square `|u|,|v|<2beta`, each coordinate has
fewer than `4beta` integer values, so each prescribed residue class contributes
at most `ceil(4beta/p)` choices per coordinate.  Primitivity, the shell condition
and sign normalisation only reduce the count.

For a fixed primitive vector of height at least `beta`, a partner has signed
scale `t` with `v_p(|t|)=d` and

\[
|t|\beta\le n-1.
\]

There are at most twice `floor((n-1)/(p^d beta))` possible signed multiples of
`p^d`.  Multiply by the direction stock. ∎

## 8. Eligible-signature endpoint

### Corollary CMR1421 -- PROVED

Every deterministic or averaged canonical-owner load admits the following exact
finite reduction.

1. Each owned triple supplies two eligible partner incidences.
2. Primitive height gives an explicit line-capacity payment.
3. Eligible incidences lie in at most `2h(p+1)B_n` arithmetic signatures.
4. A large owner load produces one heavy signature fan.
5. The same extraction remains valid for exact rook-conditioned owner averages.
6. One signature has an explicit finite stock of primitive directions and signed
   depth-`d` scales.

The remaining obstruction may therefore be expressed in the same
`(type, depth, projective direction, dyadic height)` coordinates used by prefix,
quotient and carry ledgers.  No all-`n` theorem is claimed.

Eligible incidence, capacity domination, signature stocks, response averaging,
direction multiplicity and finite fan concentration are checked in
[`scripts/verify_prime_power_eligible_owner_signature_fans.py`](../scripts/verify_prime_power_eligible_owner_signature_fans.py).
