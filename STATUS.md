# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open.  This repository does **not** contain a complete proof.

The authoritative collision-free ledger is split across:

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `proofs/composite-modulus-theorem-index-live-continuation-3.md` through CMR1469.

CMR1414--CMR1461 was deliberately reindexed after concurrent branch work had
already occupied CMR1374--CMR1413.  The obsolete colliding draft files were
removed; the concurrent theorem chain was preserved.

## Structural endpoint

The selected-minimum execution has finite canonical forms for rollback,
minimum-core contraction, nested hosts, selected routing, strict child
products, unit Hall walls, protected/free and exchange-SCC products,
fixed-core lifting, restoration ancestry, target banks and small-side bases.

Every new triple has one absolute last-entering edge owner.  Product, wall,
host and envelope exits form a finite owner DAG, so the global offspring matrix
is block upper triangular:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Only same-owner diagonal blocks still require subcritical certificates.  This
structural finiteness does **not** imply that a positive minimum reaches zero.

## Exact extension-free target bank

For one target edge `e` and opposite matching `O`, put

\[
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

The response family is exactly `PM(H_e)`, and every response has a canonical
forbidden extension through `e`.  Its size is

\[
|\operatorname{PM}(H_e)|=D_n\frac{n-2}{n-1}.
\]

After relabeling `O` to the identity and `e=(0,1)`, a compatible prescription
`P` is described by

\[
(r,q(P),d(P),\varepsilon(P)).
\]

The residual forbidden-board rook numbers are

\[
\boxed{
r_j(P)=\binom qj+\varepsilon(P)\binom{q-d}{j-1}.
}
\]

Hence the exact completion count is

\[
\boxed{
B_n(P)=
\sum_{j=0}^{n-r}(-1)^j
\left[\binom qj+\varepsilon\binom{q-d}{j-1}\right](n-r-j)!.
}
\]

Therefore

\[
\boxed{
\Pr(P\subseteq R)=
\frac{B_n(P)}{D_n(n-2)/(n-1)}.
}
\]

For fixed rank there are at most `6(n-r+1)` exact probability classes.
Expected collateral and unavailable-edge use are exact finite rook-class dot
products, not only permanent upper bounds.

## Exact shared-edge owner assignment

For response `R`, each new triple has one entering owner.  If `a` is entering
and `z_{a,L}(R)` counts selected cells on line `L` eligible to accompany `a`,
then

\[
\boxed{
\gamma_e(a,R)=\sum_{L\ni a}\binom{z_{a,L}(R)}2,
}
\]

and

\[
N(R)=\sum_{a\in R}\gamma_e(a,R).
\]

Define

\[
p_e(a)=\Pr(a\in R),
\qquad
g_e(a)=\mathbb E[\gamma_e(a,R)\mid a\in R].
\]

Then

\[
\boxed{
\mathbb E N(R)=\sum_ap_e(a)g_e(a).
}
\]

The marginal matrix `p_e(x,y)` is doubly stochastic.  Thus expected collateral
is one bipartite assignment cost.  Rational potentials satisfying

\[
\alpha_x+\beta_y\ge g_e(x,y)
\]

and

\[
\sum_x\alpha_x+\sum_y\beta_y<D_S(e)
\]

certify a strict improvement.  After clearing denominators this is a finite
integer certificate.

## Closed owner weights from rook classes

Every candidate triple `U` has residual prescription `P_U` and fixed entering
owner

\[
a(U)=\min_\prec(P_U\setminus M)
\]

before the response is sampled.  If

\[
C_e(a;r,q,d,\varepsilon)
\]

counts candidates of one owner and rook class, then

\[
\boxed{
c_e(a)=
\sum_{r,q,d,\varepsilon}
C_e(a;r,q,d,\varepsilon)\pi_n(r,q,d,\varepsilon),
}
\]

and

\[
g_e(a)=\frac{c_e(a)}{p_e(a)}.
\]

Primitive height, real-line population, prefix, quotient and carry labels may
refine these classes without losing exactness.  Fibre maxima give honest
host-uniform upper quotients.

## Lattice-capacity pair envelope

For distinct cells `a,b`, let `h(a,b)` be their primitive direction height and
put

\[
c_n(h)=
\max\left\{\left\lfloor\frac{n-1}{h}\right\rfloor-1,0\right\}.
\]

The exact line capacity gives

\[
\boxed{
\gamma_e(a,R)
\le
\frac12
\sum_{b\in E_a(R)}c_n(h(a,b)).
}
\]

for every entering owner.  Using exact pair rook probabilities produces a
conditional capacity star `mathscr C_e(a)` and

\[
\boxed{
g_e(a)\le\frac12\mathscr C_e(a).}
\]

This is strictly sharper than the harmonic relaxation.  In particular,

\[
h>\frac{n-1}{2}
\quad\Longrightarrow\quad
c_n(h)=0,
\]

so high primitive directions vanish exactly rather than forming a tail.

Eligibility is fixed before sampling: a response partner `b` contributes to
owner `a` exactly when `b` was already in the old matching or `a\prec b`.
Removing earlier entering edges gives the still sharper envelope
`Gamma_e^{elig}(a)`.

## Prime-power eligible signatures

At side

\[
n=p^k,
\]

write an eligible pair difference as

\[
b-a=G(u,v)
\]

with primitive `(u,v)`.  Every pair has one signature

\[
\boxed{
(t,s,\delta,H),
}
\]

where:

- `t` records fixed or response partner;
- `s=v_p(G)` is the first-separation depth;
- `delta=[u:v]` is the projective direction modulo `p`;
- `H` is the dyadic primitive-height band.

For one owner, at most

\[
\boxed{
2k(p+1)\bigl(1+\lfloor\log_2(n-1)\rfloor\bigr)
}
\]

signature positions occur.  A large eligible owner envelope forces one heavy
signature class.  Some actual response simultaneously realizes at least the
ceiling of its conditional mean.  All those partners lie in one prefix carry
cell, one projective class and one height band.

A fixed projective/height class contains at most

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2
\]

exact primitive directions.  Therefore a heavy simultaneous signature
concentrates quantitatively on one real line through the owner.

## Fractional packed signature endpoint

The dual of the candidate-transversal LP assigns masses `z_T` satisfying

\[
z_T\ge0,
\qquad
\sum_{T:a\in P_T}z_T\le1
\]

on every residual response edge.  Every candidate contributes exactly two
eligible owner-partner incidences.  If `nu=sum_T z_T`, then

\[
\boxed{
\sum_\sigma\mu_\sigma=2\nu.
}
\]

At a positive minimum, every exempt family below the destroyed-load threshold
has `nu>=(n-2)/3`.  Consequently one prime-power signature has packed incidence
mass at least

\[
\boxed{
\frac{n-2}
{3k(p+1)(1+\lfloor\log_2(n-1)\rfloor)}.
}
\]

A signature of mass `mu` uses at least `ceil(mu)` distinct ordered
owner-partner pairs and at least `ceil(mu/2)` distinct owners.  In the response
partner branch it also uses at least `ceil(mu)` distinct residual response
edges.

After partitioning by actual primitive direction and signed scale, one exact
lattice displacement class has mass at least

\[
\boxed{
\frac{\mu}
{2D_p(H)\left\lfloor(n-1)/(p^sH)\right\rfloor}.
}
\]

Thus the global fractional obstruction contains a translated bank of
owner-partner pairs with one first-separation depth, one projective direction,
one height band and one exact displacement vector.  This is distinct from the
one-owner loaded-line class: it is dispersed across owners but arithmetically
identical.

## Corrections retained

- Sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines and stars are not simultaneous families.
- One edge return may serve several neutralizations in one absence run.
- Removing one essential edge gives Hall deficiency exactly one.
- Aggressive batch deletion is branch-local.
- Differently masked leaf unions are not automatically one matching host.
- Conditioning on one support edge does not fix the other two layer labels.
- Finite scheduler termination is not potential improvement.
- Old response edges and old subsets create no new collateral.
- Candidate prescriptions have at most, not exactly, `(n-r)!` restricted-bank
  completions.
- Standard-grid finite classifications do not transfer to scattered residual
  coordinates.
- The side-six one-layer trap graph has six two-cycles and twelve feeders, not
  fixed points.

## Current open frontier

1. **Packed exact-displacement payment.**  Quantify prefix-return,
   quotient/carry or protected-reserve payment for the CMR1469 translated
   owner-partner bank.
2. **Loaded-line comparison.**  Compare that global payment with the one-owner
   simultaneous line gain forced by CMR1458--CMR1461.
3. **Subcritical same-owner quotient.**  Encode the comparison as a
   host-uniform rational or integer certificate `Av<v`.
4. **Prime-field and thin regimes.**  Prove the analogous diagonal certificate
   without a nonroot prefix-depth budget.
5. **Arbitrary side lengths.**  Glue the diagonal blocks through owner
   triangularity and complete balanced/CRT assembly with collision/local-line
   credit classes retained.

## Bottom line

There is no complete proof.  Through **CMR1469**, matching probabilities,
canonical owner weights, cross-line assignment, lattice-capacity reduction,
prime-power carry signatures and the global fractional packed-signature
extraction are exact.  The remaining obstruction is the quantitative payment
for one arithmetically identical exact-displacement translation bank and its
comparison with the one-owner loaded-line execution gain, not an uncontrolled
recurrence, product interaction or anonymous line maximum.
