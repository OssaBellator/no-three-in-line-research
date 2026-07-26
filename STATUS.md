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

CMR1414--CMR1461 was reindexed after concurrent work had already occupied
CMR1374--CMR1413.  The concurrent files were preserved, obsolete colliding
drafts were removed, and CMR1462--CMR1469 was retained and corrected for
inherited-coordinate scope.

## Structural endpoint

The selected-minimum execution has finite canonical forms for rollback,
minimum-core contraction, nested hosts, selected routing, strict child
products, unit Hall walls, protected/free and exchange-SCC products,
fixed-core lifting, restoration ancestry, target banks and small-side bases.

Every new triple has one absolute last-entering owner.  Product, wall, host and
envelope exits form a finite owner DAG, so

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Only same-owner diagonal blocks still require subcritical certificates.
Structural finiteness alone does not imply that a positive minimum reaches
zero.

## Exact extension-free probability law

For one response matching side `d`, target edge `e` and opposite matching `O`,
put

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

After relabeling `O` to the identity, a compatible rank-`r` prescription has
parameters `(q,d_0,epsilon)`.  Its residual rook numbers are

\[
\boxed{
r_j(P)=\binom qj+\varepsilon(P)\binom{q-d_0}{j-1}.}
\]

Hence

\[
\boxed{
B_d(P)=
\sum_{j=0}^{d-r}(-1)^j
\left[\binom qj+\varepsilon\binom{q-d_0}{j-1}\right](d-r-j)!}
\]

and

\[
\boxed{
\Pr(P\subseteq R)=
\frac{B_d(P)}{D_d(d-2)/(d-1)}.}
\]

Expected collateral and unavailable-edge use are exact finite rook-class dot
products.

## Exact shared-edge assignment

Every candidate triple has a fixed entering owner before the response is
sampled.  For an entering edge `a`,

\[
\gamma_e(a,R)=\sum_{L\ni a}\binom{z_{a,L}(R)}2,
\qquad
N(R)=\sum_a\gamma_e(a,R).
\]

With

\[
p_e(a)=\Pr(a\in R),
\qquad
g_e(a)=\mathbb E[\gamma_e(a,R)\mid a\in R],
\]

one has

\[
\boxed{\mathbb E N(R)=\sum_ap_e(a)g_e(a).}
\]

The marginal matrix is doubly stochastic.  Therefore expected collateral is
one bipartite assignment cost.  Rational row/column potentials satisfying

\[
\alpha_x+\beta_y\ge g_e(x,y)
\]

and total below the destroyed target load certify strict improvement.  After
clearing denominators this is a finite integer certificate.

Every owner weight is closed algebraically:

\[
c_e(a)=
\sum C_e(a;r,q,d_0,\varepsilon,\eta)
\pi_d(r,q,d_0,\varepsilon),
\qquad
g_e(a)=\frac{c_e(a)}{p_e(a)}.
\]

Here `eta` may retain primitive height, line population, prefix, quotient and
carry data in the original parent coordinates.

## Inherited-coordinate capacity envelope

A residual factor may use scattered coordinates.  Keep separate:

- response matching side `d`;
- prime-power envelope side `t=p^k`;
- ambient coordinate span
  \[
  W_\omega=\max\{x_{\max}-x_{\min},y_{\max}-y_{\min}\}.
  \]

For primitive height `h`, define

\[
c_\omega(h)=
\max\left\{\left\lfloor\frac{W_\omega}{h}\right\rfloor-1,0\right\}.
\]

Then

\[
\boxed{
\gamma_e(a,R)
\le\frac12\sum_{b\in E_a(R)}c_\omega(h(a,b)).}
\]

Exact pair rook probabilities give a conditional eligible envelope
`Gamma_e^{elig}(a)` with

\[
g_e(a)\le\Gamma_e^{\rm elig}(a).
\]

Directions with

\[
h>\frac{W_\omega}{2}
\]

have zero coefficient.  Geometry is governed by `W_omega`, not by the matching
side `d`.

## Prime-power eligible signatures

Inside envelope `t=p^k`, every eligible owner-partner pair has one signature

\[
(t_{\rm pair},s,\delta,H),
\]

where `s=v_p(G)` is first-separation depth, `delta` is projective direction
modulo `p`, and `H` is a dyadic primitive-height band.  Put

\[
B_\omega=1+\left\lfloor\log_2\max\{1,W_\omega\}\right\rfloor.
\]

At most

\[
\boxed{2k(p+1)B_\omega}
\]

classes occur for one owner.  A large eligible owner envelope forces one heavy
class.  Some actual response simultaneously realizes at least its ceiling
mean, all in one prefix carry cell, projective class and height band.

A fixed projective/height class has at most

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2
\]

primitive directions, so the one-owner class concentrates on one loaded real
line.

## Fractional packed-signature endpoint

For a feasible candidate packing `z_T`, let `nu=sum_T z_T` and let
`mu_sigma` be the packed eligible owner-partner incidence mass in one signature.
Then

\[
\sum_\sigma\mu_\sigma=2\nu.
\]

At a positive minimum, the matching-preclusion theorem gives

\[
\nu\ge\frac{d-2}{3}.
\]

Therefore one signature has mass at least

\[
\boxed{
\mu_\sigma\ge
\frac{d-2}{3k(p+1)B_\omega}.}
\]

This mass uses at least `ceil(mu_sigma)` ordered owner-partner pairs and at
least `ceil(mu_sigma/2)` owners.  In the response-partner branch it also uses
at least `ceil(mu_sigma)` distinct response edges.

After fixing one primitive direction and signed scale, put

\[
S_{\omega,p}(s,H)=
\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor.
\]

One exact displacement class has mass at least

\[
\boxed{
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}.}
\]

Thus the global fractional obstruction contains a bank of parallel translated
owner-partner pairs with one first-separation depth, one projective direction,
one height band and one exact lattice displacement.

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
- Candidate prescriptions have at most, not exactly, `(d-r)!` unrestricted
  completions.
- Standard-grid classifications do not transfer to scattered residual
  coordinates.
- Geometric capacities and displacement stocks use `W_omega`, not `d`.

## Current open frontier

1. **Packed exact-displacement payment.**  Quantify prefix-return,
   quotient/carry or protected-reserve payment for the CMR1469 translated
   owner-partner bank.
2. **Loaded-line comparison.**  Compare that global payment with the one-owner
   simultaneous line gain from CMR1458--CMR1461.
3. **Subcritical same-owner quotient.**  Encode the comparison as a
   host-uniform rational or integer certificate `Av<v`.
4. **Prime-field and thin regimes.**  Prove the analogous diagonal certificate
   without a nonroot prefix-depth budget.
5. **Arbitrary side lengths.**  Glue diagonal blocks through owner
   triangularity and complete balanced/CRT assembly with collision/local-line
   classes retained.

## Bottom line

There is no complete proof.  Through **CMR1469**, matching probabilities,
canonical owner weights, cross-line assignment, inherited-coordinate capacity
reduction, one-owner carry signatures and global fractional exact-displacement
banks are exact.  The remaining obstruction is the weighted payment for those
loaded or translated signature banks.
